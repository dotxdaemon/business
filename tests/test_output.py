# ABOUTME: Tests writing content packs to disk.
# ABOUTME: Ensures markdown and HTML outputs are created.
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from app.generator import ContentPackConfig, create_pack
from app.output import write_pack


class TestOutputWriter(unittest.TestCase):
    def test_write_pack_creates_files(self):
        config = ContentPackConfig(
            niche="home espresso",
            audience="busy beginners",
            keywords=["espresso machine", "grind size", "milk steaming"],
            product_type="starter guide",
        )
        pack = create_pack(config)

        with TemporaryDirectory() as temp_dir:
            output_paths = write_pack(Path(temp_dir), pack)

            self.assertTrue(output_paths.folder.exists())
            self.assertTrue(output_paths.markdown.exists())
            self.assertTrue(output_paths.html.exists())
            self.assertIn(pack["title"], output_paths.markdown.read_text(encoding="utf-8"))
            self.assertIn(pack["title"], output_paths.html.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
