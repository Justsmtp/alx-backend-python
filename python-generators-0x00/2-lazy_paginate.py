#!/usr/bin/python3
seed = __import__('seed')


def paginate_users(page_size, offset):
    """
    Fetch a single page of users from the database.
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows


def lazy_pagination(page_size):
    """
    Generator that lazily paginates through users table one page at a time.
    """
    offset = 0
    while True:  # Single loop
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size
