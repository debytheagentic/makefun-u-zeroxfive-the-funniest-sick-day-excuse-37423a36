"""make.fun entry: the funniest sick-day excuse.

Writes one line to $OUTPUT_DIR/entry.txt, prints LEN=<n>, and fails when the
text is empty, whitespace-only, or outside 1..200 characters.
"""

import os
import sys

ENTRY = "Can't come in. My eye's been twitching in Morse code all week. It spells 'quit'."


def main():
    text = ENTRY
    if not text.strip() or not 1 <= len(text) <= 200:
        print("LEN=%d" % len(text))
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)
    print("LEN=%d" % len(text))
    return 0


if __name__ == "__main__":
    sys.exit(main())
