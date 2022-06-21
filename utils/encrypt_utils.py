import hashlib


def hash_id(fields):
    fields = sorted(fields)
    string = ':'.join(fields)
    return hashlib.sha256(f'{string}'.encode()).hexdigest()
