"""The Funniest Toaster Error Message.

Writes one funny toaster error line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt): the message a kitchen toaster shows its
owner when something goes wrong. The E07 code prefix makes it read
like a real appliance error, and the line stays deadpan, fresh and
tight: the bread has formed a union, so the toaster is legally
forbidden from toasting it.
"""

import os

LINE = "E07: The bread has unionized. I am legally forbidden from toasting it."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
