# ABOUTME: Generates niche content packs from user configuration.
# ABOUTME: Builds titles, outlines, and launch materials for output.
from __future__ import annotations

from dataclasses import dataclass
from itertools import cycle


@dataclass(frozen=True)
class ContentPackConfig:
    niche: str
    audience: str
    keywords: list[str]
    product_type: str


def create_pack(config: ContentPackConfig) -> dict[str, object]:
    title = _build_title(config)
    tagline = _build_tagline(config)
    outline = _build_outline(config)
    calendar = _build_calendar(config)
    pricing = _build_pricing(config)
    sales_page = _build_sales_page(config, title, tagline)
    launch_checklist = _build_launch_checklist(config)

    return {
        "niche": config.niche,
        "audience": config.audience,
        "product_type": config.product_type,
        "title": title,
        "tagline": tagline,
        "outline": outline,
        "content_calendar": calendar,
        "pricing": pricing,
        "sales_page": sales_page,
        "launch_checklist": launch_checklist,
    }


def _build_title(config: ContentPackConfig) -> str:
    keyword = config.keywords[0] if config.keywords else config.niche
    return f"{config.product_type.title()} for {config.audience.title()}: Master {keyword.title()}"


def _build_tagline(config: ContentPackConfig) -> str:
    return (
        f"A focused roadmap for {config.audience} to get results in {config.niche} "
        "without the overwhelm."
    )


def _build_outline(config: ContentPackConfig) -> list[str]:
    starter = [
        f"Define your {config.niche} goals and success metrics",
        f"Set up the essential {config.niche} toolkit",
        f"Quick-start workflow for {config.audience}",
    ]
    keyword_items = [
        f"Deep dive: {keyword.title()}" for keyword in _normalize_keywords(config.keywords, target_count=2)
    ]
    closing = [
        "Troubleshooting checklist",
        "Next steps and scaling plan",
    ]
    return starter + keyword_items + closing


def _build_calendar(config: ContentPackConfig) -> list[str]:
    topics = []
    keyword_cycle = cycle(_normalize_keywords(config.keywords, target_count=6))
    for day in range(1, 31):
        keyword = next(keyword_cycle)
        topics.append(
            f"Day {day}: {keyword.title()} tip for {config.audience} in {config.niche}"
        )
    return topics


def _build_pricing(config: ContentPackConfig) -> dict[str, object]:
    return {
        "anchor_price": 49,
        "intro_price": 29,
        "reasoning": (
            f"{config.product_type.title()} positioned for fast wins, priced as an impulse buy for "
            f"{config.audience}."
        ),
    }


def _build_sales_page(config: ContentPackConfig, title: str, tagline: str) -> dict[str, object]:
    return {
        "headline": title,
        "subheadline": tagline,
        "pain_points": [
            f"Too many conflicting {config.niche} tips",
            "Not enough time to piece together a plan",
            f"Unclear which {config.niche} steps matter first",
        ],
        "benefits": [
            "Clear, step-by-step path",
            "Actionable checklists and templates",
            "Quick wins in the first week",
        ],
        "call_to_action": "Download the starter pack and launch today.",
    }


def _build_launch_checklist(config: ContentPackConfig) -> list[str]:
    return [
        "Finalize the cover and branding",
        "Upload the product to your sales platform",
        "Draft the announcement email",
        f"Schedule the first 7 {config.niche} content posts",
        "Collect early testimonials from beta users",
        "Review pricing after first 10 sales",
    ]


def _normalize_keywords(keywords: list[str], target_count: int) -> list[str]:
    cleaned = [keyword.strip() for keyword in keywords if keyword.strip()]
    if not cleaned:
        cleaned = ["core concept"]
    while len(cleaned) < target_count:
        cleaned.append(cleaned[len(cleaned) % len(cleaned)])
    return cleaned[:target_count]
