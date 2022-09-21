url_address_for_goals="https://apim.laliga.com/webview/api/web/matches/%s/%s"

HEADERS_FOR_GOALS={
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Language': 'en',
    'Country-Code': 'GB',
    'Host': 'apim.laliga.com',
    'Ocp-Apim-Subscription-Key': 'ee7fcd5c543f4485ba2a48856fc7ece9',
    'Origin': 'https://www.laliga.com',
    'Referer': 'https://www.laliga.com/',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

url_address_for_matches="https://apim.laliga.com/public-service/api/v1/matches?seasonYear=2021&teamSlug=%s&limit=100&status=played&orderField=date&orderType=asc"

HEADERS_FOR_MATCHES={
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Language': 'en',
    'Country-Code': 'GB',
    'Host': 'apim.laliga.com',
    'If-Modified-Since': 'Fri, 26 Aug 2022 22:32:17 GMT',
    'Ocp-Apim-Subscription-Key': 'c13c3a8e2f6b46da9c5c425cf61fab3e',
    'Origin': 'https://www.laliga.com',
    'Referer': 'https://www.laliga.com/',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
url_address_for_teams="https://apim.laliga.com/public-service/api/v1/teams?subscriptionSlug=laliga-santander-2021&limit=99&offset=0&orderField=nickname&orderType=ASC"
HEADERS_FOR_TEAMS={
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Language': 'en',
    'Country-Code': 'GB',
    'Ocp-Apim-Subscription-Key': 'c13c3a8e2f6b46da9c5c425cf61fab3e',
    'Origin': 'https://www.laliga.com',
    'Referer': 'https://www.laliga.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}