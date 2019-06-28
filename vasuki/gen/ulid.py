# -*- coding: utf-8 -*-
# (c) 2019 Andreas Motl <andreas@terkin.org>
# Apache License, Version 2
import ulid


def generate_ulid():
    """
    - https://github.com/ulid/spec
    - https://pypi.org/project/ulid-py/
    """
    return str(ulid.new())
