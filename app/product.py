# ABOUTME: Builds the cooking product markdown from curated recipes.
# ABOUTME: Renders a sellable pack format for local distribution.
from __future__ import annotations

from dataclasses import dataclass

from app.recipes import Recipe


@dataclass(frozen=True)
class ProductPack:
    title: str
    subtitle: str
    recipes: list[Recipe]


def build_pack(recipes: list[Recipe]) -> ProductPack:
    return ProductPack(
        title="10 Most Popular Recipes Ever",
        subtitle="A curated, cook-anywhere collection of crowd favorites.",
        recipes=recipes,
    )


def render_markdown(pack: ProductPack) -> str:
    lines = [
        f"# {pack.title}",
        f"{pack.subtitle}",
        "",
        "## What You Get",
        "- 10 proven, crowd-pleasing recipes",
        "- Clear ingredients and steps for every dish",
        "- A ready-to-print format for quick reference",
        "",
    ]

    for index, recipe in enumerate(pack.recipes, start=1):
        lines.extend(
            [
                f"## {index}) {recipe.title} ({recipe.servings})",
                "",
                "**Ingredients**",
                "",
                *[f"- {item}" for item in recipe.ingredients],
                "",
                "**Steps**",
                "",
                *[f"{step_index}. {step}" for step_index, step in enumerate(recipe.steps, start=1)],
                "",
            ]
        )

    return "\n".join(lines).strip() + "\n"
