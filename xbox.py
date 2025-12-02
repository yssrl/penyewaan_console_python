from connection import mycursor, mydb
from GameConsole import GameConsole

class Xbox(GameConsole):
    def __init__(self):
        super().__init__()
        self.table_name = "xbox"

    def insert(self, nama, harga_sewa_per_hari, gamepass):
        gameconsole_id = GameConsole().insert(nama, harga_sewa_per_hari, 'xbox')
        
        sql = f"INSERT INTO {self.table_name} (gameconsole_id, gamepass) VALUES (%s, %s)"
        val = (gameconsole_id, gamepass)

        mycursor.execute(sql, val)
        mydb.commit()

        print("✓ Data xbox berhasil ditambahkan")
        return True

    def getAll(self):
        sql = f"""
            SELECT x.*, g.nama, g.harga_sewa_per_hari 
            FROM {self.table_name} x
            JOIN gameconsole g ON x.gameconsole_id = g.id
        """
        mycursor.execute(sql)
        data = mycursor.fetchall()

        if not data:
            print("Tidak ada data xbox")
            return

        print("\n" + "="*75)
        print(f"{'Console ID':<12} {'Nama Console':<20} {'Harga/Hari':<15} {'Gamepass':<15}")
        print("="*75)
        for x in data:
            gamepass_status = "Ya" if x['gamepass'] else "Tidak"
            print(f"{x['gameconsole_id']:<12} {x['nama']:<20} Rp {x['harga_sewa_per_hari']:<12} {gamepass_status:<15}")
        print("="*75 + "\n")

    def show(self, gameconsole_id):
        sql = """
            SELECT x.*, g.nama, g.harga_sewa_per_hari 
            FROM xbox x
            JOIN gameconsole g ON x.gameconsole_id = g.id
            WHERE gameconsole_id = %s
        """
        mycursor.execute(sql, (gameconsole_id,))
        data = mycursor.fetchone()
        return data

    def update(self, gameconsole_id: str, nama: str, harga_sewa_per_hari: str, gamepass: int):
        GameConsole().update(gameconsole_id, nama, harga_sewa_per_hari)
        # Cek apakah data xbox ada
        xbox = self.show(gameconsole_id)
        if not xbox:
            print("✗ Data xbox tidak ditemukan")
            return False
        
        sql = "UPDATE xbox SET gamepass = %s WHERE gameconsole_id = %s"
        val = (gamepass, gameconsole_id)

        mycursor.execute(sql, val)
        mydb.commit()

        print("✓ Data xbox berhasil diperbarui")
        return True

    def remove(self, gameconsole_id):
        sql = f"DELETE FROM {self.table_name} WHERE gameconsole_id = %s"
        mycursor.execute(sql, (gameconsole_id,))
        mydb.commit()

        if mycursor.rowcount < 1:
            print("✗ Data xbox tidak ditemukan")
            return False
        else:
            # Update type gameconsole menjadi NULL
            GameConsole().remove(gameconsole_id)
            print("✓ Data xbox berhasil dihapus")
            return True