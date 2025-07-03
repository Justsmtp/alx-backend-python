#!/usr/bin/python3
seed = __import__('seed')


def stream_users_in_batches(batch_size):
    """
    Generator that fetches batches of users from the database.
    """
    offset = 0
    while True:  # one loop
        connection = seed.connect_to_prodev()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM user_data LIMIT {batch_size} OFFSET {offset}")
        rows = cursor.fetchall()
        connection.close()

        if not rows:
            break

        yield rows  # use yield, not return
        offset += batch_size


def batch_processing(batch_size):
    """
    Processes each batch by filtering users over age 25 and prints them.
    """
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                print(user)  # process each filtered user
