#!/usr/bin/env python3
"""Print alphabet without e and q."""

print("{}".format("".join(
    chr(i) for i in range(97, 123)
    if chr(i) not in "eq"
)), end="")
