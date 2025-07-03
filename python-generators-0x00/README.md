# Python Generators - Seed Script for ALX_prodev

This script sets up the MySQL database `ALX_prodev` with a `user_data` table and populates it with sample data from `user_data.csv`.

## Features

- Connects to the MySQL server
- Creates the `ALX_prodev` database if it doesn't exist
- Creates the `user_data` table with:
  - `user_id` (UUID primary key, indexed)
  - `name` (VARCHAR, not null)
  - `email` (VARCHAR, not null)
  - `age` (DECIMAL, not null)
- Populates the table with data from `user_data.csv`

## Functions

- `connect_db()`: Connects to MySQL server.
- `create_database(connection)`: Creates the `ALX_prodev` database.
- `connect_to_prodev()`: Connects directly to the `ALX_prodev` database.
- `create_table(connection)`: Creates the `user_data` table.
- `insert_data(connection, csv_file)`: Inserts data from a CSV file.

## Usage

1. Make sure you have MySQL installed and running.
2. Place your `user_data.csv` in the same directory.
3. Run the script:
   ```bash
   ./0-main.py
