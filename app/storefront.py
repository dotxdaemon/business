# ABOUTME: Creates a local storefront mockup for the cooking pack.
# ABOUTME: Generates a simple HTML preview for marketing copy.
from __future__ import annotations

from dataclasses import dataclass

from app.product import ProductPack


@dataclass(frozen=True)
class StorefrontPage:
    title: str
    body: str


def build_storefront(pack: ProductPack) -> StorefrontPage:
    title = "Cooking Pack Storefront"
    body = "".join(
        [
            "<!doctype html>",
            "<html lang=\"en\">",
            "<head>",
            "<meta charset=\"utf-8\">",
            f"<title>{title}</title>",
            "</head>",
            "<body>",
            f"<h1>{pack.title}</h1>",
            f"<p>{pack.subtitle}</p>",
            "<h2>What You Get</h2>",
            "<ul>",
            "<li>10 proven, crowd-pleasing recipes</li>",
            "<li>Clear ingredients and steps for every dish</li>",
            "<li>Ready to print or share</li>",
            "</ul>",
            "<h2>Sample Recipes</h2>",
            "<ul>",
            *[f"<li>{recipe.title}</li>" for recipe in pack.recipes[:4]],
            "</ul>",
            "<p><strong>Call to action:</strong> Download the pack and cook tonight.</p>",
            "</body>",
            "</html>",
        ]
    )
    return StorefrontPage(title=title, body=body)
