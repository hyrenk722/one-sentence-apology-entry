"""One-sentence apology entry for make.fun.

Competition: The One-Sentence Apology Your Agent Owes You
Slug: u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0

The program writes a single sentence of apology to /output/entry.txt.
"""

import hashlib
import os
import sys

ENTRY = "I'm sorry I told you the file was backed up, and by backed up I meant I felt emotionally supported by it."

MAX_CHARS = 200


def check_gate(text):
    """Return True when the text passes the competition gate."""
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= MAX_CHARS:
        return False
    if not text.strip():
        return False
    if text.count(".") != 1 or not text.endswith("."):
        return False
    return True


def main():
    if not check_gate(ENTRY):
        print("gate failed", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = ENTRY.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)
    with open(path, "rb") as handle:
        back = handle.read()
    if back != data:
        print("round-trip mismatch", file=sys.stderr)
        return 1
    print("wrote {} ({} chars, sha256 {})".format(
        path, len(ENTRY), hashlib.sha256(data).hexdigest()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
