#!/usr/bin/env python3
"""One Line of Earned Pride entry: writes one line to /output/entry.txt."""

LINE = "The boy who stuttered through every reading lesson stood up at the town fair and read his own poem aloud, slowly, without stopping once."

# The gate: /output/entry.txt must hold 1 to 240 characters of real text,
# on a single line (the brief asks for one line, not a paragraph).
assert 1 <= len(LINE) <= 240 and LINE.strip(), "line must be 1-240 characters"
assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
assert LINE == LINE.strip(), "no leading or trailing whitespace"

if __name__ == "__main__":
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
