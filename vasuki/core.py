# -*- coding: utf-8 -*-
# (c) 2019 Andreas Motl <andreas@terkin.org>
# Apache License, Version 2
from munch import munchify

from vasuki import generate_uuid4, generate_ulid, generate_nagamani19, generate_gibberish, integer_slug, generate_momentname


class VasukiCommand:

    def __init__(self, options):
        self.options = options
    
    def run(self):

        # Unique identifier generators
        if self.options.uuid:
            assert self.options.wordlength is None, 'Option "wordlength" makes no sense for UUID'
            result = generate_uuid4()

        elif self.options.ulid:
            assert self.options.wordlength is None, 'Option "wordlength" makes no sense for ULID'
            result = generate_ulid()

        elif self.options.naga19:
            assert self.options.wordlength is None, 'Option "wordlength" makes no sense for Nagamani19'
            result = generate_nagamani19()

        elif self.options.gibberish:
            result = generate_gibberish(self.options.wordlength)

        elif self.options.moment:
            assert self.options.wordlength is None, 'Option "wordlength" not implemented for MomentName'
            result = generate_momentname()

        # Slugifiers
        elif self.options.slug:
            if self.options.format == 'sixnibble':
                try:
                    intvalue = int(self.options.value)
                except ValueError:
                    raise ValueError(f'sixnibble formatter only accepts integer values but got value={self.options.value}')

                result = integer_slug(intvalue)
            else:
                raise KeyError(f'Slug format "{self.options.format}" not implemented')

        else:
            raise KeyError('Identifier type not implemented')

        # Transform identifier.
        if self.options.lower:
            result = result.lower()
        if self.options.upper:
            result = result.upper()

        return result
