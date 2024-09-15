import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Connecting to the MySQL server
        conn = mysql.connector.connect(
            host="localhost",  # This is if your server is localhost
            user="my_username", 
            password="my_password" 
        )

        # Creating a cursor object
        cursor = conn.cursor()

        # Creating the database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check your username and password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: The specified database does not exist.")
        else:
            print(f"Error: {err}")
    
    finally:
        # Closing the cursor and connection
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection to MySQL closed.")

if __name__ == "__main__":
    create_database()
