def test_grow(create_human):
    human = create_human
    human.grow()
    assert human.age == 23
