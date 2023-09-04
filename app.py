from flask import Flask, request
import sys
import os
import platform

# check os
if platform.system() == 'Windows':
    # get save folder path with system variables and so on
    save_path = 'C:\\Users\\Usuario\\OneDrive\\Documentos\\Icewind Dale - Enhanced Edition\\save\\000000001-Quick-Save'
    files = os.listdir(save_path)


# build json
response_json = {
    'characters': [],
}

# check if there are any quicksaves
# if there aren't go for autosaves
in_file = open('C:\\Users\\Usuario\\OneDrive\\Documentos\\Icewind Dale - Enhanced Edition\\save\\000000001-Quick-Save\\Baldur.gam', 'rb')
# 352 bytes per character
character_size_in_bytes = 352
# first character starts at line 368 dec 170 hex
# first character name starts at byte 372
first_character_address = 372
# first char name
for n in range(0,6):    
    # parse data
    # TODO check the actual number of characters
    in_file.seek(first_character_address + n * character_size_in_bytes)
    character_name = in_file.read(20).decode('utf-8').rstrip('\x00')
    # TODO make a character dict to be inserted on the characters list
    response_json['characters'].append(character_name)
    # portrait lines 
    # 920 HAMF_M anão boladão
    # 6B90 HFF2_M otakucel
    # 5540 BDTMAM fuhrer painho
    # 4520 HMW_M magocel
    # 2B10 BDTMJM salmão
    # 1AE0 DMF2_M anão gordão
    # equipment
    # spells
    # class
    # alignment
    # stats


# serve it
app = Flask(__name__)
@app.route('/',  methods=["GET", "OPTIONS"])
def characters():
    if request.method == 'OPTIONS':
        return _build_cors_preflight_response()
    else:
        response = app.make_response(response_json)
        response.charset = "utf-8"
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        response.headers.add('Content-type', 'application/json')
        response.headers.add("Access-Control-Allow-Origin", "https://localhost:8080")
        return response

def _build_cors_preflight_response():
    response = app.make_response({})
    response.access_control_allow_credentials = True
    response.headers.add("Access-Control-Allow-Origin", "https://localhost:8080")
    response.headers.add('Access-Control-Allow-Headers', "content-type")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response