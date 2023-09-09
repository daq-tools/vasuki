# -*- coding: utf-8 -*-
# (c) 2019 Andreas Motl <andreas@terkin.org>
import logging
from vasuki import generate_uuid4, generate_ulid, generate_nagamani19_hash, generate_gibberish, integer_slug, generate_momentname

log = logging.getLogger(__name__)


class VasukiCommand:

    def __init__(self, options):
        self.options = options

    def run_multi(self):
        results = []
        count = int(self.options.get('count', 1))
        for i in range(count):
            try:
                result = self.run_single()
                #log.info(f'Vasuki result: {result}')
                results.append(result)
            except Exception as ex:
                message = str(ex)
                log.exception(message)
                raise
        return results

    def run_single(self):

        # Unique identifier generators
        if self.options.uuid:
            assert self.options.size is None, 'Option "size" makes no sense for UUID'
            result = generate_uuid4()

        elif self.options.ulid:
            assert self.options.size is None, 'Option "size" makes no sense for ULID'
            result = generate_ulid()

        elif self.options.naga19:
            result = generate_nagamani19_hash(size=self.options.size)

        elif self.options.gibberish:
            result = generate_gibberish(size=self.options.size)

        elif self.options.moment:
            assert self.options.size is None, 'Option "size" not implemented for MomentName'
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
