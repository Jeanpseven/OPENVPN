import random
import time
import signal

def change_ip_to_random():
    global interrupted
    interrupted = False

    while True:
        if interrupted:
            break

        # Change IP to a random value here
        random_ip = random.choice(available_proxies)
        print(f"Changed IP to: {random_ip}")

        # Wait for 5 seconds
        time.sleep(5)

    # Restore the original IP here
    set_ip(original_ip)
    print("IP restored to the original value.")

def signal_handler(signal, frame):
    global interrupted
    interrupted = True
    print("Exiting...")

def main():
    # Initialize variables
    global available_proxies, original_ip, interrupted
    original_ip = get_original_ip()
    available_proxies = get_available_proxies()
    interrupted = False

    # Set up signal handler
    signal.signal(signal.SIGINT, signal_handler)

    # Change IP to random
    change_ip_to_random()

if __name__ == "__main__":
    main()
