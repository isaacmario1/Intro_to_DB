import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server (edit with your credentials)
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='your_password'  # 🔁 replace with your MySQL password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print(f"Error: {e}")

finally:
    # Clean up
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection closed.")

