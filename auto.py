import subprocess
import time

while True:
    # Executa o script vpn.py
    subprocess.run(["python3", "vpn.py"])

    # Espera 5 segundos antes de rodar novamente
    time.sleep(5)
