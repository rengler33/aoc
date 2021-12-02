import importlib

import utils

YEAR = 2021
DAY = 1


def main(year, day):
    input = utils.load_input(year, day)
    importlib.import_module(f"aoc{year}.days.day{day}").main(input)


if __name__ == "__main__":
    main(YEAR, DAY)
