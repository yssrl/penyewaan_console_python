from connection import mycursor, mydb

class GameConsole:
    def __init__(self):
        self.table_name = "gameconsole"

    def insert(self, nama, harga_sewa_per_hari, type):
        sql = "INSERT INTO gameconsole (nama, harga_sewa_per_hari, type) VALUES (%s, %s, %s)"
        val = (nama, harga_sewa_per_hari, type)

        mycursor.execute(sql, val)
        mydb.commit()

        new_id = mycursor.lastrowid
        return new_id

    def getAll(self):
        sql = f"SELECT * FROM {self.table_name}"
        mycursor.execute(sql)
        data = mycursor.fetchall()

        if not data:
            print("Tidak ada data gameconsole")
            return

        print("\n" + "="*70)
        print(f"{'ID':<5} {'Nama':<20} {'Harga/Hari':<15} {'Type':<15}")
        print("="*70)
        for x in data:
            type_val = x['type'] if x['type'] else 'Belum diset'
            print(f"{x['id']:<5} {x['nama']:<20} Rp {x['harga_sewa_per_hari']:<12} {type_val:<15}")
        print("="*70 + "\n")

    def update(self, id: str, nama: str, harga_sewa_per_hari: str):
        print(id, nama, harga_sewa_per_hari)
        # Cek apakah data ada
        if not self.show(id):
            print("✗ Data gameconsole tidak ditemukan")
            return False

        sql = "UPDATE gameconsole SET nama = %s, harga_sewa_per_hari = %s WHERE id = %s"
        val = (nama, harga_sewa_per_hari, id)

        mycursor.execute(sql, val)
        mydb.commit()

        print(f"✓ Data gameconsole berhasil diperbarui")
        return True

    def show(self, id):
        sql = f"SELECT * FROM {self.table_name} WHERE id = %s"
        mycursor.execute(sql, (id,))
        data = mycursor.fetchone()
        return data
    
    def updateType(self, id, type_value):
        sql = f"UPDATE {self.table_name} SET type = %s WHERE id = %s"
        val = (type_value, id)
        mycursor.execute(sql, val)
        mydb.commit()

    def remove(self, id):
        # Cek apakah gameconsole memiliki relasi
        game_console = self.show(id)
        if not game_console:
            return False, "Data gameconsole tidak ditemukan"
        
        if game_console['type'] and game_console['type'] != 'NULL':
            return False, f"Gameconsole masih berelasi dengan {game_console['type']}. Hapus {game_console['type']} terlebih dahulu"

        sql = f"DELETE FROM {self.table_name} WHERE id = %s"
        mycursor.execute(sql, (id,))
        mydb.commit()

        if mycursor.rowcount < 1:
            return False, "Data tidak ditemukan"
        else:
            return True, "Data berhasil dihapus"
    
