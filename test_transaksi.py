from Transaksi import Transaksi
from GameConsole import GameConsole

transaksi_controller = Transaksi()
gameconsole_controller = GameConsole()

while True:
    print("1. lihat data")
    print("2. Tambah data")
    print("3. Hapus data")
    print("4. Edit data")

    menu = input("Masukkan menu: ")

    if menu == "1":
        data = transaksi_controller.get_all()
        print(data)

    if menu == "2":
        while True:
            gameconsole_id = input("Masukkan gameconsole_id: ")
            if not gameconsole_id:
                print("Masukkan gameconsole_id")
                continue

            gameconsole = gameconsole_controller.show(gameconsole_id)
            if gameconsole == None:
                print("Gameconsole tidak ditemukan")
                continue

            nama_penyewa =  input("Masukkan nama penyewa: ")
            jumlah_hari = input("Masukkan jumlah hari: ")

            if not nama_penyewa or not jumlah_hari:
                print("Lengkapi form")
                continue

            try:
                int(jumlah_hari)
            except:
                print("Jumlah hari harus berupa angka")
                continue

            transaksi_controller.create(gameconsole_id, nama_penyewa, gameconsole["harga_sewa_per_hari"], jumlah_hari)
            break
    
    if menu == "3":
        while True:
            id = input("Masukkan id: ")
            if not id:
                print("Masukkan dengan benar")
                continue

            transaksi = transaksi_controller.get_by_id(id)
            if transaksi == None:
                print("Transaksi tidak ditemukan")
                continue

            print(transaksi)

            transaksi_controller.delete(id)
            break

    if menu == "4":
        while True:
            id = input("Masukkan id: ")
            if not id:
                print("Masukkan dengan benar")
                continue

            transaksi = transaksi_controller.get_by_id(id)
            if transaksi == None:
                print("Transaksi tidak ditemukan")
                continue

            print(transaksi)

            gameconsole_id = input("Masukkan gameconsole_id: ")
            if not gameconsole_id:
                print("Masukkan gameconsole_id")
                continue

            gameconsole = gameconsole_controller.show(gameconsole_id)
            if gameconsole == None:
                print("Gameconsole tidak ditemukan")
                continue

            nama_penyewa =  input("Masukkan nama penyewa: ")
            jumlah_hari = input("Masukkan jumlah hari: ")

            if not nama_penyewa or not jumlah_hari:
                print("Lengkapi form")
                continue

            try:
                int(jumlah_hari)
            except:
                print("Jumlah hari harus berupa angka")
                continue

            transaksi_controller.update(gameconsole_id, nama_penyewa, gameconsole["harga_sewa_per_hari"], jumlah_hari, id)
            break