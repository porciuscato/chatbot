import requests
import bs4 

url_3="https://www.naver.com/"
response_3 = requests.get(url_3).text
document_3 = bs4.BeautifulSoup(response_3,'html.parser')
favorite1 = document_3.select_one('ul.ah_l:nth-child(5) > li:nth-child(1) > a:nth-child(1) > span:nth-child(2)').text
favorite2 = document_3.select_one('ul.ah_l:nth-child(5) > li:nth-child(2) > a:nth-child(1) > span:nth-child(2)').text

for i in range(1,11):
    print("실시간 검색어 {}위는 {}".format(i,document_3.select_one('ul.ah_l:nth-child(5) > li:nth-child({}) > a:nth-child(1) > span:nth-child(2)'.format(i)).text))

favorite1 = document_3.select('ul.ah_l:nth-child(5) > li:nth-child(1) > a:nth-child(1) > span:nth-child(2)').text

print(favorite1)