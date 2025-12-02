from connection import mycursor, mydb

class User:
    def __init__(self):
        pass

    def login(self, username, password):
        sql = "SELECT level FROM kasir WHERE username = %s AND password = %s"
        val = (username, password)

        mycursor.execute(sql, val)
        user = mycursor.fetchone()
        return user
    
    def select_data(self):
        sql = "SELECT * FROM user"
        mycursor.execute(sql)

        myresult = mycursor.fetchall()

        return myresult

    def insert_data(self, nama, username, password, role):
        sql = "INSERT INTO user (nama, username, password, role) VALUES (%s, %s, %s, %s)"
        val = (nama, username, password, role)

        mycursor.execute(sql, val)
        mydb.commit()

        print(mycursor.rowcount, "Data berhasil ditambahkan...")

    def update_data(self, nama, password, role, username, id):
        sql = "UPDATE user SET nama = %s, password = %s, role = %s, username = %s WHERE id = %s"
        val = (nama, password, role, username, id)

        mycursor.execute(sql, val)
        mydb.commit()

        print(mycursor.rowcount, "Data berhasil diupdate")

    def delete_data(self, id):
        sql = "DELETE FROM user WHERE id = %s"
        val = (id,)

        mycursor.execute(sql, val)
        mydb.commit()

        print(mycursor.rowcount, "Data berhasil dihapus") 
    
    def select_data_by_id(self, id):
        sql = "SELECT id, nama, username, password, role FROM user WHERE id = %s"
        val = (id,)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchone()
        print(myresult)
        return myresult