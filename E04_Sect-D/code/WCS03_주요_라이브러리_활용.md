
# Industry 4.0 의 중심, BigData

<div align='right'><font size=2 color='gray'>Data Processing Based Python @ <font color='blue'><a href='https://www.facebook.com/jskim.kr'>FB / jskim.kr</a></font>, [김진수](bigpycraft@gmail.com)</font></div>
<hr>

## <font color='#AA3333'>TextBook. 파이썬을 이용한 웹크롤링과 스크레이핑 </font>
> <font color='#AA3333'>데이터 수집과 분석을 위한 실전 가이드
<br/>
<font color='#CC5555'>
<b>INDEX. </b>
<br/>
<select name="index">
    <option value="CH00"> 파이썬을 이용한 웹크롤링과 스크레이핑, 데이터 수집과 분석을 위한 실전 가이드 </option>
    <option value="CH00"> ------------------------------------------------------------------------------------------------------------------ </option>
    <option value="CH01"> 01.크롤링과 스크레이핑이란?                      </option>
    <option value="CH02"> 02.파이썬으로 시작하는 크롤링/스크레이핑         </option>
    <option value="CH03" selected> 03.주요 라이브러리 활용                          </option>
    <option value="CH04"> 04.크롤러를 사용할 때 기억해야 하는 것           </option>
    <option value="CH05"> 05.크롤링/스크레이핑 실전과 데이터 활용          </option>
    <option value="CH06"> 06.Scrapy 프레임워크                             </option>
    <option value="CH07"> 07.크롤러의 지속적 운용과 관리                   </option>
</select>
<br/><br/>
<b>APPENDIX </b>
<br/>
<select name="appendix">
    <option value="A00"> 부록: 베이그런트로 개발 환경 구축하기 </option>
    <option value="A00"> ------------------------------------------------------------------------------------------------------------------ </option>
    <option value="A01"> A.1 버추얼박스와 베이그런트             </option>
    <option value="A02"> A.2 CPU 가상화 지원 기능 활성화하기     </option>
    <option value="A03"> A.3 버추얼박스 설치하기                 </option>
    <option value="A04"> A.4 베이그런트 설치하기                 </option>
    <option value="A05"> A.5 가상 머신 실행하기                  </option>
    <option value="A06"> A.6 게스트 OS에 SSH 접속하기            </option>
    <option value="A07"> A.7 리눅스 기본 조작                    </option>
    <option value="A07"> A.8 베이그런트의 가상 머신 조작 명령어  </option>
</select>

<br/>
<hr>

## <font color='#0000AA'>주요 라이브러리 활용 </font>
>   
<font color='#0000CC'>
- 라이브러리 설치
- 웹 페이지 간단하게 추출
- HTML 스크레이핑
- RSS 스크레이핑하기
- 데이터베이스에 저장
- 크롤러와 URL
- 파이썬으로 크롤러 만들기

<hr>
### <font color='#0000CC'> 라이브러리 설치 </font>
> 
- pip 설치
<br/>(venv) C:\\> pip install &lt;module_name&gt;
<br/>(venv) C:\\> pip install &lt;module_name&gt;=1.0
<br/>(venv) C:\\> pip freeze

<hr>
### <font color='#0000CC'> 웹 페이지 간단하게 추출 </font>
>  urllib.Request : GET, POST 요청 처리
- get(), post(), put(), delete(), head(), option()
- 위 함수는 ** HTTP 메소드 **  GET, POST, PUT, DELETE, HEAD, OPTIONS 에 대응


<hr>
### <font color='#0000CC'>  HTML 스크레이핑 </font>
> 
- HTML 요소를 지정하는 방식 : XPath / CSS 선택자
- lxml 스크래이핑 : C언어로 작성된 XML 처리와 관련된 libxml2와 libxslt의 파이썬 바인딩
- BeautifuSoup 스크래이핑 : 아주 쉽고 간단한 공개 API (cf. Current Version : BeautifulSoup4 since 2012)
- pyquery 스크래이핑 : jQuery와 같은 사용법으로 HTML에서 스크래이핑 할 수 있게 해주는 라이브러리


```python
! wget http://www.hanbit.co.kr/store/books/full_book_list.html -O ./data/full_book_list.html
```

#### <font color='#0000FF'> c3-01_scrape_by_lxml </font>
> lxml 로 스크레이핑


```python
import lxml.html
import pandas as pd

# HTML 파일을 읽어 들이고, getroot() 메서드로 HtmlElement 객체를 생성합니다.
tree = lxml.html.parse('./data/full_book_list.html')
html = tree.getroot()

A_Tag_Text = []
A_Tag_Link = []

# cssselect() 메서드로 a 요소의 리스트를 추출하고 반복을 돌립니다.
for a in html.cssselect('a'):
    # href 속성과 글자를 추출합니다.
    # print(a.get('href'), a.text)
    
    if a.text is not None:
        A_Tag_Text.append(a.text)
        A_Tag_Link.append(a.get('href'))

book_df = pd.DataFrame({'Text' : A_Tag_Text, 
                        'Link' : A_Tag_Link},
                      columns = ['Text', 'Link'])
book_df.head(10)
```

#### <font color="#0000FF"> c3-02_scrape_by_bs4 </font>
> BeautifulSopu 로 스크래이핑


```python
# encoding type 확인 : <meta charset=''> 정보
# ! type data\full_book_list.html
```


```python
from bs4 import BeautifulSoup
import pandas as pd

# HTML 파일을 읽어 들이고 BeautifulSoup 객체를 생성합니다.
with open('data/full_book_list.html', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

category_tag = soup.find('ul', 'lnb_depth1_category')

# find_all() 메서드로 a 요소를 추출하고 반복을 돌립니다.
for a_tag in category_tag.find_all('a'):
    if len(a_tag['href']) > 1:
        print("href 속성 : {} \t, 글자 : {}, ".format(a_tag['href'], a_tag.text))
```

<hr>
### <font color='#0000CC'> RSS 스크레이핑 </font>
> 
- feedparser 모듈 사용
- 표준 라이브러리인 ElementTree보다 간단한 방법으로 RSS 피드에서 데이터 추출 가능

#### <font color="#0000FF"> c3-03_scrape_by_feedparser </font>
> feedparser 로 RSS 스크래이핑
- 모듈설치 : pip install feedparser


```python
# ! pip install feedparser
```


```python
import feedparser
import pandas as pd

Title = []
Link  = [] 

# 알라딘 도서 RSS를 읽어 들입니다.
d = feedparser.parse('http://www.aladin.co.kr/rss/special_new/351')

# 항목을 순회합니다.
for entry in d.entries:
    Title.append(entry.title)
    Link.append(entry.link)
    
    # print('제목:', entry.title)
    # print('링크:', entry.link)
    # print()
    
rss_df = pd.DataFrame({'제목': Title, '링크':Link}, columns=['제목', '링크'])
```


```python
rss_df.head(10)
```


```python
d = feedparser.parse('http://www.aladin.co.kr/rss/special_new/351')
type(d), len(d.entries)
```


```python
entry = d.entries[0]
entry
```


```python
entry.keys()
```


```python
entry.title
```


```python
entry.link
```


```python
entry.tags
```


```python
entry.tags[0]['term']
```

<hr>
### <font color='#0000CC'> 데이터베이스에 저장 </font>
> 
- MySQL
- MongoDB
<!--
#### <font color="#0000FF"> MySQL 설치 

MySQL Install in Windows
-----------------------------------------------------------------------------------------------
1. 
http://oyeahhh.tistory.com/66

2.
https://www.popit.kr/mysql-%EC%84%A4%EC%B9%98-%EC%9C%88%EB%8F%84%EC%9A%B0-%ED%99%98%EA%B2%BD/


* Download : https://dev.mysql.com/downloads/
  - MySQL Community Server
  - MySQL Installer MSI
  - Windows (x86, 32-bit), MSI Installer	8.0.13	313.8M	

//-->
#### <font color="#0000FF"> c3-04_save_mysql </font>
> MySQL에 저장
- SQLite와 달리 클리이언트/서버형 아키텍처 채용
- 즉,  connection 객체 생성할 때, 사용자계정정보(ID/PW) 정보가 필요하다

``` python
import MySQLdb

# MySQL 서버에 접속하고 연결을 변수에 저장합니다.
# 사용자 이름과 비밀번호를 지정한 뒤 scraping 데이터베이스를 사용(USE)합니다.
# 접속에 사용할 문자 코드는 utf8mb4로 지정합니다.
conn = MySQLdb.connect(db='scraping', user='scraper', passwd='password', charset='utf8mb4')

# 커서를 추출합니다.
c = conn.cursor()

# execute() 메서드로 SQL 구문을 실행합니다.
# 스크립트를 여러 번 사용해도 같은 결과를 출력할 수 있게 cities 테이블이 존재하는 경우 제거합니다.
c.execute('DROP TABLE IF EXISTS cities')

# cities 테이블을 생성합니다.
c.execute('''
    CREATE TABLE cities (
        rank integer,
        city text,
        population integer
    )
''')

# execute() 메서드의 두 번째 매개변수에는 파라미터를 지정할 수 있습니다.
# SQL 내부에서 파라미터로 변경할 부분(플레이스홀더)은 %s로 지정합니다.
c.execute('INSERT INTO cities VALUES (%s, %s, %s)', (1, '상하이', 24150000))

# 파라미터가 딕셔너리일 때는 플레이스홀더를 %(<이름>)s 형태로 지정합니다.
c.execute('INSERT INTO cities VALUES (%(rank)s, %(city)s, %(population)s)',
          {'rank': 2, 'city': '카라치', 'population': 23500000})

# executemany() 메서드를 사용하면 여러 개의 파라미터를 리스트로 지정해서
# 여러 개(현재 예제에서는 3개)의 SQL 구문을 실행할 수 있습니다.
c.executemany('INSERT INTO cities VALUES (%(rank)s, %(city)s, %(population)s)', [
    {'rank': 3, 'city': '베이징', 'population': 21516000},
    {'rank': 4, 'city': '텐진', 'population': 14722100},
    {'rank': 5, 'city': '이스탄불', 'population': 14160467},
])

# 변경사항을 커밋(저장)합니다.
conn.commit() 

# 저장한 데이터를 추출합니다.
c.execute('SELECT * FROM cities')
# 쿼리의 결과는 fetchall() 메서드로 추출할 수 있습니다.
for row in c.fetchall():
    # 추출한 데이터를 출력합니다.
    print(row)

# 연결을 닫습니다.
conn.close()
```

<hr>

#### <font color="#0000FF"> MongoDB 개요 </font>
> ** NoSQL **의 일종, 문서형 데이터베이스
- 오픈소스 소프트웨어로 공개
- 유연한 데이터 구조, 높은 쓰기 성능, 사용하기 쉽다.
<br/><br/> 
- ** MongoDB의 데이터 구조 **
<br/> - 하나의 <u>데이터베이스</u>는 여러개의 콜렉션을 가지며,
<br/> - 하나의 <u>콜렉션</u>은 여러 개의 문서를 갖는다.
<br/> - <u>문서</u>는 **BSON** 이라고 부르는 **JSON의 바이너리 형식**으로 다룬다.
<br/> - 미리 데이터 구조를 정의할 필요없고, 문서마다 다른 데이터 구조를 가질 수 있다.

<!--
MongoDB 강의. 윈도우(Windows)에 MongoDB 설치하기
<br/><br/> http://solarisailab.com/archives/1605
//-->
#### <font color="#0000FF"> MongoDB 설치 </font>
> MongoDB Install in Windows
- Manual : https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/
- Download : https://www.mongodb.com/download-center/community?jmp=homepage

#### <font color="#0000FF"> MongoDB 실행 </font> 
> 설치 디렉토리 하단의 bin에서 mongod.exe, mongo.exe 실행
- mongod.exe : MongoDB 서버 실행파일 
- mongo.exe &nbsp; : MongoDB를 조작할수 있는 MongoDB Shell 프로그램
<br/> 
<hr/> - 먼저 MongoDB Shell을 실행하기 전에 MongoDB 서버를 실행시켜야 한다. 
<br/> - 탐색기에서 실행파일 Shift+우클릭을 통해 메뉴창을 연다. 
<br/> - 여기에서 명령창 열기(W)를 눌러서 현재 폴더에서 윈도우 명령프롬프트(cmd)를 실행한다.

#### <font color="#0000FF"> c3-05_save_mongo </font>
> MongoDB에 저장
- 파이썬 바인딩인 PyMongo 를 사용
- 모듈설치 : pip install pymongo


```python
# ! pip install pymongo
```

``` python
import lxml.html
from pymongo import MongoClient

# HTML 파일을 읽어 들이고 
# getroot() 메서드를 사용해 HtmlElement 객체를 추출합니다.
tree = lxml.html.parse('data/full_book_list.html')
html = tree.getroot()

client = MongoClient('localhost', 27017)
db = client.scraping   # scraping 데이터베이스를 추출합니다.
collection = db.links  # links 콜렉션을 추출합니다.

# 스크립트를 여러 번 사용해도 같은 결과를 출력할 수 있게 콜렉션의 문서를 제거합니다.
collection.delete_many({})

# cssselect() 메서드로 a 요소의 목록을 추출합니다.
for a in html.cssselect('a'):
    # href 속성과 링크의 글자를 추출해서 저장합니다.
    collection.insert_one({
        'url': a.get('href'),
        'title': a.text.strip(),
    })

# 콜렉션의 모든 문서를 _id 순서로 정렬해서 추출합니다.
for link in collection.find().sort('_id'):
    print(link['_id'], link['url'], link['title'])

```

<hr>

<hr>
### <font color='#0000CC'> 파이썬 크롤러 </font>
>  
- 목록 페이지에서 URL 목록 추출
- 상세페이지 스크레이핑
- 상세페이지 크롤링
- 스크레이핑 데이터 저장
- 최종 크롤러 생성


#### <font color="#0000FF"> c3-06_python_crawler_1 </font>
> 목록 페이지에서 URL 목록 추출(1)


```python
import requests
import lxml.html

response = requests.get('http://www.hanbit.co.kr/store/books/new_book_list.html')
root = lxml.html.fromstring(response.content)
for a in root.cssselect('.view_box a'):
    url = a.get('href')
    print(url)
```

#### <font color="#0000FF"> c3-07_python_crawler_2 </font>
> 목록 페이지에서 URL 목록 추출(2)


```python
import requests
import lxml.html

response = requests.get('http://www.hanbit.co.kr/store/books/new_book_list.html')
root = lxml.html.fromstring(response.content)

# 모든 링크를 절대 URL로 변환합니다.
root.make_links_absolute(response.url)

# 선택자를 추가해서 명확한 선택을 할 수 있게 합니다.
for a in root.cssselect('.view_box .book_tit a'):
    url = a.get('href')
    print(url)
```

#### <font color="#0000FF"> c3-08_python_crawler_3 </font>
> 목록 페이지에서 URL 목록 추출(3)


```python
import requests
import lxml.html

def main():
    """
    크롤러의 메인 처리
    """
    # 여러 페이지에서 크롤링할 것이므로 Session을 사용합니다.
    session = requests.Session()  
    
    # scrape_list_page() 함수를 호출해서 제너레이터를 추출합니다.
    response = session.get('http://www.hanbit.co.kr/store/books/new_book_list.html')
    urls = scrape_list_page(response)
    # 제너레이터는 list처럼 사용할 수 있습니다.
    for url in urls:
        print(url)

def scrape_list_page(response):
    root = lxml.html.fromstring(response.content)
    root.make_links_absolute(response.url)
    for a in root.cssselect('.view_box .book_tit a'):
        url = a.get('href')
        # yield 구문으로 제너레이터의 요소 반환
        yield url

if __name__ == '__main__':
    main()
```

#### <font color="#0000FF"> c3-09_python_crawler_4 </font>
> 상세페이지 스크레이핑(1)


```python
import requests
import lxml.html

def main():
    # 여러 페이지에서 크롤링할 것이므로 Session을 사용합니다.
    session = requests.Session()  
    response = session.get('http://www.hanbit.co.kr/store/books/new_book_list.html')
    urls = scrape_list_page(response)

    for url in urls:
        response = session.get(url)  # Session을 사용해 상세 페이지를 추출합니다.
        ebook = scrape_detail_page(response)  # 상세 페이지에서 상세 정보를 추출합니다.
        print(ebook)  # 책 관련 정보를 출력합니다.
        break  # 책 한 권이 제대로 되는지 확인하고 종료합니다.

def scrape_list_page(response):
    root = lxml.html.fromstring(response.content)
    root.make_links_absolute(response.url)
    for a in root.cssselect('.view_box .book_tit a'):
        url = a.get('href')
        yield url

def scrape_detail_page(response):
    """
    상세 페이지의 Response에서 책 정보를 dict로 추출합니다.
    """
    root = lxml.html.fromstring(response.content)
    ebook = {
        'url': response.url,
        'title': root.cssselect('.store_product_info_box h3')[0].text_content(),
        'price': root.cssselect('.pbr strong')[0].text_content(),
        'content': [p.text_content()\
            for p in root.cssselect('#tabs_3 .hanbit_edit_view p')]
    }
    return ebook

if __name__ == '__main__':
    main()
```

#### <font color="#0000FF"> c3-10_python_crawler_5 </font>
> 상세페이지 스크레이핑(2)

#### <font color='brown'> Regular Expression 관련 사이트
- <a href="http://regexr.com/"> Text 정보를 re로 테스트 </a>
- <a href="https://regexper.com/"> 작성된 re를 다이어그램으로 표현 </a>


```python
import requests
import lxml.html
import re

def main():
    # 여러 페이지에서 크롤링할 것이므로 Session을 사용합니다.
    session = requests.Session()  
    response = session.get('http://www.hanbit.co.kr/store/books/new_book_list.html')
    urls = scrape_list_page(response)
    for url in urls:
        response = session.get(url)  # Session을 사용해 상세 페이지를 추출합니다.
        ebook = scrape_detail_page(response)  # 상세 페이지에서 상세 정보를 추출합니다.
        print(ebook)  # 책 관련 정보를 출력합니다.
        break  # 책 한 권이 제대로 되는지 확인하고 종료합니다.

def scrape_list_page(response):
    root = lxml.html.fromstring(response.content)
    root.make_links_absolute(response.url)
    for a in root.cssselect('.view_box .book_tit a'):
        url = a.get('href')
        yield url

def scrape_detail_page(response):
    """
    상세 페이지의 Response에서 책 정보를 dict로 추출합니다.
    """
    root = lxml.html.fromstring(response.content)
    ebook = {
        'url': response.url,
        'title': root.cssselect('.store_product_info_box h3')[0].text_content(),
        'price': root.cssselect('.pbr strong')[0].text_content(),
        'content': [normalize_spaces(p.text_content())
            for p in root.cssselect('#tabs_3 .hanbit_edit_view p')
            if normalize_spaces(p.text_content()) != '']
    }
    return ebook

def normalize_spaces(s):
    """
    연결돼 있는 공백을 하나의 공백으로 변경합니다.
    """
    return re.sub(r'\s+', ' ', s).strip()

if __name__ == '__main__':
    main()
```

#### <font color="#0000FF"> c3-11_python_crawler_6 </font>
> 상세페이지 크롤링


```python
import time # time 모듈을 임포트합니다.
import re 
import requests
import lxml.html

def main():
    session = requests.Session()
    response = session.get('http://www.hanbit.co.kr/store/books/new_book_list.html')
    urls = scrape_list_page(response)
    for url in urls:
        time.sleep(1) # 1초 동안 휴식합니다.
        response = session.get(url)
        ebook = scrape_detail_page(response)
        print(ebook)

def scrape_list_page(response):
    root = lxml.html.fromstring(response.content)
    root.make_links_absolute(response.url)
    for a in root.cssselect('.view_box .book_tit a'):
        url = a.get('href')
        yield url

def scrape_detail_page(response):
    """
    상세 페이지의 Response에서 책 정보를 dict로 추출합니다.
    """
    root = lxml.html.fromstring(response.content)
    ebook = {
        'url': response.url,
        'title': root.cssselect('.store_product_info_box h3')[0].text_content(),
        'price': root.cssselect('.pbr strong')[0].text_content(),
        'content': [normalize_spaces(p.text_content())
            for p in root.cssselect('#tabs_3 .hanbit_edit_view p')
            if normalize_spaces(p.text_content()) != '']
    }
    return ebook

def normalize_spaces(s):
    """
    연결돼 있는 공백을 하나의 공백으로 변경합니다.
    """
    return re.sub(r'\s+', ' ', s).strip()

if __name__ == '__main__':
    main()
```

#### <font color="#0000FF"> c3-12_python_crawler_final </font>
> MongoDB 저장기능 추가한 최종적인 크롤러

``` python 
%%writefile  ./modules/python_crawler_final.py 

import time
import re 
import requests
import lxml.html
from pymongo import MongoClient

def main():
    """
    크롤러의 메인 처리
    """
    # 크롤러 호스트의 MongoDB에 접속합니다.
    client = MongoClient('localhost', 27017)
    
    # scraping 데이터베이스의 ebooks 콜렉션
    collection = client.scraping.ebooks 
    
    # 데이터를 식별할 수 있는 유일키를 저장할 key 필드에 인덱스를 생성합니다.
    collection.create_index('key', unique=True)

    # 목록 페이지를 추출합니다.
    response = requests.get('http://www.hanbit.co.kr/store/books/new_book_list.html')
    
    # 상세 페이지의 URL 목록을 추출합니다.
    urls = scrape_list_page(response)
    for url in urls:
        # URL로 키를 추출합니다.
        key = extract_key(url)
        
        # MongoDB에서 key에 해당하는 데이터를 검색합니다.
        ebook = collection.find_one({'key': key})
        
        # MongoDB에 존재하지 않는 경우만 상세 페이지를 크롤링합니다.
        if not ebook:
            time.sleep(1)
            response = requests.get(url)
            ebook = scrape_detail_page(response)
            # 책 정보를 MongoDB에 저장합니다.
            collection.insert_one(ebook)
            
        # 책 정보를 출력합니다.
        print(ebook)

def scrape_list_page(response):
    """
    목록 페이지의 Response에서 상세 페이지의 URL을 추출합니다.
    """
    root = lxml.html.fromstring(response.content)
    root.make_links_absolute(response.url)
    for a in root.cssselect('.view_box .book_tit a'):
        url = a.get('href')
        yield url

def scrape_detail_page(response):
    """
    상세 페이지의 Response에서 책 정보를 dict로 추출합니다.
    """
    root = lxml.html.fromstring(response.content)
    ebook = {
        'url': response.url,
        'key': extract_key(response.url),
        'title': root.cssselect('.store_product_info_box h3')[0].text_content(),
        'price': root.cssselect('.pbr strong')[0].text_content(),
        'content': "생략"
    }
    return ebook

def extract_key(url):
    """
    URL에서 키(URL 끝의 p_code)를 추출합니다.
    """
    m = re.search(r"p_code=(.+)", url)
    return m.group(1)

def normalize_spaces(s):
    """
    연결돼 있는 공백을 하나의 공백으로 변경합니다.
    """
    return re.sub(r'\s+', ' ', s).strip()
    
if __name__ == '__main__':
    main()

```


```python
# 크롤러 실행
# % run modules/python_crawler_final.py 
```

<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
