"""Vasuki generates different kinds of random unique identifiers, tokens and words"""
__appname__ = 'vasuki'
__version__ = '0.0.0'

from vasuki.unique.uuid import generate_uuid4
from vasuki.unique.ulid import generate_ulid
from vasuki.unique.naga import generate_naga19
from vasuki.unique.gibberish import generate_gibberish
from vasuki.unique.nibbleword import generate_nibbleword
from vasuki.format.sixnibblename.sixnibblename import integer_slug
