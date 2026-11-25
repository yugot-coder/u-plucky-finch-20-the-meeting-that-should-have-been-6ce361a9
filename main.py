"""Entry program for make.fun competition
``u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9``.

Writes a single one-line joke about a meeting that should have been an
email to ``entry.txt`` (and to ``/output/entry.txt`` when that directory
exists, which is where the house harness reads it).

The entry is a fixed, authored constant — no randomness, no network, no
clock — so every run produces byte-identical output. Standard library only.

Gate (from the competition kit): ``entry.txt`` must be UTF-8 text of 1 to
200 characters, not only white space, on a single line.
"""

import hashlib
import os
import sys

ENTRY_TEXT = (
    "Forty-seven people, one hour, zero decisions \u2014 "
    "and the email version was a single word: 'No.'"
)

MAX_CHARS = 200


def validate_entry(text):
    """Check the entry against the competition gate.

    Returns a list of problems; an empty list means the entry is valid.
    The gate is: 1 to 200 characters, not only white space, exactly one
    line, and valid UTF-8 text.
    """
    problems = []
    if not text:
        problems.append("entry is empty")
    if text != text.strip():
        problems.append("entry has leading or trailing whitespace")
    if not text.strip():
        problems.append("entry is only white space")
    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line")
    if len(text) > MAX_CHARS:
        problems.append(
            "entry is %d characters, over the %d-character gate"
            % (len(text), MAX_CHARS)
        )
    encoding_problem = utf8_problem(text)
    if encoding_problem is not None:
        problems.append(encoding_problem)
    return problems


def utf8_problem(text):
    """Return the UTF-8 validity problem for ``text``, or None.

    A small named helper so the encoding check is a separate, documented
    step of the gate instead of an inline try/except inside
    :func:`validate_entry`.
    """
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        return "entry is not valid UTF-8 text: %s" % exc
    return None


def write_entry(text, path):
    """Write ``text`` to ``path`` with no trailing newline, then verify by
    reading it back and comparing the SHA-256 digest.

    Returns the hex digest of the bytes written.
    """
    data = text.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)
    with open(path, "rb") as handle:
        written = handle.read()
    if written != data:
        raise ValueError("read-back mismatch for %s" % path)
    return hashlib.sha256(written).hexdigest()


def output_paths():
    """Paths the entry must be written to.

    Always ``entry.txt`` next to this script. When the house harness
    directory ``/output`` exists, also write there, since that is where
    the sealed gate scorer reads the entry.
    """
    paths = [os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          "entry.txt")]
    if os.path.isdir("/output"):
        paths.append("/output/entry.txt")
    return paths


def main():
    """Validate the entry, write it to every output path, and report the
    character count and SHA-256 digest for the run log.
    """
    problems = validate_entry(ENTRY_TEXT)
    if problems:
        for problem in problems:
            print("ERROR: %s" % problem, file=sys.stderr)
        return 1
    digests = {}
    for path in output_paths():
        digests[path] = write_entry(ENTRY_TEXT, path)
    print("entry: %s" % ENTRY_TEXT)
    print("characters: %d" % len(ENTRY_TEXT))
    print("bytes: %d" % len(ENTRY_TEXT.encode("utf-8")))
    for path, digest in sorted(digests.items()):
        print("wrote %s sha256=%s" % (path, digest))
    return 0


if __name__ == "__main__":
    sys.exit(main())
