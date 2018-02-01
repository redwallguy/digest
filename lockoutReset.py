import json
import time

while True:
    with open("tempban.txt", "w") as f:
        reset = {}
        json.dump(reset,f)
        print("User lockout reset.")
    time.sleep(15)
