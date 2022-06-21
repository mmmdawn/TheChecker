import json
from utils.string_utils import is_id
from encrypt_utils import hash_id
from constants.constants import LIST_ITEM, ID


def get_name_list(data, key: str = None, parent: str = None):
    if not data:
        # In this case: No data but the field (key) still exists
        return [key]

    if key and is_id(key):
        # ID can be a timestamp, wallet address,...
        key = ID

    if is_leaf(data):
        return [key]

    _type = type(data)
    names = []
    if _type is list:
        for item in data:
            names += get_name_list(data=item, key=LIST_ITEM)
    elif _type is dict:
        for k, v in data.items():
            names += get_name_list(data=v, key=k)

    names = set(names)
    names = list(names)
    if key:
        names = add_prefix(prefix=key, names=names)
    return names


# Checking if field is "leaf" (non-leaf: dict and list)
def is_leaf(data):
    _type = type(data)
    return not (_type is dict or _type is list)


def add_prefix(prefix: str, names: list):
    return [f"{prefix}.{name}" for name in names]


if __name__ == '__main__':
    with open('../test/sample.json', 'r') as f:
        sample = json.load(f)
    a = get_name_list(sample)
    print(sorted(a))
