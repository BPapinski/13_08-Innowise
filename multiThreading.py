import threading
import time
from threading import Semaphore


espresso_machine = Semaphore(3)

def make_coffe(barista_name):
    with espresso_machine:
        print(f"{barista_name} is using the espresso machine")
        time.sleep(5)
        print(f"{barista_name} is done making coffee")

baristas = ["Anrzej", "Bartek", "Czarek", "Darek", "Eryk", "Franek", "Ganek"] # kazdy ma zrobic jedna kawe
threads = []

for barista in baristas:
    thread = threading.Thread(target=make_coffe, args=(barista,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("all coffee orders are coplete!")