import sqlite3

class Database:
# Create the class object called Database

    def __init__(self, db):
    # Define __init__ function
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.conn.commit()
        # Use instance variables so they are applied in the functions below

    def insert(self, title, author, year, isbn):
    # Define backend instert method linked to add entry button
        self.cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
        self.conn.commit()

    def view(self):
    # Define backend view method linked to view all button
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows

    def search(self, title="", author="", year="", isbn=""):
    # Define backend search method linked to search entry button
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
    # Define backend delete method linked to delete selected button
        self.cur.execute("DELETE FROM book WHERE id=? ",(id,))
        self.conn.commit()

    def update(self, id, title, author, year, isbn):
    # Define backend update method linked to update selected button
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
        self.conn.commit()

    def __del__(self):
    # Define __del__ function that closes all the connection for every method
        self.conn.close()
