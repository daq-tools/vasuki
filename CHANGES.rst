*********
Changelog
*********


in progress
===========
- Dependencies: Updated to ``responder 3.0.0``
- Dependencies: Updated to ``docopt-ng``
- Verified support for Python 3.13

2024-05-10 0.7.1
================
- Verify support for Python 3.8 and 3.12
- Fix dependency reference to ``responder``

2023-09-09 0.7.0
================
- Fix and adjust Naga19 implementation.
  Use "medium" size as default, which is millisecond granularity.

2023-09-09 0.6.0
================
- Improve service subsystem and add software tests
- Limit support to Python 3.8, 3.9, and 3.10
  The ``responder`` library currently does not install on Python 3.11.

2023-09-09 0.5.0
================
- Add software tests and CI configuration
- Change license to MIT
- Update dependencies ulid-py, hashids, and gibberish

2023-09-06 0.4.0
================
- Nagamani: Refactoring
- Nagamani: Add ``generate_nagamani19_int``

2023-09-06 0.3.4
================
- Update dependencies: Munch

2022-01-01 0.3.3
================
- Add compatibility with recent versions of Python

2019-07-04 0.3.2
================
- Start using ``gibberish==0.4.0`` from PyPI.
  Thanks, @greghaskins, @adamchainz and @ddalex.
  https://github.com/greghaskins/gibberish/issues/8
- Improve documentation

2019-06-30 0.3.1
================
- Fix MomentName generator on Python3.6 again
- Improve logging

2019-06-30 0.3.0
================
- Add Icinga2 service config object
- Check service status after starting it
- Fix MomentName generator on Python3.6

2019-06-30 0.2.0
================
- Improve documentation
- Add size parameter for naga19 in web ui
- Fix linking with parameters in web ui
- Fix footer links in web ui

2019-06-30 0.1.0
================
- Basic implementation
- Add UUIDv4 identifiers
- Add ULID identifiers
- Add ``--upper`` and ``--lower`` options for output transformation
- Add Nagamani19 identifiers
- Add Gibberish words
- Add six-nibble-name integer slug
- Add MomentName short epoch slug (4-character nibbleword generator)
- Add release tooling
- Expose generators via HTTP API
- Improve performance of gibberish generator
- Wording: Use ``MomentName`` for generator
- Wording: Rename ``--wordlength`` to ``--size``
- Swap display order of generators
- Generate multiple tokens at once
- Make Nagamani19 generator obtain size, mapping it to precision
- Adjust Gibberish generator re. size parameter
- Improve main HTML UI with metadata
- Fix sdist package
