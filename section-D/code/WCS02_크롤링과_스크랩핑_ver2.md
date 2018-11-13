
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
    <option value="CH02" selected> 02.파이썬으로 시작하는 크롤링/스크레이핑         </option>
    <option value="CH03"> 03.주요 라이브러리 활용                          </option>
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

## <font color='#0000AA'>파이썬으로 시작하는 크롤링/스크레이핑 </font>
>   
<font color='#0000CC'>
- 파이썬 기초 지식
- 웹 페이지 추출
- 웹 페이지에서 데이터 추출
- 데이터 저장
- 파이썬으로 스크레이핑하는 흐름

<hr>
### <font color='#0000CC'>  가상환경 사용법
> 
- 가상환경 생성
<br/> \> python -m venv 디렉토리명(myvenv)
<br/> \> .\scraping\Scripts\activate
<br/> \(myvenv) > python --version 
<br/><br/> 
- 가상환경 종료
<br/> \(myvenv) > .\scraping\Scripts\deactivate
<br/> \> dir/w


```python
import os
from os.path import exists

def make_dir(dir_name):
    ''' 디렉토리 생성 '''
    
    if not exists(dir_name):
        os.mkdir(dir_name)
        msg = "{} 디렉토리를 생성하였습니다!".format(dir_name)
    else:
        msg = "{} 디렉토리가 이미 존재합니다!".format(dir_name)
        
    return msg
```

<hr>
### <font color='#0000CC'> 웹 페이지 추출

#### <font color='#0000FF'> c2-09_urlopen_encoding
> ** HTTP 헤더에서 인코딩 방식 추출 **
- text/html
- text/html; charset=UTF-8
- text/html; charset=EUC-KR

cf. 연관함수 : HTTPMessage.info().get_content_charset()


```python
import sys
from urllib.request import urlopen
```


```python
f = urlopen('http://www.hanbit.co.kr/store/books/full_book_list.html')

# HTTP 헤더를 기반으로 인코딩 방식을 추출합니다
# (명시돼 있지 않을 경우 utf-8을 사용하게 합니다).
encoding = f.info().get_content_charset(failobj="utf-8")

# 인코딩 방식을 표준 오류에 출력합니다.
print('encoding:', encoding, file=sys.stderr)

```


```python
# 추출한 인코딩 방식으로 디코딩합니다.
text = f.read().decode(encoding)
# 웹 페이지의 내용을 표준 출력에 출력합니다.
text
```

#### <font color='#0000FF'> c2-10_urlopen_meta
> ** meta 태그에서 인코딩 방식 추출 **
<br/>Content-Type 헤더의 값고 실제 사용되고 있는 인코딩 형식이 다를 수 있다.
<br/> 디코딩 처리때 ** UnicodeDecodeError가 발생 ** 한다면 이러한 처리를 모방해서 구현하면 해결할 수 있다.
- < meta charset="utf-8" >
- < meta http-equiv="Content-Type" content="text/html; charset="EUC-KR" >
 
cf. 연관함수 : HTTPMessage.info().get_content_charset()


```python
import re
import sys
from urllib.request import urlopen

```


```python
f = urlopen('http://www.hanbit.co.kr/store/books/full_book_list.html')
# bytes 자료형의 응답 본문을 일단 변수에 저장합니다.
bytes_content = f.read()  

type(bytes_content), bytes_content[:2**10]
```


```python
# charset은 HTML의 앞부분에 적혀 있는 경우가 많으므로
# 응답 본문의 앞부분 1024바이트를 ASCII 문자로 디코딩해 둡니다.
# ASCII 범위 이위의 문자는 U+FFFD(REPLACEMENT CHARACTER)로 변환되어 예외가 발생하지 않습니다.
scanned_text = bytes_content[:2**10].decode('ascii', errors='replace')

type(scanned_text), scanned_text
```


```python
scanned_text = bytes_content[:2**10].decode('utf-8', errors='replace')

type(scanned_text), scanned_text
```


```python
# 디코딩한 문자열에서 정규 표현식으로 charset 값을 추출합니다.
match = re.search(r'charset=["\']?([\w-]+)', scanned_text)
if match:
    encoding = match.group(1)
else:
    # charset이 명시돼 있지 않으면 UTF-8을 사용합니다.
    encoding = 'utf-8'

# 추출한 인코딩을 표준 오류에 출력합니다.
print('encoding:', encoding, file=sys.stderr)

```


```python
# 추출한 인코딩으로 다시 디코딩합니다.
text = bytes_content.decode(encoding)

# 응답 본문을 표준 출력에 출력합니다.
print(text[:2**10])
```

<hr>
### <font color='#0000CC'> 웹 페이지에서 데이터 추출
> 
- Regular Expression
- XML Parser

#### <font color='#0000FF'>  c2-11_scrape_re
> 정규표현식으로 스크레이핑


```python
! wget http://www.hanbit.co.kr/store/books/full_book_list.html
```


```python
! dir *.html
```


```python
# ! mkdir data
make_dir('data')
```


```python
! dir data
```


```python
! ren full_book_list.html dp.html
! move dp.html data
```


```python
! dir data\*.html
```


```python
import re
from html import unescape

# 이전 절에서 다운로드한 파일을 열고 html이라는 변수에 저장합니다.
with open('./data/dp.html', encoding='utf-8') as f:
    html = f.read()

# re.findall()을 사용해 도서 하나에 해당하는 HTML을 추출합니다.
print('check')
for partial_html in re.findall(r'<td class="left"><a.*?</td>', html, re.DOTALL):
    # 도서의 URL을 추출합니다.
    url = re.search(r'<a href="(.*?)">', partial_html).group(1)
    url = 'http://www.hanbit.co.kr' + url
    # 태그를 제거해서 도서의 제목을 추출합니다.
    title = re.sub(r'<.*?>', '', partial_html)
    title = unescape(title)
    print('url:', url)
    print('title:', title)
    print('---')
```

#### <font color='#0000FF'> c2-12 : rss.xml
> RSS 파싱하기
- 서울/경기도 지역의 날씨 받기
- http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109


```python
! wget http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109
```


```python
! dir
```

<hr>

``` wget
wget --help 
wget link -O file.ext 
```


```python
! wget --help
```


```python
# rss 데이터 저장
! wget rss.xml http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109 -O ./data/rss.xml
```


```python
! dir data\*.xml
```

#### <font color='#0000FF'> c2-13_scrape_rss
> ElementTree 모듈을 사용해 RSS 파싱


```python
# ElementTree 모듈을 읽어 들입니다.
from xml.etree import ElementTree

# parse() 함수로 파일을 읽어 들이고 ElementTree 객체를 만듭니다.
tree = ElementTree.parse('./data/rss.xml')

# getroot() 메서드로 XML의 루트 요소를 추출합니다.
root = tree.getroot()

```


```python
msg = " - tree : {} \n - root : {}".format(tree, root)
print(msg)
```


```python
find_data = root.findall('channel/item/description/body/location/data')
len(find_data), find_data[0]
```


```python
# findall() 메서드로 요소 목록을 추출합니다.
# 태그를 찾습니다(자세한 내용은 RSS를 열어 참고해주세요).
for item in root.findall('channel/item/description/body/location/data'):
    # find() 메서드로 요소를 찾고 text 속성으로 값을 추출합니다.
    tm_ef = item.find('tmEf').text
    tmn   = item.find('tmn').text
    tmx   = item.find('tmx').text
    wf    = item.find('wf').text
    print(tm_ef, tmn, tmx, wf) # 출력합니다.

```

<hr>
### <font color='#0000CC'> 데이터 저장
> 
- TEXT파일로 저장 : CSV/TSV 형식, JSON 형식
- DataBase에 저장 : SQLite3, MySQL, Oracle, MongoDB 

#### <font color='#0000FF'> c2-14_save_csv_join
> CSV(Comma-Seperated Values) 형식으로 저장
- str.join() 메소드 사용
- (venb) $ python OOO.py > OOO.csv


```python
# 첫 번째 줄에 헤더를 작성합니다.
print('rank,city,population')  

```


```python
# join() 메서드의 매개변수로 전달한 list는 str이어야 하므로 주의해 주세요.
print(','.join(['1', '상하이', '24150000']))
print(','.join(['2', '카라치', '23500000']))
print(','.join(['3', '베이징', '21516000']))
print(','.join(['4', '텐진', '14722100']))
print(','.join(['5', '이스탄불', '14160467']))
```

#### <font color='#0000FF'> c2-15_save_csv
> CSV(Comma-Seperated Values) 형식으로 저장


```python
import csv

# 파일을 엽니다. newline=''으로 줄바꿈 코드의 자동 변환을 제어합니다.
csv_file = './data/top_cities_1.csv'

with open(csv_file, 'w', newline='') as f:
    # csv.writer는 파일 객체를 매개변수로 지정합니다.
    writer = csv.writer(f)  
    # 첫 번째 줄에는 헤더를 작성합니다.
    writer.writerow(['rank', 'city', 'population'])  
    # writerows()에 리스트를 전달하면 여러 개의 값을 출력합니다.
    writer.writerows([
        [1, '상하이', 24150000],
        [2, '카라치', 23500000],
        [3, '베이징', 21516000],
        [4, '텐진', 14722100],
        [5, '이스탄불', 14160467],
    ])
```


```python
# 확인
with open(csv_file, 'r') as f:
    data = f.read()

print(data)
```

#### <font color='#0000FF'>  c2-16_save_csv_dict
> 딕셔너리 형식으로 저장


```python
import csv

csv_file = './data/top_cities_2.csv'
with open(csv_file, 'w', newline='') as f:
    # 첫 번째 매개변수에 파일 객체
    # 두 번째 매개변수에 필드 이름 리스트를 지정합니다.
    writer = csv.DictWriter(f, ['rank', 'city', 'population'])
      # 첫 번째 줄에 헤더를 입력합니다.
    writer.writeheader()
    # writerows()로 여러 개의 데이터를 딕셔너리 형태로 작성합니다.
    writer.writerows([
        {'rank': 1,  'city': '상하이',   'population': 24150000},
        {'rank': 2,  'city': '카라치',   'population': 23500000},
        {'rank': 3,  'city': '베이징',   'population': 21516000},
        {'rank': 4,  'city': '텐진',     'population': 14722100},
        {'rank': 5,  'city': '이스탄불', 'population': 14160467},
    ])
```


```python
# 확인
with open(csv_file, 'r') as f:
    data = f.readlines()
    
for idx in range(len(data)):    
    print(data[idx], end='')
    if idx==0:
        print('-'*20)
    
```

#### <font color='#0000FF'> c2-17_save_json
> JSON 형식으로 저장


```python
import json

cities = [
    {'rank': 1,  'city': '상하이',   'population': 24150000},
    {'rank': 2,  'city': '카라치',   'population': 23500000},
    {'rank': 3,  'city': '베이징',   'population': 21516000},
    {'rank': 4,  'city': '텐진',     'population': 14722100},
    {'rank': 5,  'city': '이스탄불', 'population': 14160467},
]

print(json.dumps(cities))
```


```python
print(json.dumps(cities, ensure_ascii=False, indent=4))
```

#### <font color='#0000FF'> c2-18_save_sqlite3
> 데이터베이스(SQLite3)에 저장
- SQLite3 는 파일기반의 간단한 관계형 데이터베이스
- SQL 구문을 사용해 데이터를 읽고 쓰기

``` python
import sqlite3

# top_cities.db 파일을 열고 연결을 변수에 저장합니다.
conn = sqlite3.connect('./database/top_cities.db')

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
# SQL 내부에서 파라미터로 변경할 부분(플레이스홀더)은 ?로 지정합니다.
c.execute('INSERT INTO cities VALUES (?, ?, ?)', (1, '상하이', 24150000))

# 파라미터가 딕셔너리일 때는 플레이스홀더를 :<이름> 형태로 지정합니다.
c.execute('INSERT INTO cities VALUES (:rank, :city, :population)',
          {'rank': 2, 'city': '카라치', 'population': 23500000})

# executemany() 메서드를 사용하면 여러 개의 파라미터를 리스트로 지정해서
# 여러 개(현재 예제에서는 3개)의 SQL 구문을 실행할 수 있습니다.
c.executemany('INSERT INTO cities VALUES (:rank, :city, :population)', [
    {'rank': 3,  'city': '베이징',   'population': 21516000},
    {'rank': 4,  'city': '텐진',     'population': 14722100},
    {'rank': 5,  'city': '이스탄불', 'population': 14160467},
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


```python
# ! mkdir database
make_dir('database')
```


```python
import sqlite3

# top_cities.db 파일을 열고 연결을 변수에 저장합니다.
db_path = './database/top_cities.db'
conn = sqlite3.connect(db_path)

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

```


```python
# execute() 메서드의 두 번째 매개변수에는 파라미터를 지정할 수 있습니다.
# SQL 내부에서 파라미터로 변경할 부분(플레이스홀더)은 ?로 지정합니다.
c.execute('INSERT INTO cities VALUES (?, ?, ?)', (1, '상하이', 24150000))

```


```python
# 파라미터가 딕셔너리일 때는 플레이스홀더를 :<이름> 형태로 지정합니다.
c.execute('INSERT INTO cities VALUES (:rank, :city, :population)',
          {'rank': 2, 'city': '카라치', 'population': 23500000}) 

```


```python
# executemany() 메서드를 사용하면 여러 개의 파라미터를 리스트로 지정해서
# 여러 개(현재 예제에서는 3개)의 SQL 구문을 실행할 수 있습니다.
c.executemany('INSERT INTO cities VALUES (:rank, :city, :population)', [
    {'rank': 3, 'city': '베이징', 'population': 21516000},
    {'rank': 4, 'city': '텐진', 'population': 14722100},
    {'rank': 5, 'city': '이스탄불', 'population': 14160467},
])

```


```python
# 변경사항을 커밋(저장)합니다.
conn.commit()

```


```python
# 저장한 데이터를 추출합니다.
c.execute('SELECT * FROM cities')

# 쿼리의 결과는 fetchall() 메서드로 추출할 수 있습니다.
for row in c.fetchall():
    # 추출한 데이터를 출력합니다.
    print(row)

# 연결을 닫습니다.
conn.close()
```

#### <font color='#0000FF'> c2-19_python_scraper
> 파이썬으로 스크레이핑하는 프로세스
- 웹 페이지를 추출
- 스크레이핑
- 데이터를 저장

### main( ) 함수에서 차례대로 호출
- fetch(url) : 매개변수로 url을 받고 지정한 URL의 웹 페이지를 추출
- scrape(html) : 매개변수로 html을 받고, 정규표현식을 사용해 HTML에서 도서 정보를 추출
- save(db_path, books) : 매개변수로 books라는 도서 목록을 받고, SQLite 데이터베이스에 저장

``` python
# python_scraper.py 

import re
import sqlite3
from urllib.request import urlopen
from html import unescape

def main():
    """
    메인 처리입니다.
    fetch(), scrape(), save() 함수를 호출합니다.
    """
    
    url = 'http://www.hanbit.co.kr/store/books/full_book_list.html'
    db_path = './database/books.db'
    
    html = fetch(url)
    books = scrape(html)
    save(db_path, books)


def fetch(url):
    """
    매개변수로 전달받을 url을 기반으로 웹 페이지를 추출합니다.
    웹 페이지의 인코딩 형식은 Content-Type 헤더를 기반으로 알아냅니다.
    반환값: str 자료형의 HTML
    """
    f = urlopen(url)
    
    # HTTP 헤더를 기반으로 인코딩 형식을 추출합니다.
    encoding = f.info().get_content_charset(failobj="utf-8")
    
    # 추출한 인코딩 형식을 기반으로 문자열을 디코딩합니다.
    html = f.read().decode(encoding)
    return html


def scrape(html):
    """
    매개변수 html로 받은 HTML을 기반으로 정규 표현식을 사용해 도서 정보를 추출합니다.
    반환값: 도서(dict) 리스트
    """
    books = []
    
    # re.findall()을 사용해 도서 하나에 해당하는 HTML을 추출합니다.
    for partial_html in re.findall(r'<td class="left"><a.*?</td>', html, re.DOTALL):
        # 도서의 URL을 추출합니다.
        url = re.search(r'<a href="(.*?)">', partial_html).group(1)
        url = 'http://www.hanbit.co.kr' + url
        
        # 태그를 제거해서 도서의 제목을 추출합니다.
        title = re.sub(r'<.*?>', '', partial_html)
        title = unescape(title)
        books.append({'url': url, 'title': title})
    
    return books


def save(db_path, books):
    """
    매개변수 books로 전달된 도서 목록을 SQLite 데이터베이스에 저장합니다.
    데이터베이스의 경로는 매개변수 dp_path로 지정합니다.
    반환값: None(없음)
    """
    # 데이터베이스를 열고 연결을 확립합니다.
    conn = sqlite3.connect(db_path)
    
    # 커서를 추출합니다.
    c = conn.cursor()
    
    # execute() 메서드로 SQL을 실행합니다.
    # 스크립트를 여러 번 실행할 수 있으므로 기존의 books 테이블을 제거합니다.
    c.execute('DROP TABLE IF EXISTS books')
    
    # books 테이블을 생성합니다.
    c.execute('''
        CREATE TABLE books (
            title text,
            url text
        )
    ''')
    
    # executemany() 메서드를 사용하면 매개변수로 리스트를 지정할 수 있습니다.
    c.executemany('INSERT INTO books VALUES (:title, :url)', books)
    
    # 변경사항을 커밋(저장)합니다.
    conn.commit()
    
    # 연결을 종료합니다.
    conn.close()


# python 명령어로 실행한 경우 main() 함수를 호출합니다.
# 이는 모듈로써 다른 파일에서 읽어 들였을 때 main() 함수가 호출되지 않게 하는 것입니다.
# 파이썬 프로그램의 일반적인 작성 방식입니다.
if __name__ == '__main__':
    main()
    
```

<br/>
<hr>


```python
# ! mkdir modules
make_dir('modules')
```


```python
%%writefile  ./modules/python_scraper.py 

import re
import sqlite3
from urllib.request import urlopen
from html import unescape

def main():
    """
    메인 처리입니다.
    fetch(), scrape(), save() 함수를 호출합니다.
    """
    
    url = 'http://www.hanbit.co.kr/store/books/full_book_list.html'
    db_path = './database/books.db'
    
    html = fetch(url)
    books = scrape(html)
    save(db_path, books)


def fetch(url):
    """
    매개변수로 전달받을 url을 기반으로 웹 페이지를 추출합니다.
    웹 페이지의 인코딩 형식은 Content-Type 헤더를 기반으로 알아냅니다.
    반환값: str 자료형의 HTML
    """
    f = urlopen(url)
    # HTTP 헤더를 기반으로 인코딩 형식을 추출합니다.
    encoding = f.info().get_content_charset(failobj="utf-8")
    # 추출한 인코딩 형식을 기반으로 문자열을 디코딩합니다.
    html = f.read().decode(encoding)
    return html


def scrape(html):
    """
    매개변수 html로 받은 HTML을 기반으로 정규 표현식을 사용해 도서 정보를 추출합니다.
    반환값: 도서(dict) 리스트
    """
    books = []
    # re.findall()을 사용해 도서 하나에 해당하는 HTML을 추출합니다.
    for partial_html in re.findall(r'<td class="left"><a.*?</td>', html, re.DOTALL):
        # 도서의 URL을 추출합니다.
        url = re.search(r'<a href="(.*?)">', partial_html).group(1)
        url = 'http://www.hanbit.co.kr' + url
        # 태그를 제거해서 도서의 제목을 추출합니다.
        title = re.sub(r'<.*?>', '', partial_html)
        title = unescape(title)
        books.append({'url': url, 'title': title})
    
    return books


def save(db_path, books):
    """
    매개변수 books로 전달된 도서 목록을 SQLite 데이터베이스에 저장합니다.
    데이터베이스의 경로는 매개변수 dp_path로 지정합니다.
    반환값: None(없음)
    """
    # 데이터베이스를 열고 연결을 확립합니다.
    conn = sqlite3.connect(db_path)
    
    # 커서를 추출합니다.
    c = conn.cursor()
    
    # execute() 메서드로 SQL을 실행합니다.
    # 스크립트를 여러 번 실행할 수 있으므로 기존의 books 테이블을 제거합니다.
    c.execute('DROP TABLE IF EXISTS books')
    
    # books 테이블을 생성합니다.
    c.execute('''
        CREATE TABLE books (
            title text,
            url text
        )
    ''')
    
    # executemany() 메서드를 사용하면 매개변수로 리스트를 지정할 수 있습니다.
    c.executemany('INSERT INTO books VALUES (:title, :url)', books)
    
    # 변경사항을 커밋(저장)합니다.
    conn.commit()
    
    # 연결을 종료합니다.
    conn.close()

# python 명령어로 실행한 경우 main() 함수를 호출합니다.
# 이는 모듈로써 다른 파일에서 읽어 들였을 때 main() 함수가 호출되지 않게 하는 것입니다.
# 파이썬 프로그램의 일반적인 작성 방식입니다.
if __name__ == '__main__':
    main()
    
```


```python
! dir/w modules\*.py
```


```python
# 파이썬 실행1
% run modules/python_scraper.py 
```


```python
# # 파이썬 실행2
! python modules/python_scraper.py 
```


```python
! dir database
```


```python
# ! sqlite3 ./database/books.db
```

<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
