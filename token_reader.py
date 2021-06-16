from config import TOKENS_FILE


def read_all_tokens():
    with open(TOKENS_FILE) as f:
        lines = f.readlines()
    return lines
