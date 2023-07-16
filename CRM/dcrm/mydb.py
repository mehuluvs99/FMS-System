import pymysql
dataBase = pymysql.connect(
    host='localhost',
    user='root',
    passwd='Mehulvs@99',
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE IF NOT EXISTS dcrm")

print("All Done!")