
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
    <option value="CH03"> 03.주요 라이브러리 활용                          </option>
    <option value="CH04"> 04.크롤러를 사용할 때 기억해야 하는 것           </option>
    <option value="CH05" selected> 05.크롤링/스크레이핑 실전과 데이터 활용          </option>
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

## <font color='#0000AA'>크롤링/스크레이핑 실전과 데이터 활용 </font>
>  
<font color='#0000CC'>
- 데이터 세트 추출과 활용
- API로 데이터 수집하고 활용
- 시계열 데이터 수집하고 활용
- 열린 데이터 수집과 활용
- 웹 페이지 자동 조작
- 자바스크립트를 이용한 페이지 스크레이핑
- 추출한 데이터 활용


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
### <font color='0000CC'> 데이터 세트 추출과 활용 </font>
> <a href='https://dumps.wikimedia.org/kowiki/'>Index of /kowiki/ </a>
* 위키백과 데이터 세트 다운로드 
* 위키백과 데이터 세트에서 문장 추출


#### <font color='#0000CC'> 위키백과 데이터 세트 다운로드 </font>


```python
make_dir('data/dataset')
```


```python
# ! wget https://dumps.wikimedia.org/kowiki/20181101/ -q -O -
```


```python
! wget https://dumps.wikimedia.org/kowiki/20181101/ -O ./data/dataset/kowiki-2018110-index.html
```


```python
from bs4 import BeautifulSoup
import pandas as pd

filepath = './data/dataset/kowiki-2018110-index.html'
with open(filepath, encoding='utf-8') as fp:
    soup = BeautifulSoup(fp, 'lxml')

soup.title
```


```python
done_tags = soup.find_all('li', 'done')
len(done_tags)
```


```python
done_tag = done_tags[0]
done_tag
```


```python
updates = done_tag.find('span', 'updates').get_text()
updates
```


```python
title = done_tag.find('span', 'title').get_text()
title
```


```python
file_tags = done_tag.find_all('li', 'file')
files = []
for file_tag in file_tags:
    file_dict = {}
    file_name = file_tag.find('a').get_text()
    file_link = file_tag.find('a').get('href')
    
    file_dict['FileName'] = file_name
    file_dict['FileLink'] = file_link
    files.append(file_dict)

files
```


```python
from bs4 import BeautifulSoup
import pandas as pd

def getKowikiInfos(filepath):

    with open(filepath, encoding='utf-8') as fp:
        soup = BeautifulSoup(fp, 'lxml')

    Updates  = []
    Title    = []
    FileList = []   # 파일이름 리스트
    Files    = []   # 파일상세 리스트

    done_tags = soup.find_all('li', 'done')

    for done_tag in done_tags:
        # 등록날짜
        updates = done_tag.find('span', 'updates').get_text()

        # 제목
        title = done_tag.find('span', 'title').get_text()

        # 파일리스트
        file_tags = done_tag.find_all('li', 'file')
        files = []
        filenames = []
        for file_tag in file_tags:
            file_dict = {}
            file_name = file_tag.find('a').get_text()
            file_link = file_tag.find('a').get('href')

            file_dict['FileName'] = file_name
            file_dict['FileLink'] = file_link
            files.append(file_dict)

            filenames.append(file_name)

        Updates.append(updates)
        Title.append(title)
        FileList.append(tuple(filenames))
        Files.append(files)

    kokiwi_df = pd.DataFrame({ 'Updates'  : Updates, 
                               'Title'    : Title,
                               'FileList' : FileList,
                               'FileInfo' : Files }, 
                               columns = ['Updates', 'Title', 'FileList', 'FileInfo'])

    return kokiwi_df

```


```python
filepath = './data/dataset/kowiki-2018110-index.html'
kokiwi_df = getKowikiInfos(filepath)
```


```python
kokiwi_df.head()
```


```python
kokiwi_df['FileList'][0]
```

#### <font color='#0000CC'> 자연어 처리를 사용한 빈출 단어 추출 </font>
> 형태소 분석 : 자연어 처리의 기본 기술
* 주어진 단어를 형태소라는 최소 단어로 분할해서 품사 등을 판별하는 것을 의미
* 형태소 분석 라이브러리 : <a hrep="http://www.konlpy.org/ko/latest/"><u>KoNLLPy, 파이썬 한국어 NLP</u></a>
    - 한나눔
    - 꼬꼬마
    - Komoran
    - MeCab
    - 트위트


#### <font color='#0000FF'> c5-01_konlpy_sample </font>
> KoNLPy로 형태소 분석


```python
from konlpy.tag import Kkma

kkma   = Kkma()
malist = kkma.pos("아버지 가방에 들어가신다.")
malist
```

#### <font color='#0000CC'> 문장에서 빈출 단어 추출 </font>


#### <font color='#0000FF'> c5-02_word_frequency </font>
> 위키백과 문장에서 빈출 단어 추출

``` python
%%writefile  ./modules/word_frequency.py

import sys
import os
from glob import glob
from collections import Counter
from konlpy.tag import Kkma

def main():
    """
    명령라인 매개변수로 지정한
    디렉터리 내부의 파일을 읽어 들이고
    빈출 단어를 출력합니다.
    """
    # 명령어의 첫 번째 매개변수로
    # WikiExtractor의 출력 디렉터리를 지정합니다.
    input_dir = sys.argv[1]
    kkma = Kkma()
    # 단어의 빈도를 저장하기 위한 Counter 객체를 생성합니다.
    # Counter 클래스는 dict를 상속받는 클래스입니다.
    frequency = Counter()
    count_proccessed = 0
    # glob()으로 와일드카드 매치 파일 목록을 추출하고
    # 매치한 모든 파일을 처리합니다.
    for path in glob(os.path.join(input_dir, '*', 'wiki_*')):
        print('Processing {0}...'.format(path), file=sys.stderr)
        # 파일을 엽니다.
        with open(path) as file:
            # 파일 내부의 모든 기사에 반복을 돌립니다.
            for content in iter_docs(file):
                # 페이지에서 명사 리스트를 추출합니다.
                tokens = get_tokens(kkma, content)
                # Counter의 update() 메서드로 리스트 등의 반복 가능 객체를 지정하면
                # 리스트에 포함된 값의 출현 빈도를 세어줍니다.
                frequency.update(tokens)
                # 10,000개의 글을 읽을 때마다 간단하게 출력합니다.
                count_proccessed += 1
                if count_proccessed % 10000 == 0:
                    print('{0} documents were processed.'
                        .format(count_proccessed),file=sys.stderr)
    
    # 모든 기사의 처리가 끝나면 상위 30개의 단어를 출력합니다
    for token, count in frequency.most_common(30):
        print(token, count)

def iter_docs(file):
    """
    파일 객체를 읽어 들이고
    기사의 내용(시작 태그 <doc>와 종료 태그 </doc> 사이의 텍스트)를 꺼내는
    제너레이터 함수
    """
    for line in file:
        if line.startswith('<doc '):
            # 시작 태그가 찾아지면 버퍼를 초기화합니다.
            buffer = []
        elif line.startswith('</doc>'):
            # 종료 태그가 찾아지면 버퍼의 내용을 결합한 뒤 yield합니다.
            content = ''.join(buffer)
            yield content
        else:
            # 시작 태그/종료 태그 이외의 줄은 버퍼에 추가합니다.
            buffer.append(line)

def get_tokens(kkma, content):
    """
    문장 내부에 출현한 명사 리스트를 추출하는 함수
    """
    # 명사를 저장할 리스트입니다.
    tokens = []
    node = kkma.pos(content)
    for (taeso, pumsa) in node:
        # 고유 명사와 일반 명사만 추출합니다.
        if pumsa in ('NNG', 'NNP'):
            tokens.append(taeso)
    return tokens

if __name__ == '__main__':
    main()

```

<br/>
<hr>


```python
%%writefile  word_frequency.py
# %%writefile  ./modules/word_frequency.py
import sys
import os
from glob import glob
from collections import Counter
from konlpy.tag import Kkma

def main():
    """
    명령라인 매개변수로 지정한
    디렉터리 내부의 파일을 읽어 들이고
    빈출 단어를 출력합니다.
    """
    # 명령어의 첫 번째 매개변수로
    # WikiExtractor의 출력 디렉터리를 지정합니다.
    input_dir = sys.argv[1]
    print('input_dir :', input_dir)
    kkma = Kkma()
    
    # 단어의 빈도를 저장하기 위한 Counter 객체를 생성합니다.
    # Counter 클래스는 dict를 상속받는 클래스입니다.
    frequency = Counter()
    count_proccessed = 0
    
    # glob()으로 와일드카드 매치 파일 목록을 추출하고
    # 매치한 모든 파일을 처리합니다.
    # print('before for :', glob(os.path.join(input_dir, 'kowiki-*')))
    # for path in glob(os.path.join(input_dir, '*', 'wiki_*')):
    for path in glob(os.path.join(input_dir, 'kowiki-*')):
        print('path :', path)
        print('Processing {0}...'.format(path), file=sys.stderr)
        
        # 파일을 엽니다.
        with open(path) as file:
            # 파일 내부의 모든 기사에 반복을 돌립니다.
            for content in iter_docs(file):
                # 페이지에서 명사 리스트를 추출합니다.
                tokens = get_tokens(kkma, content)
                
                # Counter의 update() 메서드로 리스트 등의 반복 가능 객체를 지정하면
                # 리스트에 포함된 값의 출현 빈도를 세어줍니다.
                frequency.update(tokens)
                
                # 10,000개의 글을 읽을 때마다 간단하게 출력합니다.
                count_proccessed += 1
                if count_proccessed % 10000 == 0:
                    print('{0} documents were processed.'
                        .format(count_proccessed),file=sys.stderr)
    
    # 모든 기사의 처리가 끝나면 상위 30개의 단어를 출력합니다
    for token, count in frequency.most_common(30):
        print(token, count)

        
def iter_docs(file):
    """
    파일 객체를 읽어 들이고
    기사의 내용(시작 태그 <doc>와 종료 태그 </doc> 사이의 텍스트)를 꺼내는
    제너레이터 함수
    """
    for line in file:
        if line.startswith('<doc '):
            # 시작 태그가 찾아지면 버퍼를 초기화합니다.
            buffer = []
        elif line.startswith('</doc>'):
            # 종료 태그가 찾아지면 버퍼의 내용을 결합한 뒤 yield합니다.
            content = ''.join(buffer)
            yield content
        else:
            # 시작 태그/종료 태그 이외의 줄은 버퍼에 추가합니다.
            buffer.append(line)

            
def get_tokens(kkma, content):
    """
    문장 내부에 출현한 명사 리스트를 추출하는 함수
    """
    # 명사를 저장할 리스트입니다.
    tokens = []
    node = kkma.pos(content)
    for (taeso, pumsa) in node:
        # 고유 명사와 일반 명사만 추출합니다.
        if pumsa in ('NNG', 'NNP'):
            tokens.append(taeso)
    return tokens

if __name__ == '__main__':
    main()
    
```


```python
make_dir('./data/result')
```


```python
! python word_frequency.py .\data\dataset
```

<hr>
### <font color='0000CC'> API로 데이터 수집하고 활용 </font>
> 
* 트위트에서 데이터 수집
* 유튜브에서 데이터 수집


### <font color='#CC0000'> 트위터에서 데이터 수집 </font>
> 데이터 수집에 사용되는 2가지 API
- <font color='#7777FF'>REST API </font>: 
<br/> - <u>HTTP 요청을 전송하면 HTTP 응답을 반환하는 RESTful 형태</u>로 트윗 또는 사용자 정보를 추출, 
<br/> - 호출 횟수 제한이 굉장히 엄격
<br/> - 한 사용자당 15분에 15회만 호출 제한이 있으므로, 대규모 데이터수집에는 좋지 않다.
<br/><br/> 
- <font color='#7777FF'>Streaming API </font>: 
<br/> - 한번의 요청을 보내면 서버와의 연결(컨넥션)을 유지하고, 
<br/> - 새로운 데이터가 추가될 때마다 서버가 데이터를 전송해주는 푸시 형태
<br/> - HTTP 요청을 보냈을때 <u>연결을 확립한 상태</u>로 두고 서버에서 메시지를 계속 전송받는 형태


cf. RESTful : https://meetup.toast.com/posts/92
>  
* REST 구성
<br/> - 자원(RESOURCE) - URI
<br/> - 행위(Verb) - HTTP METHOD
<br/> - 표현(Representations)
<br/><br/>
* REST 특징
<br/> 1) Uniform (유니폼 인터페이스)
<br/> 2) Stateless (무상태성)
<br/> 3) Cacheable (캐시 가능)
<br/> 4) Self-descriptiveness (자체 표현 구조)
<br/> 5) Client - Server 구조
<br/> 6) 계층형 구조
<br/>
<br/>[참고] HTTP METHOD의 알맞은 역할 
<br/>POST, GET, PUT, DELETE 이 4가지의 Method를 가지고 CRUD를 할 수 있습니다.


#### <font color='#0000CC'> 트위터 API 인증 </font>
> OAuth 1.0a 인증 필요 (아래 4가지 모두 필요)
* 애플리케니션 단위 발행
<br/> - Cousumer Key
<br/> - Consuber Secret
<br/><br/> 
* 사용자 단위 발행
<br/> - Access Token
<br/> - Access Token Secret


> 트위터 인증 정보를 위해 애플리케이션 등록
- <a href="https://apps.twitter.com/"><b>[ 애플리케이션 관리 화면 ]</b></a> 에 트위터 계정으로 로그인
- "Create New App" 버튼 클릭
- 이름, 설명, 웹사이트 를 입력하고 사용약관 동의하면 애플리케이션이 생성된다.
- "Keys and Access Tokens" 링크 클릭 후, 생성된 4개의 키 값을 저장

<hr>
#### <font color='#0000CC'> Twitter Key 값 확인 </font>
>  key값 확인 :  https://apps.twitter.com/app/13434937/keys
<br/>
> #### <font color='#7777FF'>Application Settings  </font>
> Keep the "Consumer Secret" a secret. This key should never be human-readable in your application.
- <font color='#CC0000'>Consumer Key (API Key)       </font>:<font color='#CCCCCC'> oWmNK＊＊＊＊＊＊＊＊＊＊＊ </font>
- <font color='#CC0000'>Consumer Secret (API Secret) </font>:<font color='#CCCCCC'> pM3MNxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx </font>
<br/>

> #### <font color='#7777FF'>Your Access Token  </font>
> This access token can be used to make API requests on your own account's behalf. Do not share your access token secret with anyone.
- <font color='#CC0000'>Access Token                 </font>:<font color='#CCCCCC'> 15625xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx </font>
- <font color='#CC0000'>Access Token Secret          </font>:<font color='#CCCCCC'> aeFqGxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx </font>

<hr>


```python
# Twitter Application Settings
CONSUMER_KEY        = "oWmNK********************"
CONSUMER_SECRET     = "pM3MN*********************************************"

# Twitter Your Access Token
ACCESS_TOKEN        = "15625*********************************************"
ACCESS_TOKEN_SECRET = "aeFqG****************************************"

```

#### <font color='#0000FF'> c5-03_rest_api_with_requests_oauthlib </font>
> Requests OAuthLib 를 이용한 타임라인 추출
- 인증 정보를 사용해 OAuth1Session 객체를 생성
- API 응답이 JSON 형식의 문자열이므로 response.json()으로 파싱
- status는 트윗(Twitter API에서는 Status)를 나타내는 dict


```python
from bigpycraft.oauth import twitter_key 
from requests_oauthlib import OAuth1Session
import os

# 환경변수에서 인증 정보를 추출합니다.
# CONSUMER_KEY        = os.environ['CONSUMER_KEY']
# CONSUMER_SECRET     = os.environ['CONSUMER_SECRET']
# ACCESS_TOKEN        = os.environ['ACCESS_TOKEN']
# ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

CONSUMER_KEY        = twitter_key.CONSUMER_KEY
CONSUMER_SECRET     = twitter_key.CONSUMER_SECRET
ACCESS_TOKEN        = twitter_key.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = twitter_key.ACCESS_TOKEN_SECRET


# 인증 정보를 사용해 OAuth1Session 객체를 생성합니다.
twitter = OAuth1Session(CONSUMER_KEY,
                        client_secret=CONSUMER_SECRET,
                        resource_owner_key=ACCESS_TOKEN,
                        resource_owner_secret=ACCESS_TOKEN_SECRET)

# 사용자의 타임라인을 추출합니다.
response = twitter.get('https://api.twitter.com/1.1/statuses/home_timeline.json')

# API 응답이 JSON 형식의 문자열이므로 response.json()으로 파싱합니다.
# status는 트윗(Twitter API에서는 Status라고 부릅니다)를 나타내는 dict입니다.
for status in response.json():
    # 사용자 이름과 트윗을 출력합니다.
    print('@' + status['user']['screen_name'], status['text'])
    
```

#### <font color='#0000FF'> c5-04_rest_api_with_tweepy </font>
> tweepy 를 이용한 타임라인 추출
- Requests-OAuthlib을 사용한 코드와 비교하면 전체적인 흐름이 비스
- 다른점은 REST API의 URL 지정이 home_timeline() 메소드로 추상화
- 트윗을 나타내는 객체가 dict가 아니라 Tweepy의 Status 객체이다


```python
# ! pip install tweepy
```


```python
import os
import tweepy

# 환경변수에서 인증 정보를 추출합니다.
# CONSUMER_KEY = os.environ['CONSUMER_KEY']
# CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
# ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
# ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']
CONSUMER_KEY        = twitter_key.CONSUMER_KEY
CONSUMER_SECRET     = twitter_key.CONSUMER_SECRET
ACCESS_TOKEN        = twitter_key.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = twitter_key.ACCESS_TOKEN_SECRET

# 인증 정보를 설정합니다.
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# API 클라이언트를 생성합니다.
api = tweepy.API(auth)

# 사용자의 타임라인을 추출합니다.
public_tweets = api.home_timeline()

for status in public_tweets:
    # 사용자 이름과 트윗을 출력합니다.
    print('@' + status.user.screen_name, status.text)

```

#### <font color='#0000FF'> c5-05_streaming_api_with_tweepy </font>
> Tweepy 로 Streaming API 사용
- 연결 확립한 상태로 메시지 계속 전송
- 각 메시지는 줄바꿈 코드 CRLF로 구분
- 메시지는 대부분 트윗을 나타내는 JSON 형식의 문자열
- 트윗 이외의 연결을 유지하기 위한 공백과 메타 정보도 전송된다.

``` python 
import os
import tweepy

# 환경변수에서 인증 정보를 추출합니다.
# CONSUMER_KEY = os.environ['CONSUMER_KEY']
# CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
# ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
# ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']
CONSUMER_KEY        = twitter_key.CONSUMER_KEY
CONSUMER_SECRET     = twitter_key.CONSUMER_SECRET
ACCESS_TOKEN        = twitter_key.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = twitter_key.ACCESS_TOKEN_SECRET

# 인증 정보를 설정합니다.
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

class MyStreamListener(tweepy.StreamListener):
    """
    Streaming API로 추출한 트윗을 처리하는 클래스입니다.
    """
    def on_status(self, status):
        """
        트윗을 받을 때 호출되는 메서드
        매개변수로 트윗을 나타내는 Status 객체가 전달됩니다.
        """
        print('@' + status.author.screen_name, status.text)
        
# 인증 정보와 StreamListener를 지정해서 Stream 객체를 추출합니다.
stream = tweepy.Stream(auth, MyStreamListener())

# 공개돼 있는 트윗을 샘플링한 스트림을 받습니다.
# 키워드 매개변수인 languages로 한국어 트윗만 추출합니다
stream.sample(languages=['ko'])

```


```python
import os
import tweepy

# 환경변수에서 인증 정보를 추출합니다.
# CONSUMER_KEY = os.environ['CONSUMER_KEY']
# CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
# ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
# ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']
CONSUMER_KEY        = twitter_key.CONSUMER_KEY
CONSUMER_SECRET     = twitter_key.CONSUMER_SECRET
ACCESS_TOKEN        = twitter_key.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = twitter_key.ACCESS_TOKEN_SECRET

# 인증 정보를 설정합니다.
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

class MyStreamListener(tweepy.StreamListener):
    """
    Streaming API로 추출한 트윗을 처리하는 클래스입니다.
    """
    def on_status(self, status):
        """
        트윗을 받을 때 호출되는 메서드
        매개변수로 트윗을 나타내는 Status 객체가 전달됩니다.
        """
        print('@' + status.author.screen_name, status.text)

# 인증 정보와 StreamListener를 지정해서 Stream 객체를 추출합니다.
stream = tweepy.Stream(auth, MyStreamListener())

# 공개돼 있는 트윗을 샘플링한 스트림을 받습니다.
# 키워드 매개변수인 languages로 한국어 트윗만 추출합니다
stream.sample(languages=['ko'])
# stream.sample(languages=['en'])
```

<hr>
### <font color='#CC0000'> 유튜브에서 동영상 정보 수집 </font>
> Youtube Data API 버전 v3
- API로 동영상 업로드, 댓글 드의 처리하려면 OAuth 2.0 으로 인증해야 한다.
- 동영상 검색 또는 채널 내용 확인 등의 API는 API키로만 할 수 있다.
- 참고로 API로 추출할 수 있는 것은 동영상과 관련된 메타데이터 뿐이다.

#### <font color='#0000CC'> API 키 추출 </font>
> API 키를 추출하려면 구글 계정이 필요
- 구글 계정으로 로그인한 상태에서 <a href="https://console.developers.google.com/"><b>[ Googl API Console ]</b></a>에 들어가 새로운 프로젝트 생성
- Google API Consolo은 리소스를 프로젝트 단위로 관리
- API > 라이브러리 > YouTube Data API v3 에서, [사용 설정] 클릭
- [ 사용자 인증 정보 ] → [ API 키 ]를 눌러서 API키 를 생성
- 생성할 키의 종류를  [ 서버 키 ] 로 선택하고, 적당한 이름을 설정
- 키가 생성되면 API키가 출력되는데, 이를 복사해 둘 것!!


```python
from bigpycraft.oauth import youtube_key 

YOUTUBE_API_KEY = "AIzaSy*********************************"
YOUTUBE_API_KEY = youtube_key.API_KEY
```

#### <font color='#0000CC'> curl 명령어로 Youtube Data API 사용 </font>
> 
- Youtube Data API는 REST 형식의 간단한 API
- 간단한 URL을 조합해서 HTTP 요청을 보내면 JSON 형식으로 응답한다.

#### <font color='#0000CC'> Googld API Client for Python 사용 </font>
> 
- Youtube Data API는 간단한 REST API 이므로 Request 같은 라이브러리를 사용해도 문제없이 사용가능하다.
- 다만 구글 API를 범용적으로 사용할 때 Google API Client for Python을 사용하면 편리하다.

#### <font color='#0000FF'> c5-07_search_youtube_videos </font>
> 유튜브 동영상 검색하기


```python
# ! pip install google-api-python-client
```


```python
# ! pip install apiclient --upgrade
```


```python
# ! pip install discovery --upgrade
```


```python
# ! pip freeze

# msrest==0.5.4
# googlemaps==2.5.1
# anaconda-client==1.6.5
```


```python
# ! pip freeze

# msrest==0.5.4
# googlemaps==2.5.1
# anaconda-client==1.6.5
```


```python
# ! pip install --upgrade google-api-python-client
```


```python
# ! pip install googleapiclient
```


```python
# ! pip install --force-reinstall google-api-python-client
```

<hr>
### ImportError: No module named apiclient.discovery
> https://code.i-harness.com/ko-kr/q/116be65
<br/>
<br/>from apiclient.discovery import build
<br/>ImportError: No module named apiclient.discovery
<br/>
<br/>업데이트 : 수정 Nijjin의 도움을 따르십시오. 다음 폴더를 추가하여 문제를 해결했습니다.
<br/>apiclient, gflags, httplib2, oauth2client, uritemplate



```python
from bigpycraft.oauth import youtube_key 
import os

# pip install google-api-python-client
# google-api-python-client -> googleapiclient 
from apiclient.discovery import build

# 환경변수에서 API 키 추출하기
# YOUTUBE_API_KEY = os.environ['YOUTUBE_API_KEY']
YOUTUBE_API_KEY = youtube_key.API_KEY

# YouTube API 클라이언트를 생성합니다.
# build() 함수의 첫 번째 매개변수에는 API 이름
# 두 번째 매개변수에는 API 버전을 지정합니다.
# 키워드 매개변수 developerKey에는 API 키를 지정합니다.
# 이 함수는 내부적으로 https://www.googleapis.com/discovery/v1/apis/youtube/v3/rest라는
# URL에 접근하고 API 리소스와 메서드 정보를 추출합니다.
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

# 키워드 매개변수로 매개변수를 지정하고
# search.list 메서드를 호출합니다.
# list() 메서드를 실행하면 googleapiclient.http.HttpRequest가 반환됩니다. 
# execute() 메서드를 실행하면 실제 HTTP 요청이 보내지며, API 응답이 반환됩니다.
search_response = youtube.search().list(
    part='snippet',
    q='요리',
    type='video',
).execute()

# search_response는 API 응답을 JSON으로 나타낸 dict 객체입니다.
for item in search_response['items']:
    # 동영상 제목을 출력합니다.
    print(item['snippet']['title'])
```

#### <font color='#0000FF'> c5-08_save_youtube_video_metadata </font>
> 동영상 정보를 MongoDB에 저장하고 검색하기

<hr>
``` python
import os
import sys

from apiclient.discovery import build
from pymongo import MongoClient, DESCENDING

# 환경변수에서 API 키를 추출합니다.
YOUTUBE_API_KEY = os.environ['YOUTUBE_API_KEY']

def main():
    """
    메인 처리
    """
    # MongoDB 클라이언트 객체를 생성합니다.
    mongo_client = MongoClient('localhost', 27017)
    # youtube 데이터베이스의 videos 콜렉션을 추출합니다.
    collection = mongo_client.youtube.videos
    # 기존의 모든 문서를 제거합니다.
    collection.delete_many({})
    
    # 동영상을 검색하고, 페이지 단위로 아이템 목록을 저장합니다.
    for items_per_page in search_videos('요리'):
        save_to_mongodb(collection, items_per_page)
    
    # 뷰 수가 높은 동영상을 출력합니다.
    show_top_videos(collection)

def search_videos(query, max_pages=5):
    """
    동영상을 검색하고, 페이지 단위로 list를 yield합니다.
    """
    # YouTube의 API 클라이언트 생성하기
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)  
    # search.list 메서드로 처음 페이지 추출을 위한 요청 전송하기
    search_request = youtube.search().list(
        part='id',  # search.list에서 동영상 ID만 추출해도 괜찮음
        q=query,
        type='video',
        maxResults=50,  # 1페이지에 최대 50개의 동영상 추출
    )
    # 요청이 성공하고 페이지 수가 max_pages보다 작을 때 반복
    # 페이지 수를 제한하는 것은 실행 시간이 너무 길어지는 것을 막기 위해서입니다.
    # 더 많은 페이지를 요청해도 상관없습니다
    i = 0
    while search_request and i < max_pages:
        # 요청을 전송합니다.
        search_response = search_request.execute()
            # 동영상 ID의 리스트를 추출합니다.
            video_ids = [item['id']['videoId'] for item in search_response['items']]
        # videos.list 메서드로 동영상의 상세 정보를 추출합니다.
        videos_response = youtube.videos().list(
            part='snippet,statistics',
            id=','.join(video_ids)
        ).execute()
        # 현재 페이지 내부의 아이템을 yield합니다.
        yield videos_response['items']
        
        # list_next() 메서드로 다음 페이지를 추출하기 위한 요청을 보냅니다.
        search_request = youtube.search().list_next(search_request, search_response)
        i += 1

def save_to_mongodb(collection, items):
    """
    MongoDB에 아이템을 저장합니다.
    """
    # MongoDB에 저장하기 전에 이후에 사용하기 쉽게 아이템을 가공합니다.
    for item in items:
        # 각 아이템의 id 속성을 _id 속성으로 사용합니다.
        item['_id'] = item['id']  
        # statistics에 포함된 viewCount 속성 등은 문자열이므로 숫자로 변환합니다.
        for key, value in item['statistics'].items():
            item['statistics'][key] = int(value)
    
    # 콜렉션에 추가합니다.
    result = collection.insert_many(items)
    print('Inserted {0} documents'.format(len(result.inserted_ids)), file=sys.stderr)

def show_top_videos(collection):
    """
    MongoDB의 콜렉션 내부에서 뷰 수를 기준으로 상위 5개를 출력합니다.
    """
    for item in collection.find().sort('statistics.viewCount', DESCENDING).limit(5):
        print(item['statistics']['viewCount'], item['snippet']['title'])

if __name__ == '__main__':
    main()

```


<hr>
### <font color='0000CC'> 시계열 데이터 수집하고 활용 </font>
> 
* 환율 데이터 수집


### <font color='#CC0000'> 환율 데이터 수집 </font>
> 환율 데이터는 국적이 없다 ^^
- 환율 데이터 다운로드, FRED Economic Data
- <a href="https://fred.stlouisfed.org/series/DEXKOUS">[ South Korea / U.S. Foreign Exchange Rate ]</a>
- 기간에서 최대기간 [Max] 선택 후 CSV 형식으로 데이터 DOWNLOAD



```python
df_exchange = pd.read_csv('data/DEXKOUS.csv')
```


```python
df_exchange.head()
```


```python
df_exchange.DEXKOUS[0]
```

### <font color='#CC0000'> 국가 통계 포털 </font>
> 주제별 통계 [고용, 노동, 임금]
- <a href="http://kosis.kr/search/search.do">[ KOSIS, 국가통계포털 ]</a> : 연령별 경제활동인구 총괄
- [시점] 을 클릭하고, 년간 기간을 선택하고 데이터를 추출한다.
- 우측상단 [통계표조회]를 누른뒤에, 바로 아래 [다운로드] 버튼을 누르고 엑셀(xlsx)로 파일을 다운로드




```python
df_jobs = pd.read_excel('data/gugik.xlsx')
```


```python
df_jobs.head()
```


```python
df_jobs.stack()[6]
```


```python
df_jobs.stack()[6].index
```

#### <font color='#0000FF'> c5-11_plot_advanced_graph </font>
> 다양한 매개변수를 지정해서 그래프 그리기

``` python 
import matplotlib

# 렌더링 백엔드로 데스크톱 환경이 필요 없는 Agg를 사용합니다.
matplotlib.use('Agg')

# 한국어를 렌더링할 수 있게 폰트를 지정합니다.
# macOS와 우분투 모두 정상적으로 출력하도록 2개의 폰트를 지정했습니다.
# 기본 상태에서는 한국어가 □로 출력됩니다.
matplotlib.rcParams['font.sans-serif'] = 'NanumGothic,AppleGothic'

import matplotlib.pyplot as plt

```



```python
import platform

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

%matplotlib inline
plt.rcParams["figure.figsize"] = [8,6]
```


```python
# plot()의 세 번째 매개변수로 계열 스타일을 나타내는 문자열을 지정합니다.
# 'b'는 파란색, 'x'는 × 표시 마커, '-'는 마커를 실선으로 연결하라는 의미입니다.
# 키워드 매개변수 label로 지정한 계열의 이름은 범례로 사용됩니다.
plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5],   'bx-', label='첫 번째 함수')

# 'r'은 붉은색,'o'는 ○ 표시 마커, '--'는 점선을 의미합니다.
plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], 'ro--', label='두 번째 함수')
# xlabel() 함수로 X축의 레이블을 지정합니다.
plt.xlabel('X 값')
# ylabel() 함수로 Y축의 레이블을 지정합니다.
plt.ylabel('Y 값')
# title() 함수로 그래프의 제목을 지정합니다.
plt.title('matplotlib 샘플')
# legend() 함수로 범례를 출력합니다. loc='best'는 적당한 위치에 출력하라는 의미입니다.
plt.legend(loc='best')

# X축 범위를 0~6으로 지정합니다. ylim() 함수를 사용하면 Y축 범위를 지정할 수 있습니다.
plt.xlim(0, 6)

# 그래프를 그리고 파일로 저장합니다.
plt.savefig('advanced_graph.png', dpi=300)
plt.show()
```

#### <font color='#0000FF'> c5-12_plot_historical_data </font>
> 데이터 시각화

<hr>
``` python
from datetime import datetime
import pandas as pd
import matplotlib

matplotlib.use('Agg') 
matplotlib.rcParams['font.sans-serif'] = 'NanumGothic,AppleGothic' 
import matplotlib.pyplot as plt

def main():
    # 1981년과 2014년 사이의 환율과 고용률을 출력해 봅니다. 
    # 조금 이해하기 쉽게 Pandas 대신 기본 숫자 비교와 문자열 비교를 사용해 봤습니다.
    # 환율 정보 읽어 들이기
    df_exchange = pd.read_csv('data/DEXKOUS.csv', header=1, 
        names=['DATE', 'DEXKOUS'], skipinitialspace=True, index_col=0)
    years = {}
    output = []
    for index in df_exchange.index:
        year = int(index.split('-')[0])
        if (year not in years) and (1981 < year < 2014):
            if df_exchange.DEXKOUS[index] != ".":
                years[year] = True
                output.append([year, float(df_exchange.DEXKOUS[index])])
    df_exchange = pd.DataFrame(output)

    # 고용률 통계를 구합니다.
    df_jobs = pd.read_excel('data/gugik.xlsx') 
    output = []
    stacked = df_jobs.stack()[7]
    for index in stacked.index:
        try:
            if 1981 <= int(index) <= 2014:
                output.append([int(index), float(stacked[index])])
        except:
            pass
    s_jobs = pd.DataFrame(output)

    # 첫 번째 그래프 그리기
    plt.subplot(2, 1, 1)
    plt.plot(df_exchange[0], df_exchange[1], label='원/달러') 
    plt.xlim(1981, 2014) # X축의 범위를 설정합니다.
    plt.ylim(500, 2500)
    plt.legend(loc='best')
    
    # 두 번째 그래프 그리기
    print(s_jobs)
    plt.subplot(2, 1, 2) # 3 1 の3 のサブプロットを作成。 
    plt.plot(s_jobs[0], s_jobs[1], label='고용률(%)') 
    plt.xlim(1981, 2014) # X축의 범위를 설정합니다.
    plt.ylim(0, 100) # Y축의 범위를 설정합니다.
    plt.legend(loc='best')
    plt.savefig('historical_data.png', dpi=300) # 이미지를 저장합니다.

if __name__ == '__main__': 
    main()
    
```


```python
import platform

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

%matplotlib inline
plt.rcParams["figure.figsize"] = [8,6]
```


```python
# 1981년과 2014년 사이의 환율과 고용률을 출력해 봅니다. 
# 조금 이해하기 쉽게 Pandas 대신 기본 숫자 비교와 문자열 비교를 사용해 봤습니다.
# 환율 정보 읽어 들이기
df_exchange = pd.read_csv('data/DEXKOUS.csv', header=1, 
    names=['DATE', 'DEXKOUS'], skipinitialspace=True, index_col=0)
years = {}
output = []
for index in df_exchange.index:
    year = int(index.split('-')[0])
    if (year not in years) and (1981 < year < 2014):
        if df_exchange.DEXKOUS[index] != ".":
            years[year] = True
            output.append([year, float(df_exchange.DEXKOUS[index])])
df_exchange = pd.DataFrame(output)

# 고용률 통계를 구합니다.
df_jobs = pd.read_excel('data/gugik.xlsx') 
output = []
stacked = df_jobs.stack()[7]
for index in stacked.index:
    try:
        if 1981 <= int(index) <= 2014:
            output.append([int(index), float(stacked[index])])
    except:
        pass
s_jobs = pd.DataFrame(output)

# 첫 번째 그래프 그리기
plt.subplot(2, 1, 1)
plt.plot(df_exchange[0], df_exchange[1], label='원/달러') 
plt.xlim(1981, 2014) # X축의 범위를 설정합니다.
plt.ylim(500, 2500)
plt.legend(loc='best')

# 두 번째 그래프 그리기
# print(s_jobs)
plt.subplot(2, 1, 2) # 3 1 の3 のサブプロットを作成。 
plt.plot(s_jobs[0], s_jobs[1], label='고용률(%)') 
plt.xlim(1981, 2014) # X축의 범위를 설정합니다.
plt.ylim(0, 100) # Y축의 범위를 설정합니다.
plt.legend(loc='best')
plt.savefig('historical_data.png', dpi=300) # 이미지를 저장합니다.
plt.show()
```

<hr>
### <font color='0000CC'> 열린 데이터 수집과 활용 </font>
> Open Data : 정부, 자치단체, 기업 등이 보유하고 있는 데이터를 공개해서 자유롭게 활용할 수 있게 하는 것
- 공공 데이터 포털 : https://www.data.go.kr/
- 서울 데이터 열린광장 : http://data.seoul.go.kr/

<hr>
### <font color='0000CC'> 웹 페이지 자동 조작 </font>
> 브라우저를 조작하는 것처럼 실제로 웹페이지에 조작을 지시해서 크롤링하는 방법
- 자동 조작을 할때는 Requests 모듈의 Session 객체를 활용해도 좋다.
- RoboBrowser는 내부적으로 BeautifulSoup를 사용한다.


#### <font color='#0000FF'> c5-21_robobrowser_google </font>
> RoboBrowser로 구글 검색
- 구글 메인 페이지 오픈 : https://www.google.co.kr/search?q=검색어
- 검색 키워드 입력
- 검색 버튼 클릭
- 검색 결과 확인


```python
! pip install robobrowser
```


```python
from robobrowser import RoboBrowser

# RoboBrowser 객체를 생성합니다.
# 키워드 매개변수 parser는 BeautifulSoup()의 두 번째 매개변수와 같습니다.
# browser = RoboBrowser(parser='html.parser')
browser = RoboBrowser(parser='lxml')

# open() 메서드로 구글 메인 페이지를 엽니다.
browser.open('https://www.google.co.kr/')

# 키워드를 입력합니다.
form = browser.get_form(action='/search')
# form['q'] = 'Python'
form['q'] = 'BigData'
browser.submit_form(form, list(form.submit_fields.values())[0])

# 검색 결과 제목을 추출합니다.
# select() 메서드는 BeautifulSoup의 select() 메서드와 같습니다.
for a in browser.select('h3 > a'):
    print(a.text)
    print(a.get('href'))
    print()
```

<hr>
#### <font color='#0000FF'> c5-22_naver_order_history </font>
> 네이버페이지 주문 이력 추출
- 로그인이 필요한 웹사이트에서 데이터 크롤링 할때 RoboBrowser 등을 활용해야 한다.
- 네이버페이 주문 이력 페이지는 내부적으로 자바스크립트를 사용해 과거의 주문 이력을 가져온다.

<hr>
``` python 
import time
import sys
import os
from robobrowser import RoboBrowser

# 인증 정보를 환경변수에서 추출합니다.
NAVER_ID       = os.environ['NAVER_ID']
NAVER_PASSWORD = os.environ['NAVER_PASSWORD']

# from bigpycraft.oauth import naver_key
# NAVER_ID        = naver_key.NAVER_ID
# NAVER_PASSWORD  = naver_key.NAVER_PW

# RoboBrowser 객체를 생성합니다.
browser = RoboBrowser(
    # Beautiful Soup에서 사용할 파서를 지정합니다.
    parser='html.parser',
    # 일반적인 웹 브라우저의 User-Agent(FireFox)를 사용합니다.
    user_agent='Mozilla/5.0 (Macintosh; Intel Mac macOS 10.10; rv:45.0) Gecko/20100101 Firefox/45.0')

def main():
    # 로그인 페이지를 엽니다.
    print('Accessing to sign in page....', file=sys.stderr)
    browser.open('https://nid.naver.com/nidlogin.login')
    
    # 로그인 페이지에 들어가졌는지 확인합니다.
    assert '네이버 : 로그인' in browser.parsed.title.string
    
    # name='frmNIDLogin'이라는 입력 양식을 채웁니다.
    # 입력 양식의 name 속성은 개발자 도구로 확인할 수 있습니다.
    form = browser.get_form(attrs={'name': 'frmNIDLogin'})
    
    # name='id'라는 입력 양식을 채웁니다.
    form['id'] = NAVER_ID
    # name='pw'라는 입력 양식을 채웁니다.
    form['pw'] = NAVER_PASSWORD
    
    # 입력 양식을 전송합니다.
    # 로그인 때 로그인을 막는 것을 회피하고자 몇 가지 추가 정보를 전송합니다.
    print('Signing in...', file=sys.stderr)
    browser.submit_form(form, headers={
        'Referer': browser.url,
        'Accept-Language': 'ko,en-US;q=0.7,en;q=0.3',
    })
    
    # 주문 이력 페이지를 엽니다.
    browser.open('https://order.pay.naver.com/home?tabMenu=SHOPPING&frm=s_order')
    
    # 문제가 있을 경우 HTML 소스코드를 확인할 수 있게 출력합니다.
    # print(browser.parsed.prettify())
    # 주문 이력 페이지가 맞는지 확인합니다.
    assert '네이버페이' in browser.parsed.title.string
    # 주문 이력을 출력합니다.
    print_order_history()

def print_order_history():
    """
    주문 이력을 출력합니다.
    """
    # 주문 이력을 순회합니다: 클래스 이름은 개발자 도구로 확인합니다.
    for item in browser.select('.p_info'):
        # 주문 이력 저장 전용 dict입니다.
        order = {} 
        # 주문 이력의 내용을 추출합니다.
        name_element = item.select_one('span')
        date_element = item.select_one('.date')
        price_element = item.select_one('em')
        # 내용이 있을 때만 저장합니다.
        if name_element and date_element and price_element:
            name = name_element.get_text().strip()
            date = date_element.get_text().strip()
            price = price_element.get_text().strip()
            order[name] = {
                'date': date,
                'price': price
            }
            print(order[name]['date'], '-', order[name]['price'] + '원')

if __name__ == '__main__':
    main()
    
```

<hr>
### <font color='0000CC'> 자바스크립트를 이용한 페이지 스크레이핑 </font>
> 자바스크립트를 해석할 때는 Selenium과 WebBrowser를 조합하는 것이 일반적
- Selenium : 다양한 브라우저를 자동 조작하는 도구
- 웹 애플리케이션 자동 테스트 도구로 개발됐지만, 자바스크립트를 활요한 웹페이지 크롤링에도 자주 사용된다.
- 화면이 없는 웹브라우저(Headless Browser) 중 대표적인 것이 PhantomJS 이다.
- 가능하면 구글크롭 웹브라우저를 사용하기를 강추한다.


#### <font color='#0000FF'> c5-23_selenium_google </font>
> Selenium으로 구글 검색


```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# PhantomJS 모듈의 WebDriver 객체를 생성합니다.
# driver = webdriver.PhantomJS()
driver_path = "../driver/chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)

# Google 메인 페이지를 엽니다.
driver.get('https://www.google.co.kr/')

# 타이틀에 'Google'이 포함돼 있는지 확인합니다.
assert 'Google' in driver.title

# 검색어를 입력하고 검색합니다.
input_element = driver.find_element_by_name('q')
input_element.send_keys('Python')
input_element.send_keys(Keys.RETURN)

# 타이틀에 'Python'이 포함돼 있는지 확인합니다.
assert 'Python' in driver.title

# 스크린샷을 찍습니다.
driver.save_screenshot('search_results.png')

# 검색 결과를 출력합니다.
for a in driver.find_elements_by_css_selector('h3 > a'):
    print(a.text)
    print(a.get_attribute('href'))
    print()
    
```

<hr>
### <font color='0000CC'> 추출한 데이터 활용 </font>
> 
* 지도로 시각화
* 구글 BigQuery를 사용해 대량의 데이터를 빠르게 처리

#### <font color='#CC0000'> 지도로 시각화 </font>
> 
* Google Maps JavaScript API를 사용해 위치 정보를 지도에 시각적으로 출력
<br/> Developer Guide : https://developers.google.com/maps/documentation/geocoding/intro
<br/><br/>
* 주소를 입력하면 위도,경도를 알려주는 지오코딩 API를 사용
<br/> DashBoard :https://console.developers.google.com/projectselector/apis/api/geocoding_backend
<br/><br/>
<br/> - 프로젝트 생성
<br/> - 프로젝트에 사용자 인증 정보 추가


<hr>
``` python
import time
import sys
import os
import json
import dbm
from urllib.request import urlopen
from urllib.parse import urlencode
from SPARQLWrapper import SPARQLWrapper

def main():
    features = []  # 박물관 정보 저장을 위한 리스트
    for museum in get_museums():
        # 레이블이 있는 경우에는 레이블, 없는 경우에는 s를 추출합니다.
        label = museum.get('label', museum['s'])
        address = museum['address']
        lng, lat = geocode(address)
        
        # 값을 출력해 봅니다.
        print(label, address, lng, lat)
        # 위치 정보를 추출하지 못 했을 경우 리스트에 추가하지 않습니다.
        if lng is None:
            continue
        
        # features에 박물관 정보를 GeoJSON Feature 형식으로 추가합니다.
        features.append({
            'type': 'Feature',
            'geometry': {'type': 'Point', 'coordinates': [lng, lat]},
            'properties': {'label': label, 'address': address},
        })

    # GeoJSON FeatureCollection 형식으로 dict를 생성합니다.
    feature_collection = {
        'type': 'FeatureCollection',
        'features': features,
    }
    # FeatureCollection을 .geojson이라는 확장자의 파일로 저장합니다.
    with open('museums.geojson', 'w') as f:
        json.dump(feature_collection, f)

def get_museums():
    """
    SPARQL을 사용해 DBpedia에서 박물관 정보 추출하기
    """
    print('Executing SPARQL query...', file=sys.stderr)
    
    # SPARQL 엔드 포인트를 지정해서 인스턴스를 생성합니다.
    sparql = SPARQLWrapper('http://ko.dbpedia.org/sparql')
    
    # 한국의 박물관을 추출하는 쿼리입니다.
    sparql.setQuery('''
    SELECT * WHERE {
        ?s rdf:type dbpedia-owl:Museum .
        ?s prop-ko:소재지 ?address .
        OPTIONAL { ?s rdfs:label ?label . }
    } ORDER BY ?s
    ''')

    # 반환 형식을 JSON으로 지정합니다.
    sparql.setReturnFormat('json')

    # query()로 쿼리를 실행한 뒤 convert()로 파싱합니다.
    response = sparql.query().convert()
    print('Got {0} results'.format(len(response['results']['bindings']), file=sys.stderr))
    # 쿼리 결과를 반복 처리합니다.
    for result in response['results']['bindings']:
        # 다루기 쉽게 dict 형태로 변환해서 yield합니다.
        yield {name: binding['value'] for name, binding in result.items()}

# Google Geolocation API
GOOGLE_GEOCODER_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json'
# DBM(파일을 사용한 Key-Value 데이터베이스)로 지오코딩 결과를 캐시합니다.
# 이 변수는 dict처럼 다룰 수 있습니다.
geocoding_cache = dbm.open('geocoding.db', 'c')

def geocode(address):
    """
    매개변수로 지정한 주소를 지오코딩해서 위도와 경도를 반환합니다.
    """
    if address not in geocoding_cache:
        # 주소가 캐시에 존재하지 않는 경우 지오코딩합니다.
        print('Geocoding {0}...'.format(address), file=sys.stderr)
        time.sleep(1)
        url = GOOGLE_GEOCODER_API_URL + '?' + urlencode({
            'key': os.environ['GOOGLE_API_ID'],
            'language': 'ko',
            'address': address,
        })
        response_text = urlopen(url).read()
        # API 응답을 캐시에 저장합니다.
        # 문자열을 키와 값에 넣으면 자동으로 bytes로 변환합니다.
        geocoding_cache[address] = response_text
    
    # 캐시 내의 API 응답을 dict로 변환합니다.
    # 값은 bytes 자료형이므로 문자열로 변환합니다.
    response = json.loads(geocoding_cache[address].decode('utf-8'))
    try:
        # JSON 형식에서 값을 추출합니다.
        lng = response['results'][0]['geometry']['location']['lng']
        lat = response['results'][0]['geometry']['location']['lat']
        # float 형태로 변환한 뒤 튜플을 반환합니다.
        return (float(lng), float(lat))
    except:
        return (None, None)

if __name__ == '__main__':
    main()
    
```

<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
