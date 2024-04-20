import os
import random

def connect_to_vpn(server_number=None):
    # Lista os diretórios de servidores disponíveis
    servers = [directory for directory in os.listdir() if os.path.isdir(directory) and directory.startswith("vpnbook-openvpn-")]

    # Se não houver servidores disponíveis
    if not servers:
        print("Não foram encontrados servidores VPN disponíveis.")
        return

    # Se o usuário especificou um número de servidor, use esse servidor
    if server_number is not None:
        if server_number < 1 or server_number > len(servers):
            print("Número de servidor inválido.")
            return
        server = servers[server_number - 1]
    else:
        # Caso contrário, escolha um servidor aleatoriamente
        server = random.choice(servers)

    # Lista os arquivos de configuração .ovpn no diretório do servidor
    ovpn_files = [file for file in os.listdir(server) if file.endswith(".ovpn")]
    if not ovpn_files:
        print("Não foram encontrados arquivos de configuração .ovpn para este servidor.")
        return

    # Escolhe aleatoriamente um arquivo de configuração .ovpn
    ovpn_file = random.choice(ovpn_files)

    # Caminho completo para o arquivo de configuração
    ovpn_path = os.path.join(server, ovpn_file)

    # Comando para conectar ao VPN usando o arquivo de configuração
    command = f"openvpn --config {ovpn_path} --auth-user-pass <(echo 'vpnbook\nemw79zs')"

    # Executa o comando
    os.system(command)

# Exemplo de uso
print("1. Conectar aleatoriamente")
print("2. Escolher servidor")
choice = input("Escolha uma opção: ")

if choice == "1":
    connect_to_vpn()
elif choice == "2":
    # Lista os servidores disponíveis
    servers = [directory for directory in os.listdir() if os.path.isdir(directory) and directory.startswith("vpnbook-openvpn-")]
    if not servers:
        print("Não foram encontrados servidores VPN disponíveis.")
    else:
        print("Servidores disponíveis:")
        for index, server in enumerate(servers, start=1):
            print(f"{index}. {server}")
        server_number = int(input("Digite o número do servidor (1 a {}): ".format(len(servers))))
        connect_to_vpn(server_number)
else:
    print("Opção inválida.")
