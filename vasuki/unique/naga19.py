# -*- coding: utf-8 -*-
# (c) 2019 Andreas Motl <andreas@terkin.org>
# License: GNU Affero General Public License, Version 3
"""
Nagamani19, a short, unique, non-sequential identifier based on Hashids.
"""
import os
from binascii import hexlify
from vasuki.unique.nagamani import nagamani_id


size_map = {'small': 's', 'medium': 'ms', 'large': 'ns'}

salt = None


def generate_nagamani19(size=None):
    # https://community.hiveeyes.org/t/gestaltung-der-anonymen-identifizierer-ids-fur-die-adressierung-von-imkern-messknoten-und-anderen-entitaten/1079/8
    global salt
    if salt is None:
        salt = gensalt()
    precision = get_precision(size)
    return nagamani_id(2019, salt, precision)


def get_precision(selector):
    selector = selector or 'large'
    return size_map[selector]


def gensalt():
    """
    This generates a salt from 24 random bytes from an OS-specific randomness source.
    The returned data should be unpredictable enough for cryptographic applications,
    though its exact quality depends on the OS implementation.

    https://docs.python.org/3/library/os.html#os.urandom

    Examples::

        b5f95cead701f2488d5668decb0d63a30e7ddb4c21f26574
        b4157e5459c88a6c454186492ee629ca097f8a60cbfb1a36
        de1ba437524e540e3b0d55617afcad5677b982d9e1f45f9d
    """
    return hexlify(os.urandom(24)).decode()
