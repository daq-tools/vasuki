from vasuki import generate_nagamani19_hash, generate_nagamani19_int


def test_naga19_hash():
    outcome = generate_nagamani19_hash(size="large")
    assert len(outcome) >= 10

    outcome = generate_nagamani19_hash(size="medium")
    assert len(outcome) >= 8

    outcome = generate_nagamani19_hash(size="small")
    assert len(outcome) >= 6


def test_naga19_int():
    outcome = generate_nagamani19_int(size="large")
    assert outcome > 10 ** 13

    outcome = generate_nagamani19_int(size="medium")
    assert outcome > 10 ** 11

    outcome = generate_nagamani19_int(size="small")
    assert outcome > 10 ** 8
