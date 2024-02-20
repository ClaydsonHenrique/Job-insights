import pytest
from src.pre_built.counter import count_ocurrences


@pytest.mark.xfail
@pytest.mark.parametrize(
    "path, word, expected",
    [
        ("data/jobs.csv", "Python", 10),
        ("data/jobs.csv", "Javascript", 5),
    ],
)
def test_counter(path, word, expected):
    assert count_ocurrences(path, word) == expected
