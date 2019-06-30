#######
Backlog
#######

Tasks
=====

Prio 1
------
- [o] Trim down example on ``vasuki --help`` and refer to GitHub page

Prio 2
------
- [o] Implement ``--size`` for ``MomentName``
- [o] Clamp maximum number of tokens generated at once
- [o] Add rate limiting
- [o] UI: Buttons

Generators
==========
- [o] Add slugify-title routine
- [o] Add original shortid generator
  https://github.com/teris-io/shortid
- [o] Add https://pypi.org/project/StringGenerator/
- [o] Add ``apg``-like password generators
    - https://github.com/weirdestnerd/password-generator
    - https://pypi.org/project/correct-horse/
    - https://pypi.org/project/memorable_password/
    - https://github.com/patarapolw/randomsentence
- [o] ClassNamer

Research
========
- https://community.hiveeyes.org/t/alternatives-to-uuids-as-network-identifiers/1060
- https://community.hiveeyes.org/t/gestaltung-der-anonymen-identifizierer-ids-fur-die-adressierung-von-imkern-messknoten-und-anderen-entitaten/1079/9

Done
====
- [x] Add UUIDv4
- [x] Add ULID
- [x] Add Nagamani19
- [x] Add Gibberish
- [x] Add six-nibble-name
- [x] Add responder
  https://python-responder.org/
- [x] Route more parameters from the HTTP API to the core
- [x] Add some style
- [x] Add systemd unit file
- [x] Rename nibble to MomentName / moment
- [x] Rename wordlength to wordsize
- [x] Generate more tokens at once
- [x] UI: Embed, DOCTYPE, encoding
- [x] Size parameter for naga19 in web ui
- [x] ``AttributeError: module 'time' has no attribute 'time_ns'``
  https://api.hiveeyes.org/vasuki/unique/moment
