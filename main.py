import argparse
from pathlib import Path


ENTRY = 'My boss took me aside to say my voice carries in the open office. From three rows over, Dave said, "So does yours."'


def main():
    parser = argparse.ArgumentParser(description="Write the office joke entry.")
    parser.add_argument(
        "destination",
        nargs="?",
        type=Path,
        default="/output/entry.txt",
        help="output file (default: %(default)s)",
    )
    destination = parser.parse_args().destination
    try:
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(ENTRY.encode("utf-8"))
    except OSError as error:
        parser.exit(1, f"{parser.prog}: {error}\n")


if __name__ == "__main__":
    main()
