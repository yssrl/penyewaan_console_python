from connection import mycursor, mydb

class Transaksi:
    def __init__(self):
        pass

    def create(self, gameconsole_id, nama_penyewa, harga_sewa_per_hari, jumlah_hari):
        sql = "INSERT INTO transaksi (gameconsole_id, nama_penyewa, harga_sewa_per_hari, jumlah_hari) VALUES (%s, %s, %s, %s)"
        val = (gameconsole_id, nama_penyewa, harga_sewa_per_hari, jumlah_hari)

        mycursor.execute(sql, val)
        mydb.commit()

        print("Berhasil menambahkan data transaksi")

    def get_all(self):
        sql = """
            SELECT t.id, t.nama_penyewa, t.harga_sewa_per_hari, t.jumlah_hari, c.id gameconsole_id, c.nama
            FROM transaksi t
            LEFT JOIN gameconsole c
            ON t.gameconsole_id = c.id
        """

        mycursor.execute(sql)
        data = mycursor.fetchall()

        return data
    
    def get_by_id(self, id):
        sql = "SELECT * FROM transaksi WHERE id = %s"
        val = (id,)

        mycursor.execute(sql, val)
        data = mycursor.fetchone()

        return data
    
    def delete(self, id):
        sql = "DELETE FROM transaksi WHERE id = %s"
        val = (id,)

        mycursor.execute(sql, val)
        mydb.commit()

        print("Berhasil menghapus data transaksi")

    def update(self, gameconsole_id, nama_penyewa, harga_sewa_per_hari, jumlah_hari, id):
        sql = """
            UPDATE transaksi
            SET gameconsole_id = %s, nama_penyewa = %s, harga_sewa_per_hari = %s, jumlah_hari = %s
            WHERE id = %s
        """
        val = (gameconsole_id, nama_penyewa, harga_sewa_per_hari, jumlah_hari, id)

        mycursor.execute(sql, val)
        mydb.commit()

        print("Berhasil memperbarui data transaksi")
