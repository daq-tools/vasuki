# -*- coding: utf-8 -*-
# (c) 2019 Andreas Motl <andreas@terkin.org>
# Apache License, Version 2
import json
import logging
from docopt import docopt, DocoptExit

from vasuki import __appname__, __version__
from vasuki.core import VasukiCommand
from vasuki.util import normalize_options, setup_logging

log = logging.getLogger(__name__)


def run():
    """
    Vasuki generates different kinds of unique identifiers, tokens and words.

    Usage:
      vasuki (uuid | ulid | naga19 | gibberish | moment) [--wordlength=<wordlength>] [(--upper | --lower)]
      vasuki slug <value> --format=<format>
      vasuki service [--listen=<listen>]
      vasuki --version
      vasuki (-h | --help)

    Options:
      --wordlength=<wordlength>         Length of word (small, medium, large)
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
        01DEFKXYCJ0E91DQY0YPWZY01D

        # Nagamani19
        vasuki naga19
        Xm3k6mWq

        # Gibberish
        vasuki gibberish
        shoomly

        # MomentName
        vasuki moment
        Zese

    Examples with transformations::

        # UUIDv4, uppercase
        vasuki uuid --upper
        43FA0272-CA48-40AE-8CC1-204302D91D89

        # ULID, lowercase
        vasuki ulid --lower
        01defkz01k47dqkvcyhy0mz06e

    Example with variable word length::

        vasuki gibberish --wordlength medium
        schreblyiopp

    Slug tools::

        vasuki slug 42 --format=sixnibble
        Baca

    Start API service::

        vasuki service

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

    if options.service:
        listen_address = options.listen
        log.info(f'Starting web service on {listen_address}')
        from vasuki.api import start_service
        start_service(listen_address)
        return

    # Run command.
    try:
        workload = VasukiCommand(options)
        result = workload.run()
    except Exception as ex:
        message = str(ex)
        log.error(message)
        raise DocoptExit(message)

    # Output identifier to STDOUT.
    print(result)
