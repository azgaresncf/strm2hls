#! /usr/bin/python3

import requests
import os
import sys

def grab(stream):
    try:
        _id = stream.split('/')[4]
        s = requests.Session()
        response = s.get(f'https://www.dailymotion.com/player/metadata/video/{_id}').json()['qualities']['auto'][0]['url']
        m3u = s.get(response).text
        print(m3u)
    except Exception as e:
        m3u = 'https://raw.githubusercontent.com/naveenland4/UTLive/main/assets/info.m3u8'

def get_m3u8(streamlink:str):
    try:
        with open(f'../channels/{streamlink}.txt') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('~~'):
                    continue
                if not line.startswith('https:'):
                    line = line.split('|')
                    ch_name = line[0].strip()
                    grp_title = line[1].strip().title()
                    tvg_logo = line[2].strip()
                    tvg_id = line[3].strip()
                else:
                    grab(line)
    except:
        raise FileNotFoundError("Your channel file don't exist!")    
        
    if 'temp.txt' in os.listdir():
        os.remove('temp.txt')
        os.remove('watch*')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python dailymotion.py stream")
    else:
        get_m3u8(sys.argv[1])