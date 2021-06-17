import string
import secrets
from config import TOKENS_FILE


def generate_tokens(limit=10000000):
    """Generates n number of tokens and dumps them in the token file

    Args:
        limit (int, optional): number of tokens thats required to be generated. Defaults to 10000000.
    """
    alphabet = string.ascii_lowercase  # Numbers and uppercase letter can be added here

    i = 0
    tokens = []
    while i < limit:
        i += 1
        token = "".join(secrets.choice(alphabet) for i in range(7))
        tokens.append(f"{token}\n")

    with open(TOKENS_FILE, "w") as file:
        file.writelines(tokens)

    # Following way of generating and saving tokens is bit inefficient, compared to the upper method which I decided to use.
    # i = 0
    # with open("tokens.txt", "w") as file:
    #     while i < 10000000:
    #         i += 1
    #         token = "".join(secrets.choice(alphabet) for i in range(7))
    #         file.write(f"{token}\n")

    print("Tokens generated.")


if __name__ == "__main__":
    generate_tokens()
