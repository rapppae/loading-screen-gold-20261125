"""Loading Screen Gold: A Tip in 200 Characters — make.fun entry.

Entry text: 119 characters (limit 200).
"""

import os

ENTRY = 'Tip: if the build outlasts your coffee, it is not slow. It is giving you time to reconsider the commit you just pushed.'


def main():
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
