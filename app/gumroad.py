# ABOUTME: Builds Gumroad payloads for a cooking product pack.
# ABOUTME: Captures metadata for dry-run publishing workflows.
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone

from app.product import ProductPack


@dataclass(frozen=True)
class GumroadPayload:
    dry_run: bool
    product: dict[str, object]


def build_payload(pack: ProductPack) -> GumroadPayload:
    return GumroadPayload(
        dry_run=True,
        product={
            "name": pack.title,
            "description": pack.subtitle,
            "price": 9,
            "currency": "USD",
            "file_name": "10-most-popular-recipes-ever.md",
            "generated_at": datetime.now(timezone.utc).isoformat(),
        },
    )
