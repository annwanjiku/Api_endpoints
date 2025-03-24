import mysql.connector
from config import password,user

def get_tables():
    my_db = mysql.connector.connect(
        database = "Sakila",
        host = "localhost",
        user = user,
        password = password,
    )

    sql = "SHOW TABLES"
    my_cursor = my_db.cursor()
    my_cursor.execute(sql)

    tables = [each_table[0] for each_table in my_cursor]

    my_cursor.close()
    my_db.close()
    return tables


if __name__ == "__main__":
   print(get_tables())