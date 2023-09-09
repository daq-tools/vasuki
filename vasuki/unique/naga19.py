# -*- coding: utf-8 -*-
# (c) 2019 Andreas Motl <andreas@terkin.org>
"""
Nagamani19, a short, unique, non-sequential identifier based on Hashids.
"""
import warnings

from vasuki.unique.nagamani import Nagamani

size_map = {'small': 's', 'medium': 'ms', 'large': 'ns'}

salt = None


def generate_nagamani19_obj(size=None) -> Nagamani:
    return Nagamani(year=2019, precision=get_precision(size))


def generate_nagamani19(size=None) -> str:
    warnings.warn(DeprecationWarning("The function `generate_nagamani19` is deprecated. Please use `generate_nagamani19_hash` instead."))
    return generate_nagamani19_obj(size=size).hash()


def generate_nagamani19_hash(size=None) -> str:
    return generate_nagamani19_obj(size=size).hash()


def generate_nagamani19_int(size=None) -> int:
    return generate_nagamani19_obj(size=size).duration()


def get_precision(selector):
    selector = selector or 'medium'
    return size_map[selector]
