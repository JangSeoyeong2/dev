import requests as rq
from bs4 import BeautifulSoup

keyword = input('검색어를 입력하세요: ')
max_page = int(input('출력할 페이지 수를 입력하세요: '))
pageNum = 0
for articleNum in range(1,50,10): #1, 11, 21, 33... 
    pageNum += 1
    url = f"https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EB%8F%99%EC%84%9C%EB%8C%80%ED%95%99%EA%B5%90&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=49&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&{keyword}start={articleNum}"
    print(f'======================{pageNum}페이지====================')
    res = rq.get(url)
    html = res.text
    soup  = BeautifulSoup(html)

    word = soup.select('.news_tit')

    for item in word:
        title = item.text
        link = item.attrs['href']
        print(title,link)