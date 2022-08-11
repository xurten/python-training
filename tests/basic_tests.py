import pytest
import library.files


def test_files():
    assert library.files.get_files_content() is not None


class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert True


class TestClassDemoInstance:
    value = 0

    def test_one(self):
        self.value = 1
        assert self.value == 1

    def test_two(self):
        assert 1 == 1


def inc(x):
    return x + 1


def f():
    raise SystemExit(1)


@pytest.mark.xfail
def test_mytest():
    with pytest.raises(SystemExit):
        f()


@pytest.mark.skip(reson="Not supported")
def test_answer():
    assert inc(4) == 5


def test_needsfiles(tmp_path):
    print(tmp_path)
    assert True


@pytest.mark.slow
def test_check_marker():
    pass