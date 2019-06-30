# -*- coding: utf-8 -*-
# (c) 2019 Andreas Motl <andreas@terkin.org>
# License: GNU Affero General Public License, Version 3
import logging
import responder
from munch import DefaultMunch, munchify
from pkg_resources import resource_filename
from vasuki.core import VasukiCommand

templates_dir = resource_filename('vasuki', 'templates')
api = responder.API(static_dir=templates_dir, templates_dir=templates_dir)


log = logging.getLogger(__name__)


@api.route("/")
async def vasuki_index(request, response):
    index = munchify([
        {
            'key': 'uuid',
            'name': 'UUIDv4',
            'params': ['upper=true'],
            'description': 'universally unique identifier',
        },
        {
            'key': 'ulid',
            'name': 'ULID',
            'params': ['lower=true'],
            'description': 'universally unique lexicographically sortable identifier',
        },
        {
            'key': 'gibberish',
            'name': 'Gibberish',
            'params': ['size=small', 'size=medium', 'size=large'],
            'description': 'random, pronounceable pseudo-words',
        },
        {
            'key': 'moment',
            'name': 'MomentName',
            'description': 'short epoch slug',
        },
        {
            'key': 'naga19',
            'name': 'Nagamani19',
            'description': 'short, unique, non-sequential identifier',
        },
    ])

    cache_bust = False
    #cache_bust = time.time_ns()

    response.html = api.template('index.html', index=index, cache_bust=cache_bust)


@api.route("/unique/{kind}")
async def vasuki_service(request, response, *args, **kwargs):

    #debug_request(request, response)

    options = DefaultMunch(None)

    # Transform request parameters into munch of options (subcommands).
    subcommand_options = {}
    for v in kwargs.values():
        subcommand_options[v] = True
    options.update(subcommand_options)

    # Transform request parameters into munch of options (query arguments).
    options.update(request.params.items())

    # Run command, optionally multiple times.
    try:
        command = VasukiCommand(options)
        results = command.run_multi()

        # Output identifiers to HTTP response.
        response.text = '\n'.join(results)

    except Exception as ex:
        log.exception('Vasuki failed')
        response.status_code = api.status_codes.HTTP_500
        response.text = f'{ex.__class__.__name__}: {str(ex)}'


def debug_request(request, response):
    log.info(f'Request: {request}, {dir(request)}')
    log.info(f'Response: {response}, {dir(response)}')
    log.info(f'Request parameters: {request.params}')


def start_service(listen_address):
    host, port = listen_address.split(':')
    port = int(port)
    api.run(address=host, port=port)
