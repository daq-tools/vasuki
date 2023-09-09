# -*- coding: utf-8 -*-
# (c) 2019 Andreas Motl <andreas@terkin.org>
import os
from binascii import hexlify
from datetime import datetime
from hashids import Hashids
"""
Nagamani - short, unique, non-sequential identifiers based on Hashids.
"""


class Nagamani:
    """
    https://community.hiveeyes.org/t/gestaltung-der-anonymen-identifizierer-ids-fur-die-adressierung-von-imkern-messknoten-und-anderen-entitaten/1079/8
    """

    precisions = {
        's': 1,
        'ms': 1000,
        'ns': 1000000,
    }

    def __init__(self, year: int, salt=None, precision: str = "ns"):
        self.year: str = year
        self.salt: str = salt or gensalt()
        self.precision: str = precision

    def hash(self) -> str:
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
        return hashify(self.salt, self.duration())

    def duration(self) -> int:
        """
        Return current timestamp in milliseconds with a
        custom epoch which starts on Jan 1, 2019.
        """

        assert type(self.year) is int, 'Year must be integer'
        assert self.salt is not None, 'Salt must be given'
        assert self.precision is not None, 'Precision must be one of s, ms, ns'

        scaling = self.precisions.get(self.precision)

        duration = datetime.utcnow() - datetime(self.year, 1, 1)
        duration_scaled = int(duration.total_seconds() * scaling)
        return duration_scaled


def hashify(salt, *data) -> str:
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
