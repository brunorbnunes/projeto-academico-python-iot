import serial
import sqlite3

ser = serial.Serial('COM5', 9600)  
print("Conectado à porta serial.")
