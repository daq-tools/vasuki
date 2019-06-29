# -*- coding: utf-8 -*-
# (c) 2019 Andreas Motl <andreas@terkin.org>
# Apache License, Version 2
import time

from vasuki.format.sixnibblename.sixnibblename import integer_slug


def generate_momentname():
    return integer_slug(time.time_ns())
