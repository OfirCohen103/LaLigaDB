import sqlite3
import requests

url_address2="https://apim.laliga.com/webview/api/web/matches/%s/%s"

HEADERS2={
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

conn=sqlite3.connect("footballDB.db")
cursor_teams=conn.execute("SELECT SLUG, API_ID FROM TEAMS")
for row in cursor_teams:
    url_to_send = url_address_for_matches % (row[0])
    data = requests.get(url_to_send, headers=HEADERS_FOR_MATCHES).json()
    match_ids = []
    for e in data["matches"]:
        match_ids.append(e["id"])
    goal_scorers={}
    team_id=row[1]
    for c in match_ids:
        team_score=0
        enemy_score=0
        url_to_send=url_address2 % (str(c), "events")
        data=requests.get(url_to_send, headers=HEADERS2).json()
        for e in data["match_events"]:
            important_flag = False
            if e["match_event_kind"]["collection"] == "goal":
                #print(e["lineup"]["person"]["name"])
                if team_score==enemy_score or enemy_score-team_score==1:
                    important_flag=True
                if e["match_event_kind"]["id"]==3:
                    is_own_goal=True
                else:
                    is_own_goal=False
                if (e["lineup"]["team"]["id"] == team_id and not(is_own_goal)) or (e["lineup"]["team"]["id"] != team_id and is_own_goal):
                    team_score+=1
                    if is_own_goal:
                        name="Own Goal"
                    else:
                        name=e["lineup"]["person"]["nickname"]
                    if name in goal_scorers:
                        goal_scorers[name][2] += 1
                    else:
                        goal_scorers[name] = [team_id,name,1, 0]
                    if important_flag:
                        goal_scorers[name][3] += 1
                        """if name in important_scorers:
                            important_scorers[name] += 1
                        else:
                            important_scorers[name] = 1"""
                else:
                    enemy_score+=1
    conn.executemany("INSERT INTO STATS (TEAM_ID, NAME, GOALS, IMPORTANT) VALUES (?,?,?,?)", (dict(sorted(goal_scorers.items()))).values())
    print("added")
    goal_scorers.clear()
conn.commit()
conn.close()
