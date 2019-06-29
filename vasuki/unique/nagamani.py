# -*- coding: utf-8 -*-
# (c) 2019 Andreas Motl <andreas@terkin.org>
# License: GNU Affero General Public License, Version 3
from datetime import datetime
from hashids import Hashids
"""
Nagamani - short, unique, non-sequential identifiers based on Hashids.
"""

precisions = {
    's': 1,
    'ms': 1000,
    'ns': 1000000,
}


def nagamani_id(year, salt, precision):
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

    assert type(year) is int, 'Year must be integer'
    assert salt is not None, 'Salt must be given'
    assert precision is not None, 'Precision must be one of s, ms, ns'

    scaling = precisions.get(precision)

    duration = datetime.utcnow() - datetime(year, 1, 1)
    duration_scaled = int(duration.total_seconds() * scaling)
    return hashify(salt, duration_scaled)


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
