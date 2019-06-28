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
Id generator of all trades aiming to make id generation effortless.
There might still be dragons.


********
Features
********

Generators:

- UUIDv4_ universally unique identifier
- ULID_ universally unique lexicographically sortable identifier
Time and randomness is usually taking from the system
as implemented by the underlying utility libraries.

.. _UUIDv4: https://en.wikipedia.org/wiki/Universally_unique_identifier
.. _ULID: https://github.com/ulid/spec


********
Synopsis
********
::

    # Generate UUIDv4 universally unique identifier.
    vasuki uuid

    # Generate ULID universally unique lexicographically sortable identifier.
    vasuki ulid

********
Examples
********
::

    # UUIDv4
    vasuki uuid
    d192b464-d32c-48f1-9c23-0fe04a4e8133

    # ULID
    01DEFKXYCJ0E91DQY0YPWZY01D


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
