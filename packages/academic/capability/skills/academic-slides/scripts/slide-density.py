"""Fail a deck whose slide bodies outgrow the course's word budget.

A line limit alone does not hold: measured on a real deck, 53 slides out of 53
obeyed a six-line rule while averaging 41 words each, because six
sentence-length lines pass a line count and are still a wall of text. The
budget is the rule that bites, so it has to be checked by something other than
the agent that wrote the deck.

Reads course.yaml with a regex rather than a YAML parser: this runs wherever
the manager executes gate commands, and a missing PyYAML must not turn a
content check into an infrastructure failure.
"""

import glob
import os
import re
import sys


def scalar(text: str, section: str, key: str, default):
    block = re.search(rf"^{section}:\s*$(.*?)(?=^\S|\Z)", text, re.S | re.M)
    if not block:
        return default
    found = re.search(rf"^\s+{key}:\s*(\S+)", block.group(1), re.M)
    return found.group(1).strip("\"'") if found else default


config = open("course.yaml").read() if os.path.exists("course.yaml") else ""
cap = int(scalar(config, "slides", "maxWordsPerSlide", 25))
root = scalar(config, "layout", "lessons", "weeks")
name = scalar(config, "artifacts", "slides", "slides.md")

failures = []
for path in sorted(glob.glob(os.path.join(root, "*", name))):
    text = re.sub(r"<!--.*?-->", "", open(path).read(), flags=re.S)
    bodies = [len(part.split()) for part in text.split("\n---\n")]
    if not bodies:
        continue
    average = sum(bodies) / len(bodies)
    over = [n + 1 for n, w in enumerate(bodies) if w > cap]
    heavy = [n + 1 for n, w in enumerate(bodies) if w > cap * 2]
    if average > cap or heavy:
        failures.append((path, len(bodies), average, over, heavy))

for path, count, average, over, heavy in failures:
    print(
        f"{path}: {count} slides, {average:.1f} words on average against a "
        f"{cap}-word budget; {len(over)} over budget"
        + (f"; more than double: slides {heavy}" if heavy else "")
    )

if failures:
    print(
        f"\nCut slide bodies to {cap} words, speaker notes excluded: one claim "
        "per slide, fragments rather than sentences. Move what does not fit "
        "into the lecture, which is where a reader can re-read it."
    )
    sys.exit(1)

print(f"slide density within budget ({cap} words per body)")
