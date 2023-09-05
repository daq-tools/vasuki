"""Vasuki generates different kinds of random unique identifiers, tokens and words"""
__appname__ = 'vasuki'
__version__ = '0.3.4'

from vasuki.unique.uuid import generate_uuid4
from vasuki.unique.ulid import generate_ulid
from vasuki.unique.naga19 import generate_nagamani19
from vasuki.unique.gibberish import generate_gibberish
from vasuki.unique.moment import generate_momentname
from vasuki.format.sixnibblename.sixnibblename import integer_slug
