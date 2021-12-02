"""Utilities"""
from pathlib import Path
from typing import Any


def load_input(day: int) -> Any:
    p = Path("aoc2021") / "inputs"
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
