from numb3rs import validate


def test_valid_ips():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("192.168.0.1") == True


def test_invalid_ips():
    assert validate("275.0.0.1") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
    assert validate("1.1.1") == False
    assert validate("1.1.1.1.1") == False

    assert validate("256.0.0.1") == False
    assert validate("0.256.0.1") == False
    assert validate("0.0.256.1") == False
    assert validate("0.0.0.256") == False
