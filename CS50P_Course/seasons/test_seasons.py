from seasons import convert
from datetime import date
import pytest


def test_convert():
    assert convert("2022-01-22", today_date=date(2023, 1, 22)
                   ) == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert("2021-01-22", today_date=date(2023, 1, 22)
                   ) == "One million, fifty-one thousand, two hundred minutes"
    assert convert("2020-01-22", today_date=date(2023, 1, 22)
                   ) == "One million, five hundred seventy-eight thousand, two hundred forty minutes"
    assert convert("1997-06-24", today_date=date(2023, 1, 22)
                   ) == "Thirteen million, four hundred fifty-three thousand, nine hundred twenty minutes"


def test_exit():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        convert("January 1, 1999")
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == "Not a valid format."

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        convert("1997 June 24")
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == "Not a valid format."
