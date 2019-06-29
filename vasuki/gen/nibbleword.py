# -*- coding: utf-8 -*-
# (c) 2019 Andreas Motl <andreas@terkin.org>
# Apache License, Version 2
"""
``six-nibble-name`` converts six nibbles (three bytes) into a 4-character name.
https://github.com/HowManyOliversAreThere/six-nibble-name
"""
import time
from vasuki import integer_slug


def generate_nibbleword():
    return integer_slug(time.time_ns())
