import pymysql
import pymysql.cursors
conn = pymysql.connect(
    database="world" ,
    user="jspooner",
    password="243565207",
    host="10.100.33.60",
    cursorclass=pymysql.cursors.DictCursor
)

cursor = conn.cursor()

cursor.execute("SELECT `Name` FROM `country`")

results = cursor.fetchall()

from pprint import pprint as print

print(results)

