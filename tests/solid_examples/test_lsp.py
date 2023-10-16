import pytest

from library.solid_examples.lsp import Bird, Penguin


class TestBird:

    def test_call_fly_method_on_subclass_instance(self):
        penguin = Penguin()
        penguin.fly()

    def test_create_instance_of_bird_raises_type_error(self):
        with pytest.raises(TypeError):
            bird = Bird()

    def test_create_subclass_instance_without_implementing_fly_method_raises_type_error(self):
        with pytest.raises(TypeError):
            class MockBird(Bird):
                pass
            bird = MockBird()
