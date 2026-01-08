# ABOUTME: Tests content pack generation behavior.
# ABOUTME: Validates output structure for niche content packs.
import unittest

from app.generator import ContentPackConfig, create_pack


class TestContentPackGeneration(unittest.TestCase):
    def test_create_pack_returns_expected_sections(self):
        config = ContentPackConfig(
            niche="home espresso",
            audience="busy beginners",
            keywords=["espresso machine", "grind size", "milk steaming"],
            product_type="starter guide",
        )

        pack = create_pack(config)

        self.assertEqual(pack["niche"], "home espresso")
        self.assertEqual(pack["audience"], "busy beginners")
        self.assertEqual(pack["product_type"], "starter guide")
        self.assertTrue(pack["title"])
        self.assertTrue(pack["tagline"])
        self.assertEqual(len(pack["outline"]), 7)
        self.assertEqual(len(pack["content_calendar"]), 30)
        self.assertIn("pricing", pack)
        self.assertIn("sales_page", pack)
        self.assertIn("launch_checklist", pack)


if __name__ == "__main__":
    unittest.main()
