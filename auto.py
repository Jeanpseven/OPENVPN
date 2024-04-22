import subprocess
import time
import os

# Redireciona a saída padrão e de erro para /dev/null
FNULL = open(os.devnull, 'w')

while True:
    # Executa o script vpn.py silenciosamente
    subprocess.run(["python3", "vpn.py"], stdout=FNULL, stderr=subprocess.STDOUT)

    # Espera 5 segundos antes de rodar novamente
    time.sleep(5)
