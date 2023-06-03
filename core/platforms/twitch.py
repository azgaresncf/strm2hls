import sys
import requests
import json

def get_access_token(channel_name:str):
    """
    Retrieves the access token and signature required to access the stream.

    Args:
        channel_name (str): The name of the Twitch channel.

    Returns:
        tuple or None: A tuple containing the access token and signature if successful, or None if an error occurred.
    """
    url = "https://gql.twitch.tv/gql"
    headers = {
        'Client-ID': 'ue6666qo983tsx6so1t0vnawi233wa', #shoutout to streamlink
        'Content-Type': 'application/json'
    }

    payload = {
        "operationName": "PlaybackAccessToken",
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "0828119ded1c13477966434e15800ff57ddacf13ba1911c129dc2200705b0712"
            }
        },
        "variables": {
            "isLive": True,
            "login": channel_name,
            "isVod": False,
            "vodID": "",
            "playerType": "embed"
        }
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response_data = response.json()
        token = response_data["data"]["streamPlaybackAccessToken"]["value"]
        sig = response_data["data"]["streamPlaybackAccessToken"]["signature"]
        return token, sig
    except (requests.RequestException, KeyError, json.JSONDecodeError) as e:
        print("An error occurred while retrieving the access token:", e)
        return None, None

def get_stream_url(channel_name: str):
    """
    Retrieves the URL of the stream for the given Twitch channel.

    Args:
        channel_name (str): The name of the Twitch channel.

    Returns:
        str or None: The URL of the stream if successful, or None if an error occurred.
    """
    token, sig = get_access_token(channel_name)

    if not token or not sig:
        return None

    url = f"https://usher.ttvnw.net/api/channel/hls/{channel_name}.m3u8?token={token}&sig={sig}"

    try:
        response = requests.get(url)
        cleaned_response = remove_twitch_info_headers(response.text)
        return cleaned_response
    except requests.RequestException as e:
        print("An error occurred while retrieving the stream URL:", e)
        return None

def remove_twitch_info_headers(response_text: str):
    """
    Removes the Twitch-specific headers from the stream URL response.

    Args:
        response_text (str): The response text containing the stream URL.

    Returns:
        str: The cleaned stream URL without Twitch-specific headers.
    """
    lines = response_text.split("\n")
    cleaned_lines = [line for line in lines if not line.startswith("#EXT-X-TWITCH-INFO") and not line.startswith("#EXT-X-MEDIA")]
    cleaned_response = "\n".join(cleaned_lines)
    return cleaned_response

def main():
    """
    The main function that is executed when the script is run.
    """
    if len(sys.argv) < 2:
        print("Usage: python script.py <channel_name>")
        return

    channel_name = sys.argv[1]

    stream_url = get_stream_url(channel_name)

    if stream_url:
        print(stream_url)

if __name__ == "__main__":
    main()
