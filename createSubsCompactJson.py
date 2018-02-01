import re
import json

subText = ""

with open("Meme_subs_compact.txt") as f:
    for line in f:
        subText += line

sub_compact_array = re.split(r"|", subText)
sub_json = {}
sub_json["subs"] = sub_compact_array

with open("Meme_subs_compact2.txt", "w") as f:
    json.dump(sub_json, f)
