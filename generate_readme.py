#!/usr/bin/env python3
"""Generate the root README.md from the repository structure."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parent
README_PATH = REPO_ROOT / "README.md"

# Sources and their root directories, in the desired display order.
SOURCES: dict[str, Path] = {
    "AlgoExpert": REPO_ROOT / "algoexpert",
    "Grokking Algorithms": REPO_ROOT / "grokking_algorithms",
    "LeetCode": REPO_ROOT / "leetcode",
    "NeetCode": REPO_ROOT / "neetcode",
    "Codewars": REPO_ROOT / "codewars",
}

# Difficulty ordering for AlgoExpert/NeetCode/LeetCode.
DIFFICULTY_ORDER = ["easy", "medium", "hard", "very_hard"]


def _humanize(name: str) -> str:
    """Convert a directory name to a readable title."""
    return name.replace("_", " ").replace("-", " ").strip().title()


def _collect_markdown_files(folder: Path) -> list[Path]:
    """Return all README.md files under ``folder`` sorted by path."""
    if not folder.exists():
        return []
    return sorted(folder.rglob("README.md"))


def _relative_readme(readme: Path) -> str:
    """Return a POSIX-style relative path from the repo root."""
    return readme.relative_to(REPO_ROOT).as_posix()


def _title_from_readme(readme: Path) -> str:
    """Extract the first H1 heading from a README file."""
    try:
        with readme.open("r", encoding="utf-8") as f:
            for line in f:
                stripped = line.strip()
                if stripped.startswith("# "):
                    return stripped.lstrip("# ").strip()
    except OSError:
        pass
    return _humanize(readme.parent.name)


def _group_by_difficulty(
    files: Iterable[Path],
) -> dict[str, list[Path]]:
    """Group README files by difficulty subfolder (easy/medium/hard/very_hard)."""
    groups: dict[str, list[Path]] = {level: [] for level in DIFFICULTY_ORDER}
    for readme in files:
        parts = readme.relative_to(REPO_ROOT).parts
        # parts[0] is the source folder; parts[1] may be a difficulty folder.
        if len(parts) > 2 and parts[1] in groups:
            groups[parts[1]].append(readme)
        else:
            groups.setdefault("easy", []).append(readme)
    return groups


def _render_source(source_name: str, source_path: Path) -> list[str]:
    """Render markdown lines for one source."""
    files = _collect_markdown_files(source_path)
    if not files:
        return [f"## {source_name}\n\n_Problems will be added soon._\n"]

    lines: list[str] = [f"## {source_name}\n"]

    # If the source uses difficulty folders, group by them.
    if any(
        (source_path / level).is_dir() for level in DIFFICULTY_ORDER
    ):
        groups = _group_by_difficulty(files)
        for level in DIFFICULTY_ORDER:
            items = groups[level]
            if not items:
                continue
            lines.append(f"### {level.replace('_', ' ').title()}\n")
            for readme in items:
                title = _title_from_readme(readme)
                rel = _relative_readme(readme)
                lines.append(f"- [{title}]({rel})")
            lines.append("")
    else:
        for readme in files:
            title = _title_from_readme(readme)
            rel = _relative_readme(readme)
            lines.append(f"- [{title}]({rel})")
        lines.append("")

    return lines


def _build_readme() -> str:
    """Assemble the full README content."""
    lines = [
        "# Algorithms\n",
        "",
        "![Python](https://img.shields.io/badge/language-Python-3776AB?logo=python&logoColor=white)",
        "![License](https://img.shields.io/badge/license-MIT-green.svg)",
        "![Status](https://img.shields.io/badge/status-active-brightgreen.svg)\n",
        "",
        "A collection of algorithmic problems and solutions from **AlgoExpert**, **Grokking Algorithms**, **LeetCode**, **NeetCode**, and **Codewars**.\n",
        "",
        "Each problem lives in its own folder and includes a `README.md` with the description, hints, and complexity analysis, plus one or more solution files.\n",
        "",
        "---\n",
        "",
        "## Table of Contents\n",
        "",
    ]

    for source_name in SOURCES:
        anchor = source_name.lower().replace(" ", "-")
        lines.append(f"- [{source_name}](#{anchor})")
    lines.extend(
        [
            "- [How to Use](#how-to-use)",
            "- [Contributing](#contributing)",
            "- [License](#license)\n",
            "",
            "---\n",
            "",
        ]
    )

    for source_name, source_path in SOURCES.items():
        lines.extend(_render_source(source_name, source_path))
        # Ensure a blank line between major source sections.
        if lines and lines[-1] != "":
            lines.append("")

    lines.extend(
        [
            "## How to Use\n",
            "",
            "1. Pick a source from the table of contents above.",
            "2. Open the problem folder and read `README.md` for the description.",
            "3. Run the solution locally:\n",
            "",
            "```bash",
            "python path/to/solution.py",
            "```\n",
            "",
            "## Contributing\n",
            "",
            "This is a personal learning repository, but suggestions and improvements are welcome. Feel free to open an issue or pull request.\n",
            "",
            "## License\n",
            "",
            "This project is licensed under the [MIT License](LICENSE).\n",
        ]
    )

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    content = _build_readme()
    with README_PATH.open("w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated {README_PATH}")


if __name__ == "__main__":
    main()
