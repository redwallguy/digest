#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
import imgurpython
import re
import requests
import json
import asyncio

def postToImgur():
    strToReg = ""

    with open("Imgur_keys.txt") as f:
        for line in f:
            strToReg += line

    regex = re.compile(r"(?<=<).*?(?=>)")
    keyreg = re.compile(r"=")

    keys = regex.findall(strToReg)
    finalkeys = {}

    for key in keys:
        finalkeys[keyreg.split(key)[0]] = keyreg.split(key)[1]
    print(finalkeys)

    client_id = finalkeys['client_id']
    client_secret = finalkeys['client_secret']
    access_token = finalkeys['access_token']
    refresh_token = finalkeys['refresh_token']
    digest_vol = finalkeys['digest_vol']

    with open("Imgur_keys_dict.txt", "w") as f:
        json.dump(finalkeys,f)

postToImgur()
with open("Imgur_keys_dict.txt") as f:
    print(json.load(f))
    print(type(json.load(f)))
