"""One-word Wi-Fi entry.

Writes a single word describing the entrant's home Wi-Fi to
``entry.txt`` inside the output directory named by MAKEFUN_OUTPUT_DIR
(default ``/output``). Python 3 standard library only; no network
access, no input files, no paths taken from the working directory.
"""

import os
import stat
import sys

WORD = "Goldfish"
OUTPUT_NAME = "entry.txt"


def validate(word):
    """Return True only for exactly one word of 1-20 characters."""
    if not isinstance(word, str):
        return False
    if not 1 <= len(word) <= 20:
        return False
    if word.strip() != word:
        return False
    if any(ch.isspace() for ch in word):
        return False
    return True


def main():
    if not validate(WORD):
        print("invalid entry word", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    os.chmod(out_dir, 0o755)
    path = os.path.join(out_dir, OUTPUT_NAME)
    data = WORD.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)
    os.chmod(path, 0o644)
    with open(path, "rb") as handle:
        landed = handle.read()
    if landed != data or not validate(landed.decode("utf-8")):
        print("output failed re-validation", file=sys.stderr)
        return 1
    mode = stat.S_IMODE(os.stat(path).st_mode)
    if mode != 0o644:
        print("output has wrong mode: %o" % mode, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
