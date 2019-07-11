from flask import Flask, render_template, request
from faker import Faker
import random
import requests
from bs4 import BeautifulSoup


fake = Faker('ko_KR')
app=Flask(__name__)
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/pastlife')
def pastlife():
    return render_template("pastlife.html")

dic_name={}

@app.route('/result')
def result():
    # 이름과 직업을 알려준다.
    job=fake.job()
    # flask가 가지고 있는 메소드
    # args : argumenets 
    name = request.args.get('name')
    # 같은 이름이면 같은 값이 나오도록 저장하려면 딕셔너리를 활용
    if name in dic_name:
        return render_template('result.html',job=dic_name[name],name=name)
    else :
        dic_name[name]=job
        return render_template('result.html',job=job,name=name)


@app.route('/goonghap')
def goonghap():
    return render_template('goonghap.html')

babos={}

@app.route('/destiny')
def destiny():
    # 두 사람의 이름을 받는다.
    babo=request.args.get('babo')
    you=request.args.get('you')
    # 바보의 이름이 딕셔너리에 있는지 확인한다
    if babo in babos:
        # 있으면 바보 딕셔너리 안에 you가 있는지 확인한다
        if you in babos[babo]:
            return render_template('destiny.html',babo=babo,you=you,hap=babos[babo][you])
        # 없으면 딕셔너리에 추가한다
        else : 
            #babos[babo][you]=random.choice(range(51,101))
            babos[babo][you]=random.randint(51,101)
            return render_template('destiny.html',babo=babo,you=you,hap=babos[babo][you])
    # 없으면 바보 딕셔너리 you 딕셔너리 안에 숫자를 추가한다.
    else :
        babos[babo]={you:random.choice(range(51,101))}
        return render_template('destiny.html',babo=babo,you=you,hap=babos[babo][you])
    

#babos에 있는 사람들 모두 출력하기
@app.route('/admin')
def admin():
    babos_list=[]
    # 속은 사람들의 명단을 보여준다.
    for name in babos:
        babos_list.append(name)
    return render_template('admin.html',result=babos_list)

@app.route('/opgg')
def opgg():
    return render_template('opgg.html')

# https://www.op.gg/summoner/

@app.route('/history')
def history():
    name=request.args.get('user')
    url = f"https://www.op.gg/summoner/userName={name}"
    response = requests.get(url).text
    bs4_res=BeautifulSoup(response,'html.parser')
    win = bs4_res.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins")
    win_count=win.text[:-1]
    lose = bs4_res.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses")
    lose_count = lose.text[:-1]

    return render_template('history.html',id=name,win=win_count,lose=lose_count)


if __name__=='__main__':
    app.run(debug=True)