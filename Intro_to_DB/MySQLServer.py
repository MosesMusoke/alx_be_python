import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Connect to MySQL server
        conn = mysql.connector.connect(
            host="localhost",
            user="my_username",  # Replace with your MySQL username
            password="my_password"  # Replace with your MySQL password
        )

        # Create a cursor object
        cursor = conn.cursor()

        # SQL query to create the database
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check your username and password.")
        else:
            print(f"Error: {err}")

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection to MySQL closed.")

if __name__ == "__main__":
    create_database()
