# encoing = utf-8

from urllib import request
import json, base64, uuid, os
import wave
import pycurl
import io

#melo的微博
bda_app_id = "9271146"
bda_api_key = "OGnSaG5CXm46jORUkxylquWd"
bda_secret_key = "dbc1368d5e12d4bdeb22bc4029963872"

bda_access_token = ""
bda_expires_in = ""
ret_text = ""

def get_mac_address():
    return uuid.UUID(int=uuid.getnode()).hex[-12:]

def get_access_token():
    url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=ZrjLfF5Rh7pOL66gaOmDGnXn&client_secret=16bac9645093ca2632ebb81015ff7544"

    req = request.Request(url, method="POST")
    resp = request.urlopen(req)
    data = resp.read().decode('utf-8')
    json_data = json.loads(data)

    global bda_access_token
    bda_access_token = json_data['access_token']

    return bda_access_token

CHUNK = 1024
def get_wav_data(wav_path):
    if wav_path is None or len(wav_path) == 0:
        return None

    fp = wave.open(wav_path, 'rb')
    nf = fp.getnframes()
    f_len = nf * 2
    audio_data = fp.readframes(nf)

    return audio_data, f_len

def dump_res(buf):
    resp_json = json.loads(buf.decode('utf-8'))
    print('request api ing...\n')
    print(resp_json)
    print('\n')
    
    try:
        ret = resp_json['result']
    except:
        ret = ['谷歌地图作为错误备用']

    global ret_text
    ret_text = ret[0]
    #print(buf)

def wav_to_text(wav_path):
    if wav_path is None or len(wav_path) == 0:
        return None

    if len(bda_access_token) == 0:
        get_access_token()
        if len(bda_access_token) == 0:
            return None

    data, f_len = get_wav_data(wav_path)

    url = 'http://vop.baidu.com/server_api?cuid=' + get_mac_address() + '&token=' + bda_access_token
    http_header = [
        'Content-Type: audio/pcm; rate=8000',
        'Content-Length: %d' % f_len
    ]

    c = pycurl.Curl()
    c.setopt(pycurl.URL, str(url)) #curl doesn't support unicode
    #c.setopt(c.RETURNTRANSFER, 1)
    c.setopt(c.HTTPHEADER, http_header)   #must be list, not dict
    c.setopt(c.POST, 1)
    c.setopt(c.CONNECTTIMEOUT, 30)
    c.setopt(c.TIMEOUT, 30)
    c.setopt(c.WRITEFUNCTION, dump_res)
    c.setopt(c.POSTFIELDS, data)
    c.setopt(c.POSTFIELDSIZE, f_len)
    c.perform() #pycurl.perform() has no return val

    return ret_text