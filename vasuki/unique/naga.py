# -*- coding: utf-8 -*-
# (c) 2019 Andreas Motl <andreas@terkin.org>
# Apache License, Version 2
import os
from datetime import datetime
from binascii import hexlify
from hashids import Hashids
"""
Nagamani19, a short, unique, non-sequential identifier based on Hashids.
"""

salt = None


def generate_naga19():
    # https://community.hiveeyes.org/t/gestaltung-der-anonymen-identifizierer-ids-fur-die-adressierung-von-imkern-messknoten-und-anderen-entitaten/1079/8
    global salt
    if salt is None:
        salt = gensalt()
    return naga_id(2019, salt)


def naga_id(year, salt):
    """
    Generate unique ids based on Hashids.

    Hashids are short, unique, non-sequential ids generated from numbers
    and suitable to be used as unguessable and unpredictable short UIDs.

    Here, we are generating Hashids of the current timestamp in milliseconds.
    To keep the footprint low, a custom epoch is used which starts on Jan 1, 2019.

    Examples::

        1Zk5zBoQ
        Y4Mvj5Zx
        2b4NBvYe
        XaMvl962
        yzgOlvap

    """
    now = int(round((datetime.utcnow() - datetime(year, 1, 1)).total_seconds() * 1000))
    return hashify(salt, now)


def hashify(salt, *data):
    """
    Hashids are short, unique, non-sequential ids generated from numbers
    and suitable to be used as short UIDs.

    If you want to decode the Hashids later, you should keep your salt stable.

    Remark: Hashids are not limited to encode a single number, you can actually
    pack a list of numbers into a single Hashid.

    - https://hashids.org/
    - https://hashids.org/python/
    - https://github.com/davidaurelio/hashids-python
    """
    hashids = Hashids(salt=salt)
    return hashids.encode(*data)


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
