# ============
# Main targets
# ============


# -------------
# Configuration
# -------------

$(eval venvpath     := .venv)
$(eval pip          := $(venvpath)/bin/pip)
$(eval python       := $(venvpath)/bin/python)
$(eval bumpversion  := $(venvpath)/bin/bumpversion)
$(eval poe          := $(venvpath)/bin/poe)

# Setup Python virtualenv
setup-virtualenv:
	@test -e $(python) || `command -v python3` -m venv $(venvpath)


# -------
# Testing
# -------

# Run the main test suite
test:
	$(poe) check

test-refresh: install-tests test


# -------
# Release
# -------

# Release this piece of software
# Synopsis:
#   make release bump=minor  (major,minor,patch)
release: setup-sandbox bumpversion push build-and-upload


# ===============
# Utility targets
# ===============
bumpversion:
	@$(bumpversion) $(bump)

push:
	git push && git push --tags

build-and-upload:
	$(poe) release

setup-sandbox: setup-virtualenv
	@$(pip) install --quiet --editable --upgrade '.[develop,docs,test]'
