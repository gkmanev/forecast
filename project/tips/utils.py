import json
import requests
from django.conf import settings
from datetime import datetime,tzinfo,timedelta
from datetime import date
import pytz
from pytz import timezone
from django.conf import settings
from tips.models import OverTwoAndHalf,Btts

#Fixtures

url = "https://soccer-football-info.p.rapidapi.com/matches/day/full/"
    
headers = {"x-rapidapi-host": "soccer-football-info.p.rapidapi.com", "x-rapidapi-key": "66dcbafb75msha536f3086b06788p1f5e7ajsnac1315877f0f"}

def make_bet_url(str):
    test = str.split("EXT")
    part_one = test[0]+"com"
    part_two = test[1]
    link = part_one+part_two
    return link


def parse_date(date_str):    
    date_part = date_str.split(" ")[0]
    time_part = date_str.split(" ")[1]
    y = int(date_part.split("-")[0])
    m = int(date_part.split("-")[1])
    d = int(date_part.split("-")[2])
    h = int(time_part.split(":")[0])
    min = int(time_part.split(":")[1])    
    game_time = datetime(y, m, d, h, min, 0, tzinfo=pytz.utc)
    return game_time


def get_pagination(today):
        
    querystring = {"d":today,"p":"1","l":"en_US"}
    
    r = requests.get(url,headers=headers,params=querystring)
    page_content = r.text
    
    probably_json = page_content.replace("\\'", "'")
    # now we load the json
    feed = json.loads(probably_json) 
    
     
    if feed: 
        pagin = feed.get("pagination", None)
    if pagin:
        
        items_num = int(feed['pagination'][0]["items"])
        per_page = int(feed["pagination"][0]['per_page'])
        pagination = int(items_num/per_page)    
        return pagination


def get_data():
        
    today = str(date.today())
    today = today.split("-")
    today_new = today[0]+today[1]+today[2]
    
    pages = get_pagination(today_new)
    
    if pages:  
        
        for n in range(1, pages+2):
            querystring = {"d":today_new,"l":"en_US"}
            querystring["p"] = n           
            req = requests.get(url,headers=headers,params=querystring)
            content = req.text
            json_data = content.replace("\\'", "'")
            data_feed = json.loads(json_data)    
            if data_feed:
                fixt = data_feed.get('result',None)   
                if fixt:                  
                    fixtures = data_feed['result']
                    for gem in fixtures:  
                        teamA = gem["teamA"]["name"]
                        teamB = gem["teamB"]["name"]
                        game_date = gem["date"]
                        championship = gem["championship"]["name"]
                        bet_url = gem.get("bet365_url", None)
                        #if gem['status'] == "NOT_STARTED":                
                        perfA = gem["teamA"].get("perf",None)
                        perfB = gem["teamB"].get("perf",None)
                        if perfA and perfB:
                            
                            if bet_url:
                                url_365 = make_bet_url(bet_url)
                            else:
                                url_365 = ""
                            start_time = parse_date(game_date)
            
                            bttsA = gem["teamA"]["perf"].get("btts", None)
                            bttsB = gem["teamB"]["perf"].get("btts", None)
                            if bttsA and bttsB:
                                bttsA = float(gem["teamA"]["perf"]["btts"])
                                bttsB = float(gem["teamB"]["perf"]["btts"]) 
                                Btts.objects.get_or_create(homeTeam = teamA, awayTeam = teamB, startTime = start_time, btts_a = bttsA, btts_b = bttsB, championship = championship, bet_url = url_365 )
                                                                   
                
                            avgA = gem['teamA']['perf']['o_2_5_game']
                            avgB = gem['teamB']['perf']['o_2_5_game']    
                            if avgA and avgB:
                                avgA = float(avgA)
                                avgB = float(avgB)                    
                         
                                OverTwoAndHalf.objects.get_or_create(homeTeam = teamA, awayTeam = teamB, startTime = start_time, home_over_percentage = avgA, away_over_percentage = avgB, championship = championship, bet_url = url_365 )
                                if bet_url:
                                    print(teamA+"||"+teamB+"||"+str(start_time)+"||"+str(avgA)+"||"+str(avgB)+"||"+championship+"|||"+bet_url)
                             
                          
                                
                            