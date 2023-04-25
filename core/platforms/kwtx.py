import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Referer': 'https://www.kwtx.com/livestream/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

response = requests.get(
    'https://www.kwtx.com/pf/api/v3/content/fetch/syncbak-get-tokens?query=%7B%22deviceId%22:%22GcayU0vxF35EwubIAcrCzoiN4fDbrQI55uytQ0R4JpxKYtXHbK%22,%22queryString%22:%22%7B%5C%22query%5C%22:%5C%22+query+GrayWebAppsDefaultData+($expirationSeconds:+Int,+$vodCount:+Int)%7B+liveChannels+%7B+id+title+description+callsign+listImages+%7B+type+url+size+%7D+posterImages+%7B+type+url+size+%7D+isNew+type+status+onNow+%7B+id+title+description+episodeTitle+tvRating+startTime+endTime+duration+isLooped+isOffAir+airDate%7D+onNext+%7B+id+title+description+episodeTitle+tvRating+startTime+endTime+duration+isLooped+isOffAir+airDate%7D+isNielsenEnabled+isClosedCaptionEnabled+location+networkAffiliation+%7D+firstLiveChannel:+liveChannels(first:1)+%7B+id+title+description+callsign+listImages+%7B+type+url+size+%7D+posterImages+%7B+type+url+size+%7D+isNew+type+status+onNow+%7B+id+title+description+episodeTitle+tvRating+startTime+endTime+duration+isLooped+isOffAir+airDate%7D+onNext+%7B+id+title+description+episodeTitle+tvRating+startTime+endTime+duration+isLooped+isOffAir+airDate%7D+isNielsenEnabled+isClosedCaptionEnabled+location+networkAffiliation+streamUrl(expiresIn:+$expirationSeconds)+%7D+videoOnDemand+(first:+$vodCount)%7B+id+title+description+duration+airDate+listImages+%7B+type+url+size+%7D+posterImages+%7B+type+url+size+%7D+%7D+%7D%5C%22,%5C%22variables%5C%22:%7B%5C%22expirationSeconds%5C%22:300,%5C%22vodCount%5C%22:12%7D%7D%22%7D&_website=kwtx',
    headers=headers,
).json()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json',
    'api-token': response["apiToken"],
    'query-signature-token': response["querySignatureToken"],
    'Origin': 'https://www.kwtx.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.kwtx.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
}

data = '{"query":" query GrayWebAppsDefaultData ($expirationSeconds: Int, $vodCount: Int){ liveChannels { id title description callsign listImages { type url size } posterImages { type url size } isNew type status onNow { id title description episodeTitle tvRating startTime endTime duration isLooped isOffAir airDate} onNext { id title description episodeTitle tvRating startTime endTime duration isLooped isOffAir airDate} isNielsenEnabled isClosedCaptionEnabled location networkAffiliation } firstLiveChannel: liveChannels(first:1) { id title description callsign listImages { type url size } posterImages { type url size } isNew type status onNow { id title description episodeTitle tvRating startTime endTime duration isLooped isOffAir airDate} onNext { id title description episodeTitle tvRating startTime endTime duration isLooped isOffAir airDate} isNielsenEnabled isClosedCaptionEnabled location networkAffiliation streamUrl(expiresIn: $expirationSeconds) } videoOnDemand (first: $vodCount){ id title description duration airDate listImages { type url size } posterImages { type url size } } }","variables":{"expirationSeconds":86400,"vodCount":12}}'
response = requests.post('https://graphql-api.aws.syncbak.com/graphql', headers=headers, data=data)

print("#EXTM3U\n#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58\n#EXTVLCOPT:http-referrer=https://www.kwtx.com/")
print(response.json())
#print(response.json()["data"]["firstLiveChannel"][0]["streamUrl"])
