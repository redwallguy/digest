#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
import imgurpython
import json
import os
import sys
import errormail
import asyncio
import traceback

def postToImgur(urls):
    try:
        with open("Imgur_keys_dict.txt") as f:
            imgurkeys = json.load(f)
        client_idv = imgurkeys['client_id']
        client_secretv = imgurkeys['client_secret']
        access_tokenv = imgurkeys['access_token']
        refresh_tokenv = imgurkeys['refresh_token']
        digest_vol = imgurkeys['digest_vol']

        imgurclient = imgurpython.ImgurClient(client_id=client_idv,
                                              client_secret=client_secretv,
                                              refresh_token=refresh_tokenv)
        test_call = imgurclient.get_account_settings("DevsBad"\
                                                     "lyPhotoshoppedPicturesOfM"\
                                                     "ichaelCera")
        title = "Meme Digest Vol. " + str(digest_vol)
        
        album_info = imgurclient.create_album({"title": title})
        deletehash = album_info['deletehash']
        album_id = album_info['id']

        for key in urls:
            try:
                imgurclient.upload_from_url(urls[key][0], {"album":deletehash,"description":urls[key][1] + "\n-" +key})
                print("Posted...")
            except Exception as e:
                print(e)
                print(traceback.format_exc())

        digest_vol += 1
        imgurkeys['digest_vol'] = digest_vol

        with open("Imgur_keys_dict.txt", "w") as f:
            json.dump(imgurkeys,f)

        album_url = "imgur.com/a/" + album_id
        return album_url
    except imgurpython.helpers.error.ImgurClientError as e:
        print(e.error_message)
        print(e.status_code)
        errormail.sendDevError("Imgur Error in script"
                               + os.path.basename(sys.argv[0]),
                               str(e.error_message))
        
def get_digest(vol_no = None):
        try:
            with open("Imgur_keys_dict.txt") as f:
                imgurkeys = json.load(f)
            client_idv = imgurkeys['client_id']
            client_secretv = imgurkeys['client_secret']
            access_tokenv = imgurkeys['access_token']
            refresh_tokenv = imgurkeys['refresh_token']
            digest_vol = imgurkeys['digest_vol']

            imgurclient = imgurpython.ImgurClient(client_id=client_idv,
                                                        client_secret=client_secretv,
                                                        refresh_token=refresh_tokenv)
            test_call = imgurclient.get_account_settings("DevsBad"\
                                                     "lyPhotoshoppedPicturesOfM"\
                                                     "ichaelCera")
            if vol_no is None:
                all_albums = imgurclient.get_account_albums("me", page=0)
                for album in all_albums:
                    if "Meme Digest Vol." in album.title:
                        return album.link
            else:
                title = "Meme Digest Vol. " + vol_no
                all_albums = imgurclient.get_account_albums("me")
                for album in all_albums:
                    if title in album.title and album.title in title:
                        return album.link
                return "Sorry, that volume is not yet made."
        except imgurpython.helpers.error.ImgurClientError as e:
            print(e.error_message)
            print(e.status_code)
            errormail.sendDevError("Imgur Error in script"
                                   + os.path.basename(sys.argv[0]),
                                   str(e.error_message))
