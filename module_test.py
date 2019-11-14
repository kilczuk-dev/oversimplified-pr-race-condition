from pytest import fixture

from module import MyClass


@fixture
def my_class():
    yield MyClass


def test_a_plus_b(my_class: MyClass):
    assert my_class.member_a + my_class.member_b == 0
