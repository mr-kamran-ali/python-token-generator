from os import read
from typing import Generator
import database as db
import token_generator as generator
import token_reader as reader
import time
from collections import Counter


def main():
    """Main method of the program to run everything automatically and print the results in console."""
    start = time.process_time()

    # Initialize database
    db.initialize()

    # Generate tokens and saves them in tokens file.
    generator.generate_tokens(100000)

    # Read tokens from file and save them in database while printing three most common tokens
    tokens = reader.read_all_tokens()

    non_unique_tokens = reader.save_all_tokens_database(
        tokens
    )  # All the non-unique tokens are also available in a list if required. Printing all the non-unique tokens as well
    print("All non-unique tokens:  ")
    print(non_unique_tokens)

    # Counting and printing three most common tokens
    counter = Counter(non_unique_tokens)
    most_common_values = counter.most_common(3)
    print("Most common tokens: ", most_common_values)

    print("Time elapsed in seconds: ", time.process_time() - start)


if __name__ == "__main__":
    main()
