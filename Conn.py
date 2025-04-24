import serial
import sqlite3

ser = serial.Serial('COM5', 9600)  
print("Conectado à porta serial.")

conn = sqlite3.connect('dados_rfid.db')
c = conn.cursor()