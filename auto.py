import stem.process
import stem.control
import time

def change_ip():
    with stem.control.Controller.from_port(port=9051) as controller:
        controller.authenticate()  # Autenticar com o controlador do Tor

        # Pedir para o Tor obter uma nova identidade
        controller.signal(stem.Signal.NEWNYM)

        # Aguardar até que o novo IP esteja pronto
        time.sleep(controller.get_newnym_wait())

        # Obter o novo IP
        print("Novo IP:", requests.get('http://icanhazip.com').text.strip())

if __name__ == "__main__":
    try:
        while True:
            change_ip()
            time.sleep(5)
    except KeyboardInterrupt:
        print("Programa encerrado.")
