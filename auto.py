import socket
import socks
import time
import signal
import random

# Get the original IP address
def get_original_ip():
    return socket.gethostbyname(socket.gethostname())

# Get the available proxies
available_proxies = [
    'http://103.109.117.13:8080',
    'http://113.53.200.132:8080',
    'http://116.203.15.220:8080',
    'http://103.226.80.94:8080',
    'http://117.55.124.114:8080',
    'http://120.77.174.172:8080',
    'http://182.61.58.12:8080',
    'http://183.166.224.12:8080',
    'http://192.168.1.105:8080',
    'http://198.50.220.44:8080'
    # Add more available proxies here
]

def get_available_proxies():
    return available_proxies

# Set the IP address
def set_ip(ip):
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, ip.split(':')[0], int(ip.split(':')[1]))
    socket.socket = socks.socksocket

# Change the IP to random
def change_ip_to_random():
    global interrupted
    interrupted = False

    while True:
        if interrupted:
            break

        # Change IP to a random value
        random_ip = random.choice(get_available_proxies())
        print(f"Changed IP to: {random_ip}")

        # Wait for 5 seconds
        time.sleep(5)

    # Restore the original IP
    set_ip(get_original_ip())
    print("IP restored to the original value.")

# Signal handler
def signal_handler(signal, frame):
    global interrupted
    interrupted = True
    print("Exiting...")

# Main function
def main():
    # Initialize variables
    global interrupted
    original_ip = get_original_ip()
    interrupted = False

    # Set up signal handler
    signal.signal(signal.SIGINT, signal_handler)

    # Change IP to random
    change_ip_to_random()

if __name__ == "__main__":
    main()
