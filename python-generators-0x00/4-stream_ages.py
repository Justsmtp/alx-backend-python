#!/usr/bin/python3
seed = __import__('seed')


def stream_user_ages():
    """
    Generator that yields user ages one by one.
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT age FROM user_data")
    for row in cursor:
        yield row['age']  # yield each age
    connection.close()


def calculate_average_age():
    """
    Calculates average age from stream_user_ages generator.
    Prints result without loading entire dataset into memory.
    """
    total_age = 0
    count = 0
    for age in stream_user_ages():  # first loop
        total_age += age
        count += 1
    average_age = total_age / count if count else 0
    print(f"Average age of users: {average_age:.2f}")


if __name__ == "__main__":
    calculate_average_age()
