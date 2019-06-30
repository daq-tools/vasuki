# -*- coding: utf-8 -*-
# (c) 2019 Andreas Motl <andreas@terkin.org>
# License: GNU Affero General Public License, Version 3
import time

from vasuki.format.sixnibblename.sixnibblename import integer_slug


def generate_momentname():
    try:
        time_ns = time.time_ns()
    except:
        time_ns = time.time() * 1000 * 1000
    return integer_slug(time_ns)
