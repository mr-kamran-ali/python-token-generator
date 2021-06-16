from typing import Generator
import database as db
import token_generator as generator
import token_reader as reader
import time


def main():
    start = time.process_time()

    db.initialize()
    generator.generate_tokens(10000000)

    tokens = reader.read_all_tokens()
    conn = db.get_conn()

    for token in tokens:
        db.insert_token(conn, token)

    print("Time elapsed: ", time.process_time() - start)


if __name__ == "__main__":
    main()
