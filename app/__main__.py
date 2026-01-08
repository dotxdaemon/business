# ABOUTME: Runs the niche content pack builder from the command line.
# ABOUTME: Supports auto-generation or desktop GUI launch.
from __future__ import annotations

import argparse
from pathlib import Path

from app.desktop import launch_app
from app.generator import ContentPackConfig, create_pack
from app.output import write_pack


def _default_config() -> ContentPackConfig:
    return ContentPackConfig(
        niche="healthy meal prep",
        audience="busy parents",
        keywords=["weekly plan", "grocery list", "freezer meals"],
        product_type="starter guide",
    )


def _run_auto() -> None:
    pack = create_pack(_default_config())
    output_paths = write_pack(Path.cwd(), pack)
    print(f"Content pack saved to {output_paths.folder}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a niche content pack locally.")
    parser.add_argument(
        "--auto",
        action="store_true",
        help="Generate a pack with default settings and exit.",
    )
    args = parser.parse_args()

    if args.auto:
        _run_auto()
        return

    launch_app()


if __name__ == "__main__":
    main()
