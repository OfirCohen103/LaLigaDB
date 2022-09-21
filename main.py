# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sqlite3
import json
import requests
from flask import Flask, render_template,jsonify, request
from flask_cors import CORS,cross_origin
#from bs4 import BeautifulSoup
#import json
import APIHandler as Handler


app=Flask(__name__)
CORS(app)

@app.route("/teamsDB", methods=['POST'])
def get_teams_db():
    conn=sqlite3.connect("database/footballDB.db")
    cursor=conn.execute("SELECT * from TEAMS")
    teams=cursor.fetchall()
    conn.close()
    return json.dumps(teams)

@app.route("/statsDB", methods=['POST'])
def get_stats_db():
    team = request.get_json()
    team = json.loads(team)
    conn=sqlite3.connect("database/footballDB.db")
    cursor=conn.execute("SELECT s.NAME, s.GOALS, s.IMPORTANT FROM STATS s INNER JOIN TEAMS t ON s.TEAM_ID = t.API_ID WHERE t.NAME=?",(team,))
    stats=cursor.fetchall()
    conn.close()
    return render_template("indexDB.html",response=stats)

@app.route("/teams", methods=['POST'])
def get_teams():
    url_to_send=Handler.url_address_for_teams
    data=requests.get(url_to_send,headers=Handler.HEADERS_FOR_TEAMS).json()
    team_keys={}
    for i, e in enumerate(data["teams"]):
        #print ("for "+e["nickname"]+" type "+str(i))
        #team_keys[i]=[e["slug"], e["id"]]
        team_keys[i]=[e["slug"], e["nickname"], e["id"]]
    return json.dumps(team_keys)

@app.route("/stats", methods=['POST'])
def get_stats():
    s=request.get_json()
    s=json.loads(s)
    print(s[3])
    #url_to_send=url_address_for_matches % (team_keys[int(s)][0])
    url_to_send = Handler.url_address_for_matches % (s[1])
    data=requests.get(url_to_send,headers=Handler.HEADERS_FOR_MATCHES).json()
    match_ids=[]
    for e in data["matches"]:
        match_ids.append(e["id"])
    goal_scorers={}
    #important_scorers={}
    #team_id=team_keys[int(s)][1]
    team_id = s[3]
    for c in match_ids:
        team_score=0
        enemy_score=0
        url_to_send=Handler.url_address_for_goals % (str(c), "events")
        data=requests.get(url_to_send, headers=Handler.HEADERS_FOR_GOALS).json()
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
                        goal_scorers[name][0] += 1
                    else:
                        goal_scorers[name] = [1, 0]
                    if important_flag:
                        goal_scorers[name][1] += 1
                        """if name in important_scorers:
                            important_scorers[name] += 1
                        else:
                            important_scorers[name] = 1"""
                else:
                    enemy_score+=1
    """print (dict(sorted(goal_scorers.items())))
    print (dict(sorted(important_scorers.items())))"""
    print ("finished")
    response=[]
    response.append(dict(sorted(goal_scorers.items())))
    #response.append(dict(sorted(important_scorers.items())))
    #return json.dumps(response,ensure_ascii=False)
    return render_template('index.html',response=response)

    #print(data["match_events"][0]["match_event_kind"]["collection"])
    #soup=BeautifulSoup(data["content"]["html"],'html.parser')
    #print(soup.prettify())
# Press the green button in the gutter to run the script.

if __name__=="__main__":
    app.run()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
