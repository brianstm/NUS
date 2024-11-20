from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO world") == 0


def test_starts_with_h():
    assert value("hi there") == 20
    assert value("Hey") == 20
    assert value("howdy") == 20


def test_other():
    assert value("Good morning") == 100
    assert value("What's up") == 100
    assert value("Greetings") == 100


def test_edge_cases():
    assert value("h") == 20
    assert value("hellohello") == 0
