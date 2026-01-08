# ABOUTME: Provides a desktop interface for generating niche content packs.
# ABOUTME: Captures user inputs and saves output files locally.
import tkinter as tk
from tkinter import messagebox
from pathlib import Path

from app.generator import ContentPackConfig, create_pack
from app.output import write_pack


class ContentPackApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Niche Content Pack Builder")

        self.niche_var = tk.StringVar(value="healthy meal prep")
        self.audience_var = tk.StringVar(value="busy parents")
        self.keywords_var = tk.StringVar(value="weekly plan, grocery list, freezer meals")
        self.product_type_var = tk.StringVar(value="starter guide")

        self._build_form()

    def _build_form(self) -> None:
        container = tk.Frame(self.root, padx=16, pady=16)
        container.pack(fill="both", expand=True)

        fields = [
            ("Niche", self.niche_var),
            ("Audience", self.audience_var),
            ("Keywords (comma-separated)", self.keywords_var),
            ("Product type", self.product_type_var),
        ]

        for row, (label, variable) in enumerate(fields):
            tk.Label(container, text=label).grid(row=row, column=0, sticky="w", pady=4)
            tk.Entry(container, textvariable=variable, width=50).grid(
                row=row, column=1, sticky="ew", pady=4
            )

        container.columnconfigure(1, weight=1)

        button = tk.Button(container, text="Generate & Save Pack", command=self._generate_pack)
        button.grid(row=len(fields), column=0, columnspan=2, pady=(12, 0))

    def _generate_pack(self) -> None:
        config = ContentPackConfig(
            niche=self.niche_var.get().strip(),
            audience=self.audience_var.get().strip(),
            keywords=[keyword.strip() for keyword in self.keywords_var.get().split(",")],
            product_type=self.product_type_var.get().strip(),
        )

        pack = create_pack(config)
        output_paths = write_pack(Path.cwd(), pack)

        messagebox.showinfo(
            "Pack created",
            f"Saved to {output_paths.folder}",
        )


def launch_app() -> None:
    root = tk.Tk()
    app = ContentPackApp(root)
    root.mainloop()
