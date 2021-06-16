import string
import secrets
from config import TOKENS_FILE


def generate_tokens(limit=10000000):
    alphabet = string.ascii_lowercase  # Numbers and uppercase letter can be added here

    i = 0
    tokens = []
    while i < limit:
        i += 1
        token = "".join(secrets.choice(alphabet) for i in range(7))
        tokens.append(f"{token}\n")

    with open(TOKENS_FILE, "w") as file:
        file.writelines(tokens)

    # i = 0
    # with open("tokens.txt", "w") as file:
    #     while i < 10000000:
    #         i += 1
    #         token = "".join(secrets.choice(alphabet) for i in range(7))
    #         file.write(f"{token}\n")
