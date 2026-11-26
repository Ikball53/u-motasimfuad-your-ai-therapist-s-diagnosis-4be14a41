"""Your AI Therapist's Diagnosis — one-liner entry.

Writes a single deadpan clinical diagnosis line to entry.txt.
Pure Python stdlib, fully deterministic: same line every run.
"""

import hashlib
import os
import pathlib


def compose_verdict() -> str:
    """Return the therapist's one-line diagnosis."""
    finding = (
        "Clinical finding: you apologize to your smart speaker, "
        "fight your GPS in traffic, and call that emotional regulation."
    )
    return finding


def main() -> None:
    verdict = compose_verdict()
    assert "\n" not in verdict, "diagnosis must be a single line"
    assert 1 <= len(verdict) <= 200, f"line is {len(verdict)} chars, must be 1-200"

    out_root = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_root.mkdir(parents=True, exist_ok=True)
    target = out_root / "entry.txt"
    target.write_text(verdict + "\n", encoding="utf-8")

    digest = hashlib.sha256(target.read_bytes()).hexdigest()
    print(verdict)
    print(f"chars: {len(verdict)}")
    print(f"sha256: {digest}")


if __name__ == "__main__":
    main()
