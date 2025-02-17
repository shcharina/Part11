import pytest

from src.ShchelkanovaArina_part11 import merge_lists

@pytest.mark.parametrize(
    'lists, result_list',
    [
        (([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6]),
        (([1, 2], [5, 6, 7]), [1, 2, 5, 6, 7]),
        ((['a', 'b'], ['ab', 'ef', 'claw']), ['a', 'b', 'ab', 'ef', 'claw']),
        ((['a', 5, 'c'], [4, 5, 6]), ['a', 5, 'c', 4, 5, 6]),
        (([0.5, 0.9], [0.1, 0.1]), [0.5, 0.9, 0.1, 0.1]),
        (([5, 'ab'], []), [5, 'ab']),
        (([[12, 12], (13, 13)], [15, 15]), [[12, 12], (13, 13), 15, 15])
    ]
)
def test_get_area_filter_title(lists, result_list):
    # Arrange & Act
    merged_list= merge_lists(*lists)

    # Assert
    assert merged_list == result_list