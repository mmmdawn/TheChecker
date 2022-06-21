from constants.constants import ID_STARTS_WITH


# Check if input string is an id (wallet address, timestamp for example)
def is_id(string: str):
    return string.startswith(ID_STARTS_WITH) or string.isnumeric()
