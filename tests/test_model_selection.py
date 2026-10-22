import importlib.util
import itertools
import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / ".claude/skills/model-selection/scripts/recommend_model.py"
SPEC = importlib.util.spec_from_file_location("recommend_model", SCRIPT)
ROUTER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ROUTER)
recommend = ROUTER.recommend


class ModelSelectionTests(unittest.TestCase):
    def test_default_is_balanced_and_availability_is_unknown(self):
        result = recommend()
        self.assertEqual(result["recommended_model"], "sonnet")
        self.assertEqual(result["availability"], "unverified")
        self.assertIsNone(result["meets_quality_floor"])
        self.assertFalse(result["session_changed"])

    def test_bounded_low_stakes_task_uses_haiku(self):
        result = recommend(complexity="low", risk="low", ambiguity="low", context="small")
        self.assertEqual(result["recommended_model"], "haiku")
        self.assertEqual(result["selection_command"], "/model haiku")

    def test_ordinary_engineering_uses_sonnet(self):
        self.assertEqual(recommend(complexity="medium", risk="low")["quality_floor"], "sonnet")

    def test_complex_or_ambiguous_cross_system_tasks_use_opus(self):
        for inputs in ({"complexity": "high"}, {"risk": "high"},
                       {"complexity": "medium", "ambiguity": "high"},
                       {"complexity": "medium", "context": "large"}):
            with self.subTest(inputs=inputs):
                self.assertEqual(recommend(**inputs)["quality_floor"], "opus")

    def test_economy_preference_can_reduce_low_stakes_choice(self):
        inputs = dict(complexity="low", risk="low", ambiguity="medium", context="medium")
        self.assertEqual(recommend(**inputs)["recommended_model"], "sonnet")
        self.assertEqual(recommend(**inputs, budget="low-cost")["recommended_model"], "haiku")
        self.assertEqual(recommend(**inputs, latency="fast")["recommended_model"], "haiku")

    def test_explicit_quality_precedes_latency_tradeoff(self):
        result = recommend(complexity="low", risk="low", ambiguity="medium",
                           context="medium", budget="quality", latency="fast")
        self.assertEqual(result["recommended_model"], "sonnet")

    def test_high_risk_never_downgrades_for_cost_or_latency(self):
        for complexity, ambiguity, budget, latency in itertools.product(
                ROUTER.LEVELS, ROUTER.LEVELS, ("balanced", "low-cost", "quality"), ("normal", "fast")):
            with self.subTest(complexity=complexity, ambiguity=ambiguity, budget=budget, latency=latency):
                result = recommend(complexity=complexity, ambiguity=ambiguity, risk="high",
                                   budget=budget, latency=latency)
                self.assertEqual(result["quality_floor"], "opus")

    def test_availability_uses_least_capable_family_meeting_floor(self):
        result = recommend(complexity="low", risk="low", ambiguity="low", context="small",
                           available=["opus", "sonnet"])
        self.assertEqual(result["recommended_model"], "sonnet")
        self.assertEqual(result["quality_floor"], "haiku")
        self.assertTrue(result["meets_quality_floor"])
        self.assertTrue(result["warning"])

    def test_available_but_inadequate_family_is_explicit(self):
        result = recommend(risk="high", available=["haiku", "sonnet"])
        self.assertEqual(result["recommended_model"], "sonnet")
        self.assertEqual(result["quality_floor"], "opus")
        self.assertFalse(result["meets_quality_floor"])
        self.assertTrue(result["warning"])

    def test_empty_availability_selects_nothing(self):
        result = recommend(available=[])
        self.assertIsNone(result["recommended_model"])
        self.assertIsNone(result["selection_command"])
        self.assertFalse(result["meets_quality_floor"])

    def test_invalid_dimensions_and_aliases_are_rejected(self):
        for key in ("complexity", "risk", "ambiguity", "context", "budget", "latency"):
            with self.subTest(key=key), self.assertRaises(ValueError):
                recommend(**{key: "invalid"})
        for available in (["imaginary-model"], "haiku"):
            with self.subTest(available=available), self.assertRaises(ValueError):
                recommend(available=available)

    def test_available_input_is_not_modified(self):
        available = ["opus", "haiku"]
        recommend(available=available)
        self.assertEqual(available, ["opus", "haiku"])

    def test_cli_emits_json_for_a_real_decision(self):
        run = subprocess.run([sys.executable, str(SCRIPT), "--risk", "high", "--available", "haiku"],
                             text=True, capture_output=True, check=True)
        result = json.loads(run.stdout)
        self.assertEqual(result["quality_floor"], "opus")
        self.assertFalse(result["meets_quality_floor"])
        self.assertFalse(result["session_changed"])

    def test_cli_rejects_unknown_alias(self):
        run = subprocess.run([sys.executable, str(SCRIPT), "--available", "imaginary-model"],
                             text=True, capture_output=True)
        self.assertEqual(run.returncode, 2)
        self.assertEqual(run.stdout, "")


if __name__ == "__main__":
    unittest.main()
