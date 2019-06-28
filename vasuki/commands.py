# -*- coding: utf-8 -*-
# (c) 2019 Andreas Motl <andreas@terkin.org>
# Apache License, Version 2
import json
import logging
from docopt import docopt, DocoptExit

from vasuki import __appname__, __version__, generate_uuid4, generate_ulid, generate_naga19, generate_gibberish
from vasuki.util import normalize_options, setup_logging

log = logging.getLogger(__name__)


def run():
    """
    Vasuki generates different kinds of unique identifiers, tokens and words.

    Usage:
      vasuki (uuid | ulid | naga19 | gibberish) [--wordlength=<wordlength>] [(--upper | --lower)]
      vasuki --version
      vasuki (-h | --help)

    Options:
      --wordlength=<wordlength>         Length of word (small, medium, large)
      --upper                           Transform to upper case
      --lower                           Transform to lower case
      --version                         Show version information
      --debug                           Enable debug messages
      -h --help                         Show this screen

    Examples::

        # UUIDv4
        vasuki uuid
        d192b464-d32c-48f1-9c23-0fe04a4e8133

        # ULID
        01DEFKXYCJ0E91DQY0YPWZY01D

        # Nagamani19
        vasuki naga19
        Xm3k6mWq

        # Gibberish
        vasuki gibberish
        shoomly

    Examples with transformations::

        # UUIDv4, uppercase
        vasuki uuid --upper
        43FA0272-CA48-40AE-8CC1-204302D91D89

        # ULID, lowercase
        vasuki ulid --lower
        01defkz01k47dqkvcyhy0mz06e

    Examples with variable word length::

        vasuki gibberish --wordlength medium
        schreblyiopp

    """

    # Parse command line arguments
    options = normalize_options(docopt(run.__doc__, version=__appname__ + ' ' + __version__))

    # Setup logging
    debug = options.get('debug')
    log_level = logging.INFO
    if debug:
        log_level = logging.DEBUG
    setup_logging(log_level)

    # Debugging
    log.debug('Options: {}'.format(json.dumps(options, indent=4)))

    if options.uuid:
        assert options.wordlength is None, 'Option "wordlength" makes no sense for UUID'
        result = generate_uuid4()

    elif options.ulid:
        assert options.wordlength is None, 'Option "wordlength" makes no sense for ULID'
        result = generate_ulid()

    elif options.naga19:
        assert options.wordlength is None, 'Option "wordlength" makes no sense for Nagamani19'
        result = generate_naga19()

    elif options.gibberish:
        result = generate_gibberish(options.wordlength)

    else:
        raise DocoptExit('Unknown identifier type')

    # Transform identifier.
    if options.lower:
        result = result.lower()
    if options.upper:
        result = result.upper()

    # Output identifier to STDOUT.
    print(result)
