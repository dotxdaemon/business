# ABOUTME: Runs the cooking pack dry-run publisher from the command line.
# ABOUTME: Emits local artifacts for markdown, storefront, and payload data.
from __future__ import annotations

import argparse
from pathlib import Path

from app.publish import publish_dry_run


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a cooking pack and Gumroad dry-run payload.")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path.cwd(),
        help="Output directory for generated files.",
    )
    args = parser.parse_args()

    result = publish_dry_run(args.output)
    print("Dry-run complete.")
    print(f"Markdown: {result.markdown_path}")
    print(f"Storefront: {result.storefront_path}")
    print(f"Payload: {result.payload_path}")


if __name__ == "__main__":
    main()
