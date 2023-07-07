import pytest

from pytest_dz.human import Human


def test_grow(create_human):
    human = create_human
    new_age = human.age + 1
    human.grow()
    assert human.age == new_age


def test_grow_reach_age_limit(create_giga_old_human):
    human = create_giga_old_human
    for _ in range(2):
        human.grow()
    with pytest.raises(Exception, match="Misha is already dead..."):
        human.grow()


# I think I found a bug here, because if I create an instance of a class with the age
# that is higher than age_limit the status does not change to "dead",
# needs to be fixed  in the initialization
def test_grow_if_already_dead(create_dead_human):
    human = create_dead_human
    with pytest.raises(Exception, match="Misha is already dead..."):
        human.grow()


def test_grow_if_age_is_negative(create_negative_human):
    human = create_negative_human
    with pytest.raises(Exception, match="Misha is already dead..."):
        human.grow()


def test_change_gender_valid(create_human):
    human = create_human
    gender = "male"
    new_gender = "female"
    human.change_gender(new_gender)
    assert human.gender == "female", "Gender didn't changed"
    human.change_gender(gender)
    assert human.gender == "male", "Gender didn't changed"


def test_change_gender_same_gender(create_human):
    human = create_human
    new_gender = "male"
    with pytest.raises(Exception, match="Misha already has gender 'male'"):
        human.change_gender(new_gender)


def test_change_gender_invalid(create_human):
    human = create_human
    new_gender = "some_new_gender"
    with pytest.raises(Exception, match="Not correct name of gender"):
        human.change_gender(new_gender)


def test_age_property():
    human = Human('Misha', 22, 'male')
    current_age = 22
    assert human.age == current_age, "Age value isn't matched with the expected"


def test_gender_property():
    human = Human('Misha', 22, 'male')
    current_gender = "male"
    assert human.gender == current_gender, "Gender value isn't matched with the expected"


def test_gender_type(create_human):
    human = create_human
    result = human.gender
    assert isinstance(result, str), 'Gender should be string value'


def test_age_type(create_human):
    human = create_human
    result = human.age
    assert isinstance(result, int), 'Gender should be int value'
