.. image:: https://github.com/daq-tools/vasuki/actions/workflows/main.yml/badge.svg
    :alt: Software test outcome
    :target: https://github.com/daq-tools/vasuki/actions/workflows/main.yml

.. image:: https://img.shields.io/codecov/c/gh/daq-tools/vasuki.svg
    :alt: Software tests code coverage
    :target: https://codecov.io/gh/daq-tools/vasuki/

.. image:: https://img.shields.io/pypi/pyversions/vasuki.svg
    :alt: Supported versions of Python
    :target: https://pypi.org/project/vasuki/

.. image:: https://img.shields.io/pypi/status/vasuki.svg
    :alt: PyPI Status
    :target: https://pypi.org/project/vasuki/

.. image:: https://img.shields.io/pypi/v/vasuki.svg
    :alt: Version on PyPI
    :target: https://pypi.org/project/vasuki/

.. image:: https://pepy.tech/badge/vasuki/month
    :target: https://pypi.org/project/vasuki/

.. image:: https://img.shields.io/pypi/l/vasuki.svg
    :alt: License
    :target: https://github.com/daq-tools/vasuki/blob/main/LICENSE

|

.. figure:: https://ptrace.hiveeyes.org/2019-06-29_vasuki-small.jpg
    :target: https://en.wikipedia.org/wiki/Vasuki#/media/File:Kurma,_the_tortoise_incarnation_of_Vishnu.jpg


.. vasuki-readme:

######
Vasuki
######


*****
About
*****

Vasuki generates different kinds of random unique identifiers, tokens, and words.
It can be used as a library and as an HTTP service, aiming to provide effortless
identifier generation for your applications.


*******
Install
*******

Prerequisites
=============
::

    pip install vasuki

With service API::

    pip install 'vasuki[service]'


********
Features
********

Unique ID generators
====================
- UUIDv4_ universally unique identifier
- ULID_ universally unique lexicographically sortable identifier
- Gibberish_ random, pronounceable pseudo-words
- MomentName, a short epoch slug
- Nagamani19, a short, unique, non-sequential identifier based on Hashids_
  and a custom Epoch starting on January 1, 2019.

Time and randomness is usually taking from the system
as implemented by the libraries underpinning this package.

Slugifiers
==========
- `six-nibble-name`_ converts six nibbles (three bytes) into a 4-character name

Optional service API
====================
The fine responder_ optionally exposes the machinery as HTTP API.

.. _UUIDv4: https://en.wikipedia.org/wiki/Universally_unique_identifier
.. _ULID: https://github.com/ulid/spec
.. _Hashids: https://hashids.org/
.. _Gibberish: https://github.com/greghaskins/gibberish
.. _six-nibble-name: https://github.com/HowManyOliversAreThere/six-nibble-name
.. _responder: https://pypi.org/project/responder/


********
Synopsis
********
::

    # UUIDv4 universally unique identifier.
    vasuki uuid

    # ULID universally unique lexicographically sortable identifier.
    vasuki ulid

    # Gibberish random, pronounceable pseudo-words
    vasuki gibberish

    # MomentName short epoch slugs
    vasuki moment

    # Nagamani19 short, unique, non-sequential identifier.
    vasuki naga19


********
Examples
********

Identifier generation
=====================
::

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


With transformations
====================
Vasuki can apply uppercase or lowercase transformation to the
generated identifier or word::

    # UUIDv4, uppercase
    vasuki uuid --upper
    43FA0272-CA48-40AE-8CC1-204302D91D89

    # ULID, lowercase
    vasuki ulid --lower
    01defkz01k47dqkvcyhy0mz06e

With variable word length
=========================
::

    vasuki gibberish --size medium
    schreblyiopp


Slug tools
==========
::

    vasuki slug 42 --format=sixnibble
    Baca

Multiple tokens at once
=======================
::

    vasuki naga19 --count 10
    vasuki gibberish --size large --count 50


HTTP API
========
Start the Vasuki service as daemon::

    vasuki service

Example requests would look like::

    # UUIDv4
    /unique/uuid

    # Uppercase UUIDv4
    /unique/uuid?upper=true

    # Multiple ULIDs
    /unique/ulid?count=10

    # Very short Nagamani19
    /unique/naga19?size=small


***********
Development
***********

Acquire sources::

    git clone https://github.com/daq-tools/vasuki
    cd vasuki

Install development sandbox::

    python3 -m venv .venv
    source .venv/bin/activate
    pip install --editable=.[develop,docs,test]
    vasuki --version

Run linter and software tests::

    poe check


**********
Disclaimer
**********

The algorithms and procedures curated here generate different kinds of random and
pseudo-random identifiers, tokens, names or passwords.

While some of the generated tokens max out on the randomness and uniqueness
aspects like UUIDs, others compromise on the time vs. space domain but focus
more on human memorability and empathize with their common sense and humor.

Saying that, you should know what about their properties and features when using
those identifiers in different contexts. YMMV.


*******
Credits
*******
- Andrew Hawker for https://github.com/ahawker/ulid
- David Aurelio for https://github.com/davidaurelio/hashids-python
- Gregory Haskins for https://github.com/greghaskins/gibberish
- Oliver Robson for https://github.com/HowManyOliversAreThere/six-nibble-name
- All authors for all other fine pieces this software is made of.
- Mozilla for `Zilla Slab`_
- Vasuki Logo from https://en.wikipedia.org/wiki/Vasuki

.. _Zilla Slab: https://blog.mozilla.org/opendesign/zilla-slab-common-language-shared-font/


*********
Etymology
*********

Kurma_ is one of the avatars of Vishnu_. He appears in the form of a tortoise
or turtle to support the foundation of the cosmos, while the gods and demons
churn the cosmic ocean with the help of serpent Vasuki_ to produce the nectar
of immortality.

Vasuki is a naga serpent king, occasionally coiling around Kurma's or Shiva's
neck, who blessed and wore him as an ornament. He is described as having
a gem called Nagamani on his head.

.. _Kurma: https://en.wikipedia.org/wiki/Kurma
.. _Vishnu: https://en.wikipedia.org/wiki/Vishnu
.. _Vasuki: https://en.wikipedia.org/wiki/Vasuki
