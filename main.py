"""The One-Line Laugh — writes one funny line to /output/entry.txt."""

LINE = (
    "My houseplant died of neglect, my sourdough died of attention \u2014 "
    "turns out I'm not a caretaker, I'm a climate."
)


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
