#! /usr/bin/python3

import requests
import os
import sys

def grab(line):
    try:
        _id = line.split('/')[4]
        s = requests.Session()
        response = s.get(f'https://www.dailymotion.com/player/metadata/video/{_id}').json()['qualities']['auto'][0]['url']
        m3u = s.get(response).text
        m3u = m3u.strip().split('\n')[1:]
        d = {}
        cnd = True
        for item in m3u:
            if cnd:
                resolution = item.strip().split(',')[2].split('=')[1]
                if resolution not in d:
                    d[resolution] = []
            else:
                d[resolution]= item
            cnd = not cnd
        m3u = d[max(d, key=int)]    
    except Exception as e:
        m3u = 'https://raw.githubusercontent.com/naveenland4/UTLive/main/assets/info.m3u8'
    finally:
        print(m3u)

def get_m3u8(channel_name:str):
    print('#EXTM3U')
    print('#EXT-X-VERSION:3')
    print('#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000')
    try:
        with open(f'../channels/{channel_name}.txt') as f:
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
        print("Usage: python dailymotion.py <channel_name from txt file>")
    else:
        get_m3u8(sys.argv[1])