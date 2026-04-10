import time

def tick_tock(seconds):
    i = 0
    while i < seconds:
        if i < seconds:
            print("Tick...")
            time.sleep(1)
            i += 1
            if i < seconds:
                print("Tock...")
                time.sleep(1)
                i += 1

tick_tock(3)