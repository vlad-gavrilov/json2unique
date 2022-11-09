import pytest
import random
import string

from src.json2unique.parser import parse_json_to_list_of_unique
from src.json2unique.context_manager import RecursionDepth


def gen_nested_dict(dct, depth=10):
    rnd_str = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))
    dct[rnd_str] = dict()
    if depth > 1:
        dct[rnd_str] = gen_nested_dict(dct[rnd_str], depth - 1)
    return dct


@pytest.mark.parametrize('depth', [10, 100, 500, 900, 1000, 5000, 10000, 20000])
def test_parser(depth):
    with RecursionDepth(depth * 2):
        big_depth_dict = gen_nested_dict({}, depth=depth)
        resulting_list = parse_json_to_list_of_unique(big_depth_dict)

    assert len(resulting_list) == depth
