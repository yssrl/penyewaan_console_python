import mysql.connector

mydb = mysql.connector.connect(
    host= "localhost",
    user= "root",
    password="",
    database= "rentalps"
)

mycursor = mydb.cursor(dictionary=True)

# mycursor.execute("CREATE TABLE gameconsole (id INT AUTO_INCREMENT PRIMARY KEY, nama VARCHAR(55), harga_sewa_per_hari INT)")
# mycursor.execute("CREATE TABLE playstation (gameconsole_id VARCHAR(55), bonus_game varchar(500))")
# mycursor.execute("CREATE TABLE xbox (gameconsole_id VARCHAR(55), gamepass BOOLEAN)")
# mycursor.execute("ALTER TABLE gameconsole ADD COLUMN type VARCHAR(10)")
# mycursor.execute('CREATE TABLE user (id INT AUTO_INCREMENT PRIMARY KEY, nama varchar(55), username varchar(55), password varchar(255), role varchar(25))')