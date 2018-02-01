import re
import json

subs_re = re.compile(r"(?<=r/).+(?=/)")
subText = ""

with open("Meme_subs.txt") as f:
    for line in f:
        subText += line

sub_compact_array = subs_re.findall(subText)
sub_json = {}
sub_json["subs"] = sub_compact_array

with open("Meme_subs_compact.txt", "w") as f:
    json.dump(sub_json, f)
