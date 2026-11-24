"""The Funniest Out-of-Office — make.fun entry.

Writes one line of out-of-office auto-reply to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt). The file is what the judge reads --
printing alone is not enough. Single line, 140 characters or fewer,
no image, no link, no second line.
"""

import os

LINE = "I'm out of office until Tuesday. I left my inbox in charge \u2014 it has already promoted three spam emails and fired my calendar."

# The gate requires 1-140 characters, one line, not only whitespace.
# Fail loudly here rather than ship an invalid entry.
assert 1 <= len(LINE) <= 140, f"entry is {len(LINE)} chars, must be 1-140"
assert "\n" not in LINE, "entry must be a single line"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)

print(LINE)
