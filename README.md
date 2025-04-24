# 📡 Projeto IoT + Indústria 4.0 com RFID, Arduino e Python

Este projeto integra conceitos de **IoT (Internet das Coisas)** e **Indústria 4.0**, utilizando um sistema de leitura RFID com **Arduino**, **Python**, **SQLite3**, um **Display LCD**, e um **módulo RTC (Relógio de Tempo Real)** para registrar informações localmente.

## 🔧 Tecnologias e Componentes Utilizados

- 🟣 **Arduino roxo** (compatível com UNO)
- 🧿 **Módulo RFID**
- 🖥️ **Display LCD 16x2 com I2C**
- ⏰ **Módulo RTC (DS3231 ou similar)**
- 🐍 **Python 3**
- 🗃️ **SQLite3** para banco de dados local
- 🔌 **PySerial** para comunicação serial entre Arduino e PC

## 💡 Funcionamento

1. O Arduino lê um cartão RFID.
2. Se o UID for válido, ele envia os dados pela serial no formato: VALID,UID,DATA,HORA
3. O script Python recebe esses dados via `pyserial`, armazena no banco de dados SQLite e exibe todos os registros salvos.
