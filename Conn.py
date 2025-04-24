import serial
import sqlite3

ser = serial.Serial('COM5', 9600)  
print("Conectado à porta serial.")

conn = sqlite3.connect('dados_rfid.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS registros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        uid TEXT NOT NULL,
        data TEXT NOT NULL,
        hora TEXT NOT NULL
    )
''')
conn.commit()