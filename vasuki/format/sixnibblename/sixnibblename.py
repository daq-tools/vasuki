# -*- coding: utf-8 -*-
# (c) 2018-2019 Oliver Robson <http://oliver-robson.tech/>, MIT License
# https://github.com/HowManyOliversAreThere/six-nibble-name
C = 'bcdfghjklmnpqrstvwxyz'
V = 'aeiou'


def integer_slug(uid):
    assert type(uid) is int, f'integer_slug only accepts integer types but got value={uid}, type={type(uid)}'
    sb = uid
    n = ''
    n += C[((sb & 0xFE0000) >> 17) % len(C)].upper()
    n += V[((sb & 0x1F000) >> 12) % len(V)]
    n += C[((sb & 0xFE0) >> 5) % len(C)]
    n += V[(sb & 0x1F) % len(V)]
    return n
