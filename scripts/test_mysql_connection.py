import mysql.connector

DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "clean_agent"
DB_USER = "root"
DB_PASSWORD = ""

try:
    connection = mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cursor = connection.cursor()
    print("✅ MySQL Connection Successful!")

    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    print("✅ Tables in the database:")
    for table in tables:
        print(table[0])

    cursor.close()
    connection.close()
    print("✅ Connection Closed.")

except Exception as e:
    print(f"❌ Error connecting to MySQL: {e}")
