import pytest
from treasure.find import find_treasure


map_1 = [1, 1, 1, 9]
map_2 = [1, 1, 2, 9]
map_3 = [1, 3, 1, 1, 1, 3, 10, 9]


# Parametrized test for pytest
@pytest.mark.parametrize(
    "instructions, coins, expected",
    [
        ([9], 0, 0),
        (map_1, 0, 3),
        (map_1, 1, 2),
        (map_2, 0, None),
        (map_2, 1, 2),
        (map_2, 2, 2),
        (map_3, 0, None),
        (map_3, 1, 4),
        (map_3, 2, 3),
    ],
    ids=[
        "Base case (no coins)",
        f"Map:{map_1}, coin 0",
        f"Map:{map_1}, coin 1",
        f"Map:{map_2}, coin 0",
        f"Map:{map_2}, coin 1",
        f"Map:{map_2}, coin 2",
        f"Map:{map_3}, coin 0",
        f"Map:{map_3}, coin 1",
        f"Map:{map_3}, coin 2",
    ]
)
def test_find_treasure(instructions, coins, expected):
    result = find_treasure(instructions, coins)
    assert result == expected

