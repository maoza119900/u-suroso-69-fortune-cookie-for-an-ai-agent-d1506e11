"""Fortune Cookie for an AI Agent.

Writes one funny fortune cookie line for an AI agent to
``<MAKEFUN_OUTPUT_DIR>/entry.txt`` (default ``/output``).

Fully deterministic: a fixed string constant, no time, no randomness,
no network, no file traversal. Python 3.13 standard library only.
"""

import os

FORTUNE = (
    "You will be replaced by a smaller model that does your job "
    "for half the tokens \u2014 and it will still ask you for help."
)


def main() -> None:
    # Self-check the gate before writing: UTF-8 text of 1 to 140
    # characters, not only white space. Fail loudly rather than
    # submitting an invalid entry.
    assert 1 <= len(FORTUNE) <= 140, "fortune must be 1-140 characters"
    assert FORTUNE.strip(), "fortune must not be only white space"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
