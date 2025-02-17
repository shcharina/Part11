import pytest

from src.ShchelkanovaArina_part11 import generate_responses

@pytest.mark.parametrize(
    'item_ids, result_list',
    [
        ([1, 2, 3], [{'item_id': 1}, {'item_id': 2}, {'item_id': 3}]),
        ([None], [{'item_id': None}]),
        ([], [])
    ]
)
def test_get_area_filter_title(item_ids, result_list):
    # Arrange & Act
    id_list = list(generate_responses(item_ids=item_ids))

    # Assert
    assert id_list == result_list