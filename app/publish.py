# ABOUTME: Coordinates dry-run publishing for the cooking pack.
# ABOUTME: Writes markdown, storefront, and Gumroad payload artifacts.
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from app.gumroad import build_payload
from app.product import build_pack, render_markdown
from app.recipes import get_popular_recipes
from app.storefront import build_storefront


@dataclass(frozen=True)
class PublishResult:
    markdown_path: Path
    storefront_path: Path
    payload_path: Path


def publish_dry_run(output_root: Path) -> PublishResult:
    recipes = get_popular_recipes()
    pack = build_pack(recipes)
    markdown_text = render_markdown(pack)
    storefront_page = build_storefront(pack)
    payload = build_payload(pack)

    output_dir = output_root / "cooking-pack"
    output_dir.mkdir(parents=True, exist_ok=True)

    markdown_path = output_dir / "10-most-popular-recipes-ever.md"
    storefront_path = output_dir / "storefront-mockup.html"
    payload_path = output_dir / "gumroad-dry-run.json"

    markdown_path.write_text(markdown_text, encoding="utf-8")
    storefront_path.write_text(storefront_page.body, encoding="utf-8")
    payload_path.write_text(
        json.dumps({"dry_run": payload.dry_run, "product": payload.product}, indent=2),
        encoding="utf-8",
    )

    return PublishResult(
        markdown_path=markdown_path,
        storefront_path=storefront_path,
        payload_path=payload_path,
    )
