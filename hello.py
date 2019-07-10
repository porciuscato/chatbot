import webbrowser

url="https://search.daum.net/search?&q=" # q = 뒤에 원하는 키워드를 넣으면 됨
keywords=["사나","나연","쯔위"]
for name in keywords:
    webbrowser.open(url+name)