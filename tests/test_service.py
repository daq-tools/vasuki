import uuid


def test_index(api):
    r = api.requests.get("/")
    assert "<!DOCTYPE html>" in r.text
    assert "Vasuki - random unique identifiers, tokens, and words" in r.text


def test_uuid(api):
    r = api.requests.get("/unique/uuid")

    raw = r.text
    decoded = uuid.UUID(raw).hex
    assert int(decoded, 16) > 10 ** 5
