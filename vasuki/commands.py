# -*- coding: utf-8 -*-
# (c) 2019 Andreas Motl <andreas@terkin.org>
# Apache License, Version 2
import json
import logging
from docopt import docopt

from vasuki import __appname__, __version__, uuid4
from vasuki.util import normalize_options, setup_logging

log = logging.getLogger(__name__)


def run():
    """
    Usage:
      vasuki uuid
      vasuki --version
      vasuki (-h | --help)

      --version                         Show version information
      --debug                           Enable debug messages
      -h --help                         Show this screen

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
        print(uuid4())
