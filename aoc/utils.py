"""Utilities"""
from pathlib import Path
from typing import Any


def load_input(year: int, day: int) -> Any:
    p = Path("aoc") / f"aoc{year}" / "inputs"
    filepath = p / f"day{day}.txt"
    try:
        with open(filepath) as f:
            for line in f.readlines():
                yield line.strip()
    except FileNotFoundError:
        raise


if __name__ == "__main__":
    input = load_input(1)
    print(list(input))
