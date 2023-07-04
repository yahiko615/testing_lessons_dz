import pytest


def test_grow(create_human):
    human = create_human
    human.grow()
    assert human.age == 23


def test_grow_reach_age_limit(create_giga_old_human):
    human = create_giga_old_human
    for _ in range(2):
        human.grow()
    assert human._Human__status == "dead", "Person should reach age limit and die"


def test_grow_if_already_dead(create_giga_old_human):
    human = create_giga_old_human
    human._Human__status = "dead"
    with pytest.raises(Exception, match="Misha is already dead..."):
        human.grow()


def test_is_alive_status_alive(create_human):
    human = create_human
    result = human._Human__is_alive()
    assert result is True, "Person should be alive"


def test_is_alive_status_dead(create_human):
    human = create_human
    human._Human__status = "dead"
    with pytest.raises(Exception, match="Misha is already dead..."):
        human._Human__is_alive()


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


def test_age_property(create_human):
    human = create_human
    assert human.age == 22


def test_gender_property(create_human):
    human = create_human
    assert human.gender == "male"
