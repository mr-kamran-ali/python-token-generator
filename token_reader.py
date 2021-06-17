from config import TOKENS_FILE
import database as db
from collections import Counter


def read_all_tokens(file=TOKENS_FILE):
    """Reads all the tokens from a file

    Args:
        file (str, optional): filepath for tokens file. Defaults to TOKENS_FILE.

    Returns:
        list: list of all the tokens in the file
    """
    with open(file) as f:
        lines = f.readlines()
    return lines


def save_all_tokens_database(tokens):
    """Saves all the tokens in the database

    Args:
        tokens (list): list of random tokens

    Returns:
        list: list of all non-unique tokens that wasn't saved in database
    """
    print("Saving tokens in database...")

    conn = db.get_conn()
    non_unique_tokens = []
    for token in tokens:
        token = token.rstrip("\n")
        if not db.insert_token(conn, token):
            non_unique_tokens.append(token)

    return non_unique_tokens


if __name__ == "__main__":
    tokens = read_all_tokens()
    non_unique_tokens = save_all_tokens_database(
        tokens
    )  # All the non-unique tokens are also available in a list if required. Printing all the non-unique tokens as well
    print("All non-unique tokens:  ")
    print(non_unique_tokens)

    # Counting and printing three most common tokens
    counter = Counter(non_unique_tokens)
    most_common_values = counter.most_common(3)

    print("Most common tokens: ", most_common_values)
