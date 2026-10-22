#!/usr/bin/env python3
"""Recommend a model family without calling APIs or changing configuration."""

import argparse
import json

MODELS = ("haiku", "sonnet", "opus")
LEVELS = ("low", "medium", "high")


def recommend(*, complexity="medium", risk="medium", ambiguity="medium",
              context="medium", budget="balanced", latency="normal", available=None):
    """Return an explainable policy decision; availability None means unknown."""
    inputs = dict(complexity=complexity, risk=risk, ambiguity=ambiguity,
                  context=context, budget=budget, latency=latency)
    choices = dict(complexity=LEVELS, risk=LEVELS, ambiguity=LEVELS,
                   context=("small", "medium", "large"),
                   budget=("balanced", "low-cost", "quality"), latency=("normal", "fast"))
    for key, value in inputs.items():
        if value not in choices[key]:
            raise ValueError(f"Invalid {key}: {value!r}")
    if available is not None:
        if isinstance(available, str):
            raise ValueError("available must be a list of aliases, not a string")
        available = list(available)
        if any(model not in MODELS for model in available):
            raise ValueError("available must contain only haiku, sonnet, or opus")

    if risk == "high" or complexity == "high":
        floor, reason = "opus", "High risk or complexity requires the strongest reasoning tier."
    elif ambiguity == "high" and complexity != "low":
        floor, reason = "opus", "Ambiguous work with interacting decisions needs deeper reasoning."
    elif context == "large" and complexity != "low":
        floor, reason = "opus", "Broad context and interacting decisions need cross-system reasoning."
    elif (complexity, risk, ambiguity, context) == ("low", "low", "low", "small"):
        floor, reason = "haiku", "The task is bounded, clear, and low stakes."
    elif (complexity == "low" and risk == "low" and ambiguity != "high"
          and context != "large" and (budget == "low-cost" or latency == "fast")
          and budget != "quality"):
        floor, reason = "haiku", "A low-stakes task permits the requested cost or latency tradeoff."
    else:
        floor, reason = "sonnet", "Use balanced reasoning for ordinary engineering and analysis."

    selected = floor
    meets_floor = None if available is None else True
    warning = None
    if available is not None and floor not in available:
        capable = [model for model in MODELS if model in available
                   and MODELS.index(model) >= MODELS.index(floor)]
        if capable:
            selected = capable[0]
            warning = f"{floor} is unavailable; {selected} meets the quality floor."
        else:
            selected = next((model for model in reversed(MODELS) if model in available), None)
            meets_floor = False
            warning = "No available alias meets the quality floor; obtain access or rescope the task."
    return dict(recommended_model=selected, quality_floor=floor, reason=reason,
                availability="unverified" if available is None else "provided",
                meets_quality_floor=meets_floor, warning=warning, inputs=inputs,
                selection_command=f"/model {selected}" if selected else None,
                session_changed=False)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--complexity", choices=LEVELS, default="medium")
    parser.add_argument("--risk", choices=LEVELS, default="medium")
    parser.add_argument("--ambiguity", choices=LEVELS, default="medium")
    parser.add_argument("--context", choices=("small", "medium", "large"), default="medium")
    parser.add_argument("--budget", choices=("balanced", "low-cost", "quality"), default="balanced")
    parser.add_argument("--latency", choices=("normal", "fast"), default="normal")
    parser.add_argument("--available", nargs="*", choices=MODELS, default=None,
                        help="Verified available aliases; omit if unknown, empty means none.")
    print(json.dumps(recommend(**vars(parser.parse_args(argv))), indent=2))


if __name__ == "__main__":
    main()
