import importlib

import utils


def main():
    DAY = 1
    input = utils.load_input(DAY)
    day_module = importlib.import_module(f"days.day{DAY}")
    day_module.main(input)


if __name__ == "__main__":
    main()
