import shlex
import sys
import uuid

import docopt
import pytest
import ulid

from vasuki.cli import run


def set_cmd_args(command, more_options=""):
    command = f'vasuki {command} {more_options}'
    sys.argv = shlex.split(command)


def test_cli_failure():
    # Run erroneous command.
    set_cmd_args("foo")
    with pytest.raises(docopt.DocoptExit) as ex:
        run()

    # Verify output.
    assert ex.match("Usage:\n      vasuki")


def test_uuid(capsys):
    # Run command and capture output.
    set_cmd_args("uuid")
    run()
    out, err = capsys.readouterr()

    # Verify output.
    raw = out.strip()
    decoded = uuid.UUID(raw).hex
    assert int(decoded, 16) > 10 ** 5


def test_ulid(capsys):
    # Run command and capture output.
    set_cmd_args("ulid")
    run()
    out, err = capsys.readouterr()

    # Verify output.
    raw = out.strip()
    decoded = ulid.parse(raw)
    assert decoded.timestamp() > 10 ** 5


def test_gibberish(capsys):
    # Run command and capture output.
    set_cmd_args("gibberish")
    run()
    out, err = capsys.readouterr()

    # Verify output.
    raw = out.strip()
    assert len(raw) >= 5


def test_moment(capsys):
    # Run command and capture output.
    set_cmd_args("moment")
    run()
    out, err = capsys.readouterr()

    # Verify output.
    raw = out.strip()
    assert len(raw) >= 4


def test_naga19(capsys):
    # Run command and capture output.
    set_cmd_args("naga19")
    run()
    out, err = capsys.readouterr()

    # Verify output.
    raw = out.strip()
    assert len(raw) >= 10


def test_slug_sixnibble(capsys):
    # Run command and capture output.
    set_cmd_args("slug 42 --format=sixnibble")
    run()
    out, err = capsys.readouterr()

    # Verify output.
    raw = out.strip()
    assert raw == "Baca"
