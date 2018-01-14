import json

with open("tempban.txt", "w") as f:
    reset = {}
    json.dump(reset,f)
    print("User lockout reset.")
