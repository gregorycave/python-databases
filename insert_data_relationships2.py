import sqlite3

def query(sql,data):
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute(sql,data)
        db.commit()

if __name__ == "__main__":
    sql = "delete from ProductType where Description = 'Tea'"
    sql = "update ProductType set ProductTypeID = 15 where ProductTypeID = 2"
    sql = "update Product set ProductTypeID = 57 where ProductID = 1"
    query(sql,())
