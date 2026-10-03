from app.main import get_human_age


def test_return_value_should_have_two_elements() -> None:
    assert (
        len(get_human_age(14, 14)) == 2
    ), ""


def test_should_return_one_year_for_first_fifteen() -> None:
    assert (
        get_human_age(15, 15) == [1, 1]
    ), ""


def test_should_return_two_years_for_twenty_four() -> None:
    assert (
        get_human_age(24, 24) == [2, 2]
    ), ""


def test_should_return_different_years_for_twenty_eight() -> None:
    assert (
        get_human_age(28, 28) == [3, 2]
    ), ""


def test_should_return_zero_years_for_under_fifteen() -> None:
    assert (
        get_human_age(14, 14) == [0, 0]
    ), ""
