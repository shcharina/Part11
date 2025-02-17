from random import uniform
from typing import TypeVar
from itertools import chain

# Задание 1 Случайности не случайны

def generate_float_nums(quantity: int) -> list[float]:
    for _ in range(quantity):
        yield uniform(0, quantity)

for x in generate_float_nums(10):
    print(round(x, 3),  end=' ')

# Задание 2 Ленивое объединение

T = TypeVar("T")

def merge_lists(*lists: list[T]) -> list[T]:
    return list(chain(*lists))

# Задание 3 Рефакторинг

def generate_responses(item_ids: list[T] = [None]) -> list[dict]:
    item_ids = [None] if item_ids is None else item_ids

    for item_id in item_ids:
        new_response = dict(item_id=item_id)
        yield new_response