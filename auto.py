import requests
import random
import time

proxies = [
    {'http': 'http://103.109.117.13:8080'},
    {'http': 'http://113.53.200.132:8080'},
    {'http': 'http://116.203.15.220:8080'},
    {'http': 'http://103.226.80.94:8080'},
    {'http': 'http://117.55.124.114:8080'},
    {'http': 'http://120.77.174.172:8080'},
    {'http': 'http://182.61.58.12:8080'},
    {'http': 'http://183.166.224.12:8080'},
    {'http': 'http://192.168.1.105:8080'},
    {'http': 'http://198.50.220.44:8080'},
    {'http': 'http://103.109.117.13:8080'},
    {'http': 'http://113.53.200.132:8080'},
    {'http': 'http://116.203.15.220:8080'},
    {'http': 'http://103.226.80.94:8080'},
    {'http': 'http://117.55.124.114:8080'},
    {'http': 'http://120.77.174.172:8080'},
    {'http': 'http://182.61.58.12:8080'},
    {'http': 'http://183.166.224.12:8080'},
    {'http': 'http://192.168.1.105:8080'},
    {'http': 'http://198.50.220.44:8080'}
]

def change_ip():
    proxy = random.choice(proxies)
    try:
        r = requests.get('http://icanhazip.com', proxies=proxy, timeout=10)
        print("Novo IP:", r.text.strip())
    except Exception as e:
        print("Erro ao mudar o IP:", e)

if __name__ == "__main__":
    try:
        while True:
            change_ip()
            time.sleep(5)
    except KeyboardInterrupt:
        print("Programa encerrado.")
