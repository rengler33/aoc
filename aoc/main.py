import importlib

import utils

YEAR = 2021
DAY = 1


def main():
    input = utils.load_input(YEAR, DAY)
    day_module = importlib.import_module(f"aoc{YEAR}.days.day{DAY}")
    day_module.main(input)


if __name__ == "__main__":
    main()
