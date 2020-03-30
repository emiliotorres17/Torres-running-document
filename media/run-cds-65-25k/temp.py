#!/usr/bin/env python3

import os
import sys
from subprocess import call


names   = ["Pi-enst-449", "ke-2-2449", "ke-2449", "ke-average2449"]

for name in names:
    call(["pdftoppm", name + ".pdf", name, "-png"])
    call(["mv", name + "-1.png", name + ".png"])
