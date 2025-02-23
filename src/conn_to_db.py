import psycopg2
import os
from dotenv import load_dotenv

load_dotenv(override=True)

hostname = os.getenv("olist_hostname")
database = os.getenv("olist_database")
port = os.getenv("olist_port")
username = os.getenv("olist_username")
password = os.getenv("olist_password")

# Establishing the connection
# Establishing the connection
conn = psycopg2.connect(
   database=database, user=username, password=password, host=hostname, port=port
)
# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Executing an MYSQL function using the execute() method
cursor.execute("select version()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Connection established to: ", data)

# Closing the connection
conn.close()
