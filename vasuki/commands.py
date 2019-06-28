# -*- coding: utf-8 -*-
# (c) 2019 Andreas Motl <andreas@terkin.org>
# Apache License, Version 2
import json
import logging
from docopt import docopt, DocoptExit

from vasuki import __appname__, __version__, generate_uuid4, generate_ulid
from vasuki.util import normalize_options, setup_logging

log = logging.getLogger(__name__)


def run():
    """
    Usage:
      vasuki uuid|ulid
      vasuki --version
      vasuki (-h | --help)

      --version                         Show version information
      --debug                           Enable debug messages
      -h --help                         Show this screen

    Examples::

        # UUIDv4
        vasuki uuid
        d192b464-d32c-48f1-9c23-0fe04a4e8133

        # ULID
        01DEFKXYCJ0E91DQY0YPWZY01D

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
        print(generate_uuid4())

    elif options.ulid:
        print(generate_ulid())
