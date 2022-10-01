
import os
from pymssql import connect
from getpass import getpass

host = os.environ.get("DB_HOST")
user = os.environ.get("DB_USER")
pwd  = getpass("Please enter user's MSSQL password:")

if not host:
    print("Please set the DB_HOST env variable when running the container")
    exit(1)
if not user:
    print("Please set the DB_USER env variable when running the container")
    exit(1)

c = connect(host=host, port='1433', user=user, password=pwd)
cursor = c.cursor()
cursor.execute("select name FROM sys.databases;")

print("Databases:")
for row in cursor.fetchall():
    print(f"- {row[0]}")
