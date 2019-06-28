"""Vasuki is an id generator of all trades"""
__appname__ = 'vasuki'
__version__ = '0.0.0'

from vasuki.gen.uuid import generate_uuid4
from vasuki.gen.ulid import generate_ulid
from vasuki.gen.naga import generate_naga19
from vasuki.gen.gibberish import generate_gibberish
