import mysql.connector

# AWS RDS MySQL connection parameters
host = "sampledatabase.cbsm42wu8lt1.ca-central-1.rds.amazonaws.com"
user = "admin"
password = "password!123"
database = "sampledb"

# Establish a connection
try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    if connection.is_connected():
        print("Connected to the database")
        
        # Create a cursor
        cursor = connection.cursor()

        # Execute SQL queries
        cursor.execute("SELECT * FROM employees")
        rows = cursor.fetchall()

        # Process the result
        for row in rows:
            print(row)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the cursor and connection
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Connection closed")