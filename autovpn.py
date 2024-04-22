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

def connect_to_vpn(server):
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

    # Comando para conectar ao VPN usando o arquivo de configuração e o arquivo de autenticação
    command = f"openvpn --config {ovpn_path} --auth-user-pass {auth_file} --cipher AES-256-GCM --inactive 3600"

    # Executa o comando
    os.system(command)

    # Remove o arquivo temporário após a conexão
    os.unlink(auth_file)

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

        # Conecta ao VPN
        print(f"Conectando ao servidor: {server}")
        connect_to_vpn(server)

        # Aguarda 10 segundos antes de trocar de servidor
        time.sleep(10)

# Exemplo de uso
VPNLoopChange()
