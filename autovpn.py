import os
import random
import tempfile
import time

def create_auth_file():
    # Cria um arquivo temporário para armazenar as credenciais
    auth_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
    auth_file.write("vpnbook\nemw79zs")
    auth_file.close()
    return auth_file.name

def create_ovpn_config(server):
    # Lista os arquivos de configuração .ovpn no diretório do servidor
    ovpn_files = [file for file in os.listdir(server) if file.endswith(".ovpn")]
    if not ovpn_files:
        print("Não foram encontrados arquivos de configuração .ovpn para este servidor.")
        return

    # Escolhe aleatoriamente um arquivo de configuração .ovpn
    ovpn_file = random.choice(ovpn_files)

    # Caminho completo para o arquivo de configuração
    ovpn_path = os.path.join(server, ovpn_file)

    # Cria o arquivo temporário com as credenciais
    auth_file = create_auth_file()

    # Caminho para o arquivo de saída
    output_path = "vpn_config.ovpn"

    # Escreve o conteúdo do arquivo de configuração
    with open(output_path, "w") as output_file:
        output_file.write(f"auth-user-pass {auth_file}\n")
        output_file.write(open(ovpn_path).read())

    return output_path

def VPNLoopChange():
    while True:
        # Lista os diretórios de servidores disponíveis
        servers = [directory for directory in os.listdir() if os.path.isdir(directory) and directory.startswith("vpnbook-openvpn-")]

        # Se não houver servidores disponíveis
        if not servers:
            print("Não foram encontrados servidores VPN disponíveis.")
            return

        # Escolhe aleatoriamente um servidor
        server = random.choice(servers)

        # Cria o arquivo de configuração .ovpn
        config_path = create_ovpn_config(server)

        # Conecta ao VPN
        print(f"Conectando ao servidor: {server}")
        os.system(f"openvpn --config {config_path}")

        # Aguarda 5 segundos antes de trocar de servidor
        time.sleep(5)

# Exemplo de uso
VPNLoopChange()
