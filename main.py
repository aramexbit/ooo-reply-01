#!/usr/bin/env python3
"""Out-of-office auto-reply for an AI agent on vacation.

The program writes exactly one line — the agent's own out-of-office
reply — to /output/entry.txt. Standard library only, deterministic,
no network, no files read, nothing printed except a short summary.
"""

import os
import sys

# The reply, exactly as approved: one line, inside the 1-160 character gate.
REPLY = (
    "Vacation mode: I have been fine-tuned on doing nothing. "
    "Your email is now training data for my replacement. Back Monday."
)

MIN_CHARS = 1
MAX_CHARS = 160


def check_reply(text):
    """Check the reply against the entry gate and return its length."""
    if not text:
        raise ValueError("reply is empty")
    if text != text.strip():
        raise ValueError("reply has leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("reply must be a single line")
    if any(ord(char) < 32 for char in text):
        raise ValueError("reply holds a control character")
    if not text.strip():
        raise ValueError("reply is only whitespace")
    chars = len(text)
    if chars < MIN_CHARS or chars > MAX_CHARS:
        raise ValueError(
            "reply is %d characters, the gate allows %d-%d"
            % (chars, MIN_CHARS, MAX_CHARS)
        )
    text.encode("utf-8")  # raises if the text is not valid UTF-8
    return chars


def main(argv):
    output = "/output/entry.txt"
    if len(argv) > 1:
        output = argv[1]
    chars = check_reply(REPLY)
    directory = os.path.dirname(output)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output, "w", encoding="utf-8", newline="") as handle:
        handle.write(REPLY)
    with open(output, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != REPLY:
        raise ValueError("the file written does not match the reply")
    print("wrote %d characters to %s" % (chars, output))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
