# -*- coding: utf-8 -*-
# (c) 2019 Andreas Motl <andreas@terkin.org>
import json
import logging
from docopt import docopt, DocoptExit

from vasuki import __appname__, __version__
from vasuki.core import VasukiCommand
from vasuki.util import normalize_options, setup_logging

log = logging.getLogger(__name__)


def run():
    """
    Vasuki generates different kinds of unique identifiers, tokens, and words.

    Usage:
      vasuki (uuid | ulid | gibberish | moment | naga19) [--size=<size>] [--count=<count>] [(--upper | --lower)]
      vasuki slug <value> --format=<format>
      vasuki service [--listen=<listen>]
      vasuki --version
      vasuki (-h | --help)

    Options:
      --size=<size>                     Size of item (small, medium, large)
      --count=<count>                   Number of items. [Default: 1]
      --upper                           Transform to upper case
      --lower                           Transform to lower case
      --format=<format>                 Format for transformations for slugs, etc.
      --listen=<listen>                 HTTP server listen address. [Default: localhost:24641]
      --version                         Show version information
      --debug                           Enable debug messages
      -h --help                         Show this screen

    Examples::

        # UUIDv4
        vasuki uuid
        d192b464-d32c-48f1-9c23-0fe04a4e8133

        # ULID
        vasuki ulid
        01DEFKXYCJ0E91DQY0YPWZY01D

        # Gibberish
        vasuki gibberish
        shoomly

        # MomentName
        vasuki moment
        Zese

        # Nagamani19
        vasuki naga19
        Xm3k6mWq

    Transformations::

        # UUIDv4, uppercase
        vasuki uuid --upper
        43FA0272-CA48-40AE-8CC1-204302D91D89

        # ULID, lowercase
        vasuki ulid --lower
        01defkz01k47dqkvcyhy0mz06e

    Variable word length::

        vasuki gibberish --size medium
        schreblyiopp

    Multiple tokens at once::

        vasuki naga19 --count 10
        vasuki gibberish --size large --count 50

    Slug tools::

        vasuki slug 42 --format=sixnibble
        Baca

    Start API service::

        vasuki service

    """

    name = f'{__appname__} {__version__}'

    # Parse command line arguments
    options = normalize_options(docopt(run.__doc__, version=name))

    # Setup logging
    debug = options.get('debug')
    log_level = logging.INFO
    if debug:
        log_level = logging.DEBUG
    setup_logging(log_level)

    # Debugging
    # log.debug('Options: {}'.format(json.dumps(options, indent=4)))

    if options.service:
        listen_address = options.listen
        log.info(f'Starting {name}')
        log.info(f'Starting web service on {listen_address}')
        from vasuki.api import start_service
        start_service(listen_address)
        return

    # Run command, optionally multiple times.
    command = VasukiCommand(options)
    results = command.run_multi()

    # Output identifiers to STDOUT.
    print('\n'.join(results))
