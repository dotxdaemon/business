# ABOUTME: Writes generated content packs to disk in multiple formats.
# ABOUTME: Creates organized folders for niche content assets.
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class OutputPaths:
    folder: Path
    markdown: Path
    html: Path


def write_pack(output_root: Path, pack: dict[str, object]) -> OutputPaths:
    folder_name = f"content_pack_{_slugify(pack['niche'])}"
    folder = output_root / folder_name
    folder.mkdir(parents=True, exist_ok=True)

    markdown_path = folder / "content-pack.md"
    html_path = folder / "content-pack.html"

    markdown_path.write_text(_render_markdown(pack), encoding="utf-8")
    html_path.write_text(_render_html(pack), encoding="utf-8")

    return OutputPaths(folder=folder, markdown=markdown_path, html=html_path)


def _render_markdown(pack: dict[str, object]) -> str:
    outline_items = "\n".join(f"- {item}" for item in pack["outline"])
    calendar_items = "\n".join(f"- {item}" for item in pack["content_calendar"])
    checklist_items = "\n".join(f"- {item}" for item in pack["launch_checklist"])

    pricing = pack["pricing"]
    sales_page = pack["sales_page"]

    return "\n".join(
        [
            f"# {pack['title']}",
            f"{pack['tagline']}",
            "",
            "## Outline",
            outline_items,
            "",
            "## 30-Day Content Calendar",
            calendar_items,
            "",
            "## Pricing",
            f"Anchor price: ${pricing['anchor_price']}",
            f"Intro price: ${pricing['intro_price']}",
            pricing["reasoning"],
            "",
            "## Sales Page Copy",
            f"Headline: {sales_page['headline']}",
            f"Subheadline: {sales_page['subheadline']}",
            "Pain points:",
            "\n".join(f"- {item}" for item in sales_page["pain_points"]),
            "Benefits:",
            "\n".join(f"- {item}" for item in sales_page["benefits"]),
            f"CTA: {sales_page['call_to_action']}",
            "",
            "## Launch Checklist",
            checklist_items,
        ]
    )


def _render_html(pack: dict[str, object]) -> str:
    outline_items = "".join(f"<li>{item}</li>" for item in pack["outline"])
    calendar_items = "".join(f"<li>{item}</li>" for item in pack["content_calendar"])
    checklist_items = "".join(f"<li>{item}</li>" for item in pack["launch_checklist"])

    pricing = pack["pricing"]
    sales_page = pack["sales_page"]

    return "".join(
        [
            "<!doctype html>",
            "<html lang=\"en\">",
            "<head>",
            "<meta charset=\"utf-8\">",
            f"<title>{pack['title']}</title>",
            "</head>",
            "<body>",
            f"<h1>{pack['title']}</h1>",
            f"<p>{pack['tagline']}</p>",
            "<h2>Outline</h2>",
            f"<ul>{outline_items}</ul>",
            "<h2>30-Day Content Calendar</h2>",
            f"<ul>{calendar_items}</ul>",
            "<h2>Pricing</h2>",
            f"<p>Anchor price: ${pricing['anchor_price']}</p>",
            f"<p>Intro price: ${pricing['intro_price']}</p>",
            f"<p>{pricing['reasoning']}</p>",
            "<h2>Sales Page Copy</h2>",
            f"<p><strong>{sales_page['headline']}</strong></p>",
            f"<p>{sales_page['subheadline']}</p>",
            "<h3>Pain points</h3>",
            "<ul>" + "".join(f"<li>{item}</li>" for item in sales_page["pain_points"]) + "</ul>",
            "<h3>Benefits</h3>",
            "<ul>" + "".join(f"<li>{item}</li>" for item in sales_page["benefits"]) + "</ul>",
            f"<p>{sales_page['call_to_action']}</p>",
            "<h2>Launch Checklist</h2>",
            f"<ul>{checklist_items}</ul>",
            "</body>",
            "</html>",
        ]
    )


def _slugify(value: str) -> str:
    return "".join(char.lower() if char.isalnum() else "_" for char in value).strip("_")
