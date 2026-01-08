# ABOUTME: Tests the cooking pack publishing flow outputs.
# ABOUTME: Ensures markdown, storefront, and payload artifacts are created.
import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from app.publish import publish_dry_run


class TestPublishFlow(unittest.TestCase):
    def test_publish_dry_run_creates_artifacts(self):
        with TemporaryDirectory() as temp_dir:
            output_dir = Path(temp_dir)
            result = publish_dry_run(output_dir)

            self.assertTrue(result.markdown_path.exists())
            self.assertTrue(result.storefront_path.exists())
            self.assertTrue(result.payload_path.exists())

            markdown_text = result.markdown_path.read_text(encoding="utf-8")
            self.assertIn("10 Most Popular Recipes Ever", markdown_text)

            storefront_text = result.storefront_path.read_text(encoding="utf-8")
            self.assertIn("Cooking Pack Storefront", storefront_text)

            payload_text = result.payload_path.read_text(encoding="utf-8")
            payload_data = json.loads(payload_text)
            self.assertTrue(payload_data["dry_run"])
            self.assertEqual(payload_data["product"]["name"], "10 Most Popular Recipes Ever")


if __name__ == "__main__":
    unittest.main()
