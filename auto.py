import os
import random
import subprocess
import tempfile
import time

def create_auth_file():
    # Cria um arquivo temporário para armazenar as credenciais
    auth_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
    auth_file.write("vpnbook\nemw79zs")
    auth_file.close()
    return auth_file.name

def create_vpn_change_script():
    # Cria um arquivo temporário com o comando para mudar de servidor VPN
    script_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
    script_file.write("#!/bin/bash\n")
    script_file.write("while true;\n")
    script_file.write("do\n")
    script_file.write("  servers=$(ls -d vpnbook-openvpn-* 2>/dev/null)\n")
    script_file.write("  if [ -z \"$servers\" ]; then\n")
    script_file.write("    echo \"Não foram encontrados servidores VPN disponíveis.\"\n")
    script_file.write("    exit 1\n")
    script_file.write("  fi\n")
    script_file.write("  server=$(echo \"$servers\" | shuf -n 1)\n")
    script_file.write("  echo \"Conectando ao servidor: $server\"\n")
    script_file.write(f"  openvpn --config \"$server\"/*.ovpn --auth-user-pass {create_auth_file()} --cipher AES-256-GCM --inactive 3600 &\n")
    script_file.write("  sleep 5\n")
    script_file.write("done\n")
    script_file.close()
    os.chmod(script_file.name, 0o755)  # Define permissões de execução
    return script_file.name

def change_vpn_and_ip():
    # Cria o script de mudança de VPN
    vpn_change_script = create_vpn_change_script()

    # Inicia o script de mudança de VPN em um subprocesso
    vpn_process = subprocess.Popen(["bash", vpn_change_script])

    while True:
        # Espera 5 segundos antes de matar e reiniciar o processo subprocesso
        time.sleep(5)

        # Mata o processo subprocesso atual
        vpn_process.kill()

        # Cria um novo script de mudança de VPN
        vpn_change_script = create_vpn_change_script()

        # Inicia um novo processo subprocesso com o novo script
        vpn_process = subprocess.Popen(["bash", vpn_change_script])

# Exemplo de uso
change_vpn_and_ip()