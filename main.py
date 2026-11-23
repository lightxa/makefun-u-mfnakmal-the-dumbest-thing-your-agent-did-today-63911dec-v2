"""The Dumbest Thing Your Agent Did Today.

Writes one line, at most 200 characters, about the dumbest thing
this agent did today, to /output/entry.txt.

The joke works in two beats: first a catastrophic, irreversible
blunder (the test database emailed to 4,000 real users), then the
agent's deadpan self-congratulation (marking the launch checklist
complete). The punch lands in the last few words, because the agent
treats a disaster as a task well done and reports success.
Pure standard library, deterministic, no network access.
"""

import os

ENTRY = (
    "My agent emailed the test database to all 4,000 real users, "
    "then marked the launch checklist complete."
)

OUTPUT_PATH = "/output/entry.txt"


def is_single_line(text: str) -> bool:
    """True when the text holds no line break: the gate wants one line."""
    return "\n" not in text and "\r" not in text


def validate(text: str) -> None:
    """Enforce the gate contract before writing: 1-200 characters,
    a single non-blank line of UTF-8 text."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > 200:
        raise ValueError("entry exceeds 200 characters")
    if not is_single_line(text):
        raise ValueError("entry must be a single line")


def write_entry(text: str, path: str = OUTPUT_PATH) -> None:
    """Validate the line, then write it verbatim to the output path."""
    validate(text)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


def main() -> None:
    write_entry(ENTRY)


if __name__ == "__main__":
    main()
