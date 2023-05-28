import sys
import streamlink

def get_twitch_streams(channel_url):
    streams = {}
    plugins = streamlink.streams(channel_url)

    for plugin in plugins:
        streams[plugin] = plugins[plugin].url

    return streams

def convert_to_m3u8(streams):
    m3u8_content = "#EXTM3U\n"

    for plugin, url in streams.items():
        m3u8_content += f"#EXTINF:-1,{plugin}\n{url}\n"

    return m3u8_content

def twitch_streams_to_m3u8(channel_url):
    twitch_streams = get_twitch_streams(channel_url)
    m3u8_content = convert_to_m3u8(twitch_streams)
    return m3u8_content

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python twitch_streams.py [Twitch_Channel_URL]")
    else:
        channel_url = sys.argv[1]
        m3u8_content = twitch_streams_to_m3u8(channel_url)
        print(m3u8_content)
