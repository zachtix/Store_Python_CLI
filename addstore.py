import sqlite3
import time

def store():
    time.sleep(0.2)
    barcode = int(input('Bar Code :'))
    name = input('Name :')
    price = int(input('Price :'))
    stock = int(input('Stock :'))
    def insertVaribleIntoTable(BARCODE, NAME, PRICE, STOCK):
        try:
            time.sleep(1)
            sqliteConnection = sqlite3.connect('database_store.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")
                    
            time.sleep(0.2)
            sqlite_insert_with_param = """INSERT INTO store
                            (BARCODE, NAME, PRICE, STOCK) 
                            VALUES (?, ?, ?, ?);"""

            data_tuple = (BARCODE, NAME, PRICE, STOCK)
            cursor.execute(sqlite_insert_with_param, data_tuple)
            sqliteConnection.commit()
            print("Variables inserted successfully into store table")

            cursor.close()

        except sqlite3.Error as error:
            time.sleep(0.2)
            print("Failed to insert variable into sqlite table", error)
        finally:
            if (sqliteConnection):
                time.sleep(0.2)
                sqliteConnection.close()
                print("The SQLite connection is closed")
    insertVaribleIntoTable(barcode, name, price, stock)