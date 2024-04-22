import subprocess
import time

while True:
    # Inicia o processo do script vpn.py
    vpn_process = subprocess.Popen(["python3", "vpn.py"])

    # Espera 5 segundos
    time.sleep(5)

    # Mata o processo do script vpn.py
    vpn_process.terminate()

    # Aguarda um momento para garantir que o processo seja encerrado
    time.sleep(1)
