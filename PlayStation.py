from connection import mycursor, mydb
from GameConsole import GameConsole

class PlayStation(GameConsole):
    def __init__(self):
        super().__init__()
        self.table_name = "playstation"

    def insert(self, nama, harga_sewa_per_hari, bonus_game):
        gameconsole_id = GameConsole().insert(nama, harga_sewa_per_hari, 'playstation')

        sql = f"INSERT INTO {self.table_name} (gameconsole_id, bonus_game) VALUES (%s, %s)"
        val = (gameconsole_id, bonus_game)

        mycursor.execute(sql, val)
        mydb.commit()

        print("✓ Data playstation berhasil ditambahkan")
        return True

    def getAll(self):
        sql = f"""
            SELECT p.*, g.nama, g.harga_sewa_per_hari 
            FROM {self.table_name} p
            JOIN gameconsole g ON p.gameconsole_id = g.id
        """
        mycursor.execute(sql)
        data = mycursor.fetchall()

        if not data:
            print("Tidak ada data playstation")
            return
        
        return data
    
    def search_by_name(self, search):
        sql = """
            SELECT p.*, g.nama, g.harga_sewa_per_hari 
            FROM playstation p
            JOIN gameconsole g ON p.gameconsole_id = g.id
            WHERE g.nama LIKE %s
        """
        val = (f"%{search}%",)

        mycursor.execute(sql, val)
        data = mycursor.fetchall()

        if not data:
            print("Tidak ada data playstation")
            return
        
        return data
    
    def get_by_id(self, id):
        sql = "SELECT * FROM playstation p JOIN gameconsole g ON p.gameconsole_id = g.id WHERE gameconsole_id = %s"
        val = (id,)

        mycursor.execute(sql, val)
        data = mycursor.fetchone()

        return data

    def show(self, gameconsole_id):
        sql = """
            SELECT p.*, g.nama, g.harga_sewa_per_hari 
            FROM playstation p
            JOIN gameconsole g ON p.gameconsole_id = g.id
            WHERE gameconsole_id = %s
        """
        mycursor.execute(sql, (gameconsole_id,))
        data = mycursor.fetchone()
        return data

    def update(self, gameconsole_id, nama, harga_sewa_per_hari, bonus_game):
        GameConsole.update(self, gameconsole_id, nama, harga_sewa_per_hari)
        # Cek apakah data playstation ada
        playstation = self.show(gameconsole_id)
        if not playstation:
            print("✗ Data playstation tidak ditemukan")
            return False

        sql = f"UPDATE {self.table_name} SET bonus_game = %s WHERE gameconsole_id = %s"
        val = (bonus_game, gameconsole_id)

        mycursor.execute(sql, val)
        mydb.commit()

        print("✓ Data playstation berhasil diperbarui")
        return True

    def remove(self, gameconsole_id):
        sql = "DELETE FROM playstation WHERE gameconsole_id = %s"
        mycursor.execute(sql, (gameconsole_id,))
        mydb.commit()

        if mycursor.rowcount < 1:
            print("✗ Data playstation tidak ditemukan")
            return False
        else:
            # Update type gameconsole menjadi NULL
            GameConsole().remove(gameconsole_id)
            print("✓ Data playstation berhasil dihapus")
            return True