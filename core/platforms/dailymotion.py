#!/usr/bin/python3
import requests
import sys

def get_dailymotion_streams(video_id: str):
    """
    Retrieves Dailymotion streams based on the video ID.

    Args:
        video_id (str): The ID of the Dailymotion video.

    Returns:
        None

    Raises:
        Exception: If an error occurs while retrieving the streams.
    """
    try:
        url = f'https://www.dailymotion.com/player/metadata/video/{video_id}'
        response = requests.get(url).json()
        stream_url = response['qualities']['auto'][0]['url']
        m3u = requests.get(stream_url).text
        print(m3u)
    except Exception as e:
        m3u = 'https://raw.githubusercontent.com/naveenland4/UTLive/main/assets/info.m3u8'
        print(m3u)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python dailymotion.py stream")
    else:
        video_id = sys.argv[1]
        get_dailymotion_streams(video_id)
