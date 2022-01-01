#######
Backlog
#######


Tasks
=====

Prio 1
------
- [o] Add compatibility with recent versions of ``typesystem`` (vs. ``responder``/``apistar```
    - https://github.com/taoufik07/responder/pull/430
    - https://github.com/taoufik07/responder/issues/440
    - https://github.com/encode/apistar/pull/675

Prio 1.5
--------
- [o] Trim down example on ``vasuki --help`` but refer to
  GitHub page and/or live instance.
- [o] Add Disclaimer to index.html
- [o] Add "Why?" section to documentation
- [o] Announce on https://community.hiveeyes.org/t/gestaltung-der-anonymen-identifizierer-ids-fur-die-adressierung-von-imkern-messknoten-und-anderen-entitaten/1079
- [o] Add to https://community.hiveeyes.org/t/messdaten-an-die-hiveeyes-plattform-ubermitteln/1813

Prio 2
------
- [o] Add prefix and suffix parameters to prepend or append
  fixed strings to the generated tokens
- [o] Introduce prwords ontology
- [o] Add more generators
- [o] API documentation
- [o] Implement ``--size`` for ``MomentName``
- [o] Clamp maximum number of tokens generated at once
- [o] Add rate limiting
- [o] UI: Buttons
- [o] Research into and give credit for the underlying algorithms,
  not only the people implementing them. Turtles all the way down.
- [o] Add favicon.ico to static folder


Generators
==========

Ontology
--------
- Identifiers/Tokens, Names, Passwords, Slugs

Identifiers
-----------
- [o] Add original shortid generator
  https://github.com/teris-io/shortid
- [o] Add https://pypi.org/project/StringGenerator/
- https://community.hiveeyes.org/t/alternatives-to-uuids-as-network-identifiers/1060/2

Names
-----
- Class names
  https://www.classnamer.org/
  https://rubygems.org/gems/classnamer
- Funny Colored Animal [fca]
  https://pypi.org/project/random_name/
- Funny Person [fp1]
  https://github.com/moby/moby/blob/master/pkg/namesgenerator/names-generator.go
- Funny Person [fp2]
  e.g. Speedy_Gonzales on https://community.hiveeyes.org/t/upload-und-initiale-konfiguration-der-micropython-firmware/2206/10
- Ubuntu Distribution
  e.g. Bionic Beaver
- Toponyms
  https://en.wikipedia.org/wiki/Toponymy
  https://en.wikipedia.org/wiki/List_of_words_derived_from_toponyms
- User agents
  https://pypi.org/project/random-useragent/
- Words from Dadaism

Sentences
---------
- https://pypi.org/project/correct-horse/
- https://github.com/patarapolw/randomsentence
- Whole stories from GPT-2

Passwords
---------
- ``apg``-like password generator
- https://pypi.org/project/password-generator/
  https://github.com/weirdestnerd/password-generator
- https://pypi.org/project/memorable_password/
- https://github.com/patarapolw/randomsentence
- https://pypi.org/project/random_password/
- https://pypi.org/project/memorable_password/
- https://pypi.org/project/password_gen/
- https://pypi.org/project/simple_password_generator/
-

Slugs
-----
- [o] Add slugify-title routine



Research
========
- https://community.hiveeyes.org/t/alternatives-to-uuids-as-network-identifiers/1060
- https://community.hiveeyes.org/t/gestaltung-der-anonymen-identifizierer-ids-fur-die-adressierung-von-imkern-messknoten-und-anderen-entitaten/1079/9

Done
====
- [x] Add UUIDv4
- [x] Add ULID. https://github.com/ulid/spec
- [x] Add Nagamani19
- [x] Add Gibberish. https://github.com/greghaskins/gibberish
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
