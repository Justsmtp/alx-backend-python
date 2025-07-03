#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error

def stream_users():
    """
    Generator function that streams rows from user_data table
    one by one as dictionaries.
    """
    try:
        # Connect to the ALX_prodev database
        connection = mysql.connector.connect(
            host='localhost',
            user='your_mysql_username',    # replace with your username
            password='your_mysql_password',  # replace with your password
            database='ALX_prodev'
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data;")

        # Single loop yielding rows one by one
        for row in cursor:
            yield row

    except Error as e:
        print(f"Error connecting to database: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
