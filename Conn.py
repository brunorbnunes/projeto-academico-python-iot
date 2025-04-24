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

while True:
    line = ser.readline().decode('utf-8').strip()
    print(f"Linha lida: {line}")

    if line.startswith("VALID"):
        try:
            _, uid, date, time = line.split(',')

            
            print(f"UID: {uid}, Data: {date}, Hora: {time}")

            
            c.execute('INSERT INTO registros (uid, data, hora) VALUES (?, ?, ?)', (uid.strip(), date.strip(), time.strip()))
            conn.commit()
            print("Dados armazenados no banco de dados.")

            c.execute('SELECT * FROM registros')
            registros = c.fetchall()

            for registro in registros:
                print(f"ID: {registro[0]}, UID: {registro[1]}, Data: {registro[2]}, Hora: {registro[3]}")

        except ValueError as e:
            print(f"Erro ao processar a linha: {line}. Erro: {e}")
    else:
        print("Dados inválidos, UID não reconhecido.")
