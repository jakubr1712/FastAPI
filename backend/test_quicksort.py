import pytest
from main import quicksort


@pytest.mark.parametrize(
    "input_array, expected_output",
    [
        ([], []),
        ([1], [1]),
        ([3, 1, 2], [1, 2, 3]),
        ([5, 3, 8, 6, 2], [2, 3, 5, 6, 8]),
        ([10, -1, 0, 3, 5], [-1, 0, 3, 5, 10]),
        ([1, 2, 2, 1], [1, 1, 2, 2]),
    ],
)
def test_quicksort(input_array, expected_output):
    assert quicksort(input_array) == expected_output
