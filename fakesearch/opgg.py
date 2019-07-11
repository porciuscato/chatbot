# 1. op.gg에 요청을 보낸다.
import requests
from bs4 import BeautifulSoup
url="https://www.op.gg/summoner/userName=cuzz"
response = requests.get(url).text
bs_res=BeautifulSoup(response,"html.parser")
win = bs_res.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins")
print(win.text.replace("W","승"))


# 2. html 응답을 받아
# 3. html 안의 정보를 출력