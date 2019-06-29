.. image:: https://img.shields.io/badge/Python-3-green.svg
    :target: https://github.com/daq-tools/vasuki

.. image:: https://img.shields.io/pypi/v/vasuki.svg
    :target: https://pypi.org/project/vasuki/

.. image:: https://img.shields.io/github/tag/daq-tools/vasuki.svg
    :target: https://github.com/daq-tools/vasuki

|

.. vasuki-readme:

######
Vasuki
######


*****
About
*****
Vasuki generates different kinds of random unique identifiers, tokens and words.

It aims to make identifier generation effortless.

There might still be dragons.


*******
Install
*******
::

    pip install vasuki

With service API::

    pip install vasuki[service]


********
Features
********

Unique ID generators
====================
- UUIDv4_ universally unique identifier
- ULID_ universally unique lexicographically sortable identifier
- Nagamani19, a short, unique, non-sequential identifier based on Hashids_
  and a custom Epoch starting on January 1, 2019.
- Gibberish_ random, pronounceable pseudo-words

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

    # Nagamani19 short, unique, non-sequential identifier.
    vasuki naga19

    # Gibberish random, pronounceable pseudo-words
    vasuki gibberish

    # Nibble short names from integer slugs
    vasuki nibble


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
    01DEFKXYCJ0E91DQY0YPWZY01D

    # Nagamani19
    vasuki naga19
    Xm3k6mWq

    # Gibberish
    vasuki gibberish
    shoomly

    # Nibble name
    vasuki nibble
    Zese


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

    vasuki gibberish --wordlength medium
    schreblyiopp


Slug tools
==========
::

    vasuki slug 42 --format=sixnibble
    Baca


*******
Credits
*******
- Andrew Hawker for https://github.com/ahawker/ulid
- David Aurelio for https://github.com/davidaurelio/hashids-python
- Gregory Haskins for https://github.com/greghaskins/gibberish
- Oliver Robson for https://github.com/HowManyOliversAreThere/six-nibble-name
- All authors for all other fine pieces this software is made of.
- Mozilla for `Zilla Slab`_

.. _Zilla Slab: https://blog.mozilla.org/opendesign/zilla-slab-common-language-shared-font/


*********
Etymology
*********

Kurma_ is one of the avatars of Vishnu_. He appears in the form of a tortoise
or turtle to support the foundation of the cosmos, while the gods and demons
churn the cosmic ocean with the help of serpent Vasuki_ to produce the nectar
of immortality.

Vasuki is a serpent king, occasionally coiling around Kurma's or Shiva's
neck, who blessed and wore him as an ornament. He is described as having
a gem called Nagamani on his head.

.. _Kurma: https://en.wikipedia.org/wiki/Kurma
.. _Vishnu: https://en.wikipedia.org/wiki/Vishnu
.. _Vasuki: https://en.wikipedia.org/wiki/Vasuki
