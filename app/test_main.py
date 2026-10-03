from app.main import get_human_age


def test_should_return_zero_when_cat_and_dog_ages_are_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zero_when_cat_and_dog_ages_are_less_than_fifteen() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_one_when_cat_and_dog_ages_are_fifteen() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_one_when_cat_and_dog_ages_are_twenty_three() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_two_when_cat_and_dog_ages_are_twenty_four() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_two_when_cat_and_dog_ages_are_twenty_seven() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_should_return_different_ages_for_cat_and_dog() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_return_correct_large_values() -> None:
    assert get_human_age(100, 100) == [21, 17]
