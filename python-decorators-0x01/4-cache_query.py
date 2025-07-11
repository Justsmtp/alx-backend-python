import time
import sqlite3
import functools

# Cache dictionary (global)
query_cache = {}

# Decorator to handle DB connection
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

# Decorator to cache query results based on the SQL query string
def cache_query(func):
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        # Support query passed as positional or keyword argument
        query = kwargs.get('query') if 'query' in kwargs else args[0] if args else None

        if query in query_cache:
            print(f"[CACHE HIT] Returning cached result for: {query}")
            return query_cache[query]
        
        print(f"[CACHE MISS] Executing and caching: {query}")
        result = func(conn, *args, **kwargs)
        query_cache[query] = result
        return result
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# First call — should execute and cache
users = fetch_users_with_cache(query="SELECT * FROM users")
print(users)

# Second call — should return cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")
print(users_again)
