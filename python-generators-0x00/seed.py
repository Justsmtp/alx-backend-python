#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error
import csv
import uuid

DB_NAME = "ALX_prodev"


def connect_db():
    """
    Connects to the MySQL server (without specifying a database).
    """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',       # Change if needed
            password='your_password'  # Replace with your MySQL root password
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None


def create_database(connection):
    """
    Creates the ALX_prodev database if it doesn't exist.
    """
    try:
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        print(f"Database {DB_NAME} created successfully")
    except Error as e:
        print(f"Error creating database: {e}")
    finally:
        cursor.close()


def connect_to_prodev():
    """
    Connects to the ALX_prodev database.
    """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',       # Change if needed
            password='your_password',  # Replace with your MySQL root password
            database=DB_NAME
        )
        return connection
    except Error as e:
        print(f"Error connecting to database {DB_NAME}: {e}")
        return None


def create_table(connection):
    """
    Creates the user_data table with specified fields if it doesn't exist.
    """
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_data (
                user_id CHAR(36) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age DECIMAL NOT NULL,
                INDEX (user_id)
            );
        """)
        connection.commit()
        print("Table user_data created successfully")
    except Error as e:
        print(f"Error creating table: {e}")
    finally:
        cursor.close()


def insert_data(connection, csv_file):
    """
    Inserts data from a CSV file into user_data table.
    """
    try:
        cursor = connection.cursor()
        with open(csv_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                user_id = str(uuid.uuid4())
                name = row['name']
                email = row['email']
                age = row['age']
                cursor.execute("""
                    INSERT INTO user_data (user_id, name, email, age)
                    VALUES (%s, %s, %s, %s)
                """, (user_id, name, email, age))
        connection.commit()
        print(f"Data inserted successfully from {csv_file}")
    except Error as e:
        print(f"Error inserting data: {e}")
    except FileNotFoundError:
        print(f"CSV file {csv_file} not found.")
    finally:
        cursor.close()
