#!/usr/bin/env python3

import os
import sys
from subprocess import call


names   = ["Pi-enst-4750", "ke-2-4750", "ke-4750", "ke-average4750", "A-enst-4750", "A-ke-4750",\
                "C-ke-4750", "Pi-enst-4750", "P-ke-4750", "P-enst-4750", "enst-4750", "ke-4750",\
                "ke-2-4750", "enst-2-4750", "D-enst-4750", "D-ke-4750", "enst-average4750",\
                "B-enst-4750", "B-ke-4750"]

for name in names:
    print(name)
    call(["pdftoppm", name + ".pdf", name, "-png"])
    call(["mv", name + "-1.png", name + ".png"])
