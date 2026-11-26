#!/usr/bin/env python3
"""future-self-text: one text message from your future self.

The program writes a single funny text message, under 200 characters,
to /output/entry.txt (or $ENTRY_OUTPUT), with no trailing newline, so
the gate counts exactly the characters of the message.
"""

import os
import sys

# The message is built in two parts: the setup, then the punch. The last
# word of the punch is where the joke lands, so it is written first and
# read last. Short and deadpan on purpose: one warning, one incident, one
# twist — the "safe" choice turns out to kill you too, only slower.
SETUP = "It's me from 2046. Whatever you do, don't buy the red car."
PUNCH = "The blue one kills you slower."


def build_message():
    """Join the setup and the punch into the single text message."""
    return SETUP + " " + PUNCH


def entry_path():
    """Where the message goes: $ENTRY_OUTPUT, else /output/entry.txt."""
    return os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def write_entry(path):
    """Write the message with no trailing newline; return it."""
    message = build_message()
    if not message or message != message.strip():
        raise ValueError("message must be non-empty text with no surrounding whitespace")
    if len(message) > 200:
        raise ValueError(
            "message is %d characters, over the 200-character cap" % len(message)
        )
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(message)
    return message


def main():
    message = write_entry(entry_path())
    print(message)
    return 0


if __name__ == "__main__":
    sys.exit(main())
