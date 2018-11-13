
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
    <option value="CH04" selected> 04.크롤러를 사용할 때 기억해야 하는 것           </option>
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

## <font color='#0000AA'>크롤러 사용할 때 기억해야 하는 것 </font>
>   
<font color='#0000CC'>
- 크롤러 분류하기
- 크롤러 만들때 주의해야 하는 것
- 여러 번 사용을 전제로 설계하기
- 크롤링 대상의 변화에 대응하기

<hr>
### <font color='#0000CC'> 크롤러 분류하기 </font>
> 3가지 분류기준
- 상태를 가지고 있는지 : Statefull, Stateless
- 자바스크립트를 실행할 수 있는지
- 불특정 다수의 사이트를 대상으로 하는지

cf. Selenium : 브라우저를 자동으로 조작할 수 있게 해주는 도구

<hr>
### <font color='#0000CC'> 크롤러 만들때 주의해야 하는 것 </font>
> 
* robots.txt : Robots Exclusion Protocol 
<br/> - 웹사이트 최상위 디렉토리에 배치
<br/> - 디렉티브 : User-agent, Disallow, Allow, Sitemap, Crawl-delay

#### <font color='#0000FF'> robots.txt 파싱
> ** RobotFileParser ** : robots.txt를 파싱하기 위한 urllib.robotparser


```python
import urllib.robotparser

rp = urllib.robotparser.RobotFileParser()
```


```python
url = 'http://wikibook.co.kr'
url = 'https://www.google.com'

rp_url = url + '/robots.txt'
print(rp_url)

rp.set_url(rp_url)
rp.read()
```


```python
# 해당 URL을 크롤링해도 괜찮은지 확인
rp.can_fetch('mybot', url)
```

``` python
Signature: rp.can_fetch(useragent, url)
Docstring: using the parsed robots.txt decide if useragent can fetch url
```
<hr>

#### <font color='#0000FF'> c4-07_error_handling </font>
> 상태코드에 맞는 오류 처리


```python
import time
import requests
# 일시적인 오류를 나타내는 상태 코드를 지정합니다.
TEMPORARY_ERROR_CODES = (408, 500, 502, 503, 504)  

def main():
    """
    메인 처리입니다.
    """
    response = fetch('http://httpbin.org/status/200,404,503')
    if 200 <= response.status_code < 300:
        print('Success!')
    else:
        print('Error!')

def fetch(url):
    """
    지정한 URL에 요청한 뒤 Response 객체를 반환합니다.
    일시적인 오류가 발생하면 최대 3번 재시도합니다.
    """
    max_retries = 3  # 최대 3번 재시도합니다.
    retries = 0      # 현재 재시도 횟수를 나타내는 변수입니다.
    
    while True:
        try:
            print('Retrieving {0}...'.format(url))
            response = requests.get(url)
            print('Status: {0}'.format(response.status_code))
            if response.status_code not in TEMPORARY_ERROR_CODES:
                return response  # 일시적인 오류가 아니라면 response를 반환합니다.
            
        except requests.exceptions.RequestException as ex:
            # 네트워크 레벨 오류(RequestException)의 경우 재시도합니다.
            print('Exception occured: {0}'.format(ex))
            retries += 1
            if retries >= max_retries:
                # 재시도 횟수 상한을 넘으면 예외를 발생시켜버립니다.
                raise Exception('Too many retries.')  
            # 지수 함수적으로 재시도 간격을 증가합니다(**는 제곱 연산자입니다).
            wait = 2**(retries - 1)  
            print('Waiting {0} seconds...'.format(wait))
            time.sleep(wait)  # 대기합니다.

if __name__ == '__main__':
    main()
    
```


```python
url = 'http://www.google.com'
fetch(url)
```


```python
url = 'http://www.naver.com'
fetch(url)
```


```python
url = 'http://www.nagooglever.com'
fetch(url)
```


```python
url = 'http://www.notexist.kr'
fetch(url)
```

<hr>
#### <font color='#0000FF'> c4-08_error_handling_with_retrying </font>
> retrying을 이용한 재시도 처리


```python
# ! pip install retrying
```


```python
import requests
from retrying import retry  
import time

# 일시적인 오류를 나타내는 상태 코드를 지정합니다.
TEMPORARY_ERROR_CODES = (408, 500, 502, 503, 504)  

def main():
    """
    메인 처리입니다.
    """
    response = fetch('http://httpbin.org/status/200,404,503')
    if 200 <= response.status_code < 300:
        print('Success!')
    else:
        print('Error!')

        
# decorator 
# stop_max_attempt_number로 최대 재시도 횟수를 지정합니다.
# wait_exponential_multiplier로 특정한 시간 만큼 대기하고 재시도하게 합니다. 단위는 밀리초로 입력합니다.
@retry(stop_max_attempt_number=3, wait_exponential_multiplier=1000)
def fetch(url):
    """
    지정한 URL에 접근한 뒤 Response 객체를 반환합니다.
    일시적인 오류가 발생할 경우 3번까지 재시도합니다.
    """
    print('Retrieving {0}...'.format(url))
    response = requests.get(url)
    print('Status: {0}'.format(response.status_code))
    if response.status_code not in TEMPORARY_ERROR_CODES:
        # 오류가 없다면 response를 반환합니다.
        return response
    # 오류가 있다면 예외를 발생시킵니다.
    raise Exception('Temporary Error: {0}'.format(response.status_code))

if __name__ == '__main__':
    main()
```
<!--
from retrying import retry
from random import randint

@retry(stop_max_attempt_number=3)
def a():
    number = randint(0, 10)

    if number > 0:
        print(number)
        raise Exception("Some exception")
    else:
        print('*'*5)
        return number

# Case 1
a = retry(a)      # This works as expected - i.e. execs until I get a 0
print(a())

print('-'*5)
# Case 2
# a = retry(a, stop_max_attempt_number=3)
# print(a())
//-->

```python
# decorator.py
# -*- coding: utf-8 -*-
def decorator_function(original_function):
    def wrapper_function():
        print('{} 함수가 호출되기전 입니다.'.format(original_function.__name__))
        return original_function()
    return wrapper_function


@decorator_function  #1
def display_1():
    print('display_1 함수가 실행됐습니다.')


@decorator_function  #2
def display_2():
    print('display_2 함수가 실행됐습니다.')

# display_1 = decorator_function(display_1)  #3
# display_2 = decorator_function(display_2)  #4

display_1()
print('-'*50)
display_2()
```

<hr>
### <font color='#0000CC'> 여러 번 사용을 전제로 설계하기 </font>
> 크롤링 도중에 오류가 발생했을때를 위한 처리
- 이후에 변경된 데이터를 추가로 추출할 수 있게 하기 위해
- 오류 등으로 중간에 중지되었을 때, 중간부터 다시 재개하기 위해

#### <font color='#0000FF'> c4-09_request_with_cache </font>
> CacheControl을 사용해 캐시 처리


```python
# ! pip install CacheControl
```


```python
import requests
from cachecontrol import CacheControl  

session = requests.session()

# session을 래핑한 cached_session 만들기
cached_session = CacheControl(session)

url = 'https://docs.python.org/3/'
# 첫 번째는 캐시돼 있지 않으므로 서버에서 추출한 이후 캐시합니다.
response = cached_session.get(url)
print(response.from_cache)

# 두 번째는 ETag와 Last-Modified 값을 사용해 업데이트됐는지 확인합니다.
# 변경사항이 없는 경우에는 콘텐츠를 캐시에서 추출해서 사용하므로 빠른 처리가 가능합니다.
response = cached_session.get(url)
print(response.from_cache) 
```


```python
response = cached_session.get(url)
print(response.from_cache) 
```

<hr>
### <font color='#0000CC'> 크롤링 대상의 변화에 대응하기 </font>
>  
- 변화 감지하기
- 변화 통지하기


<hr>
### <font color='#0000CC'> 변화 감지 </font>
#### <font color='#0000FF'> c4-10_validate_with_re </font>


```python
import re

value = '3,000'
value = '3천'

# 숫자와 쉼표만을 포함한 정규 표현식에 매치하는지 확인합니다.
if not re.search(r'^[0-9,]+$', value):
    # 값이 제대로 돼 있지 않다면 예외를 발생시킵니다.
    raise ValueError('Invalid price')
```


```python
# ! pip install voluptuous
```

#### <font color='#0000FF'> c4-11_validate_with_voluptuous </font>


```python
from voluptuous import Schema, Match  

# 다음 4개의 규칙을 가진 스키마를 정의합니다
schema = Schema({                  # 규칙1: 객체는 dict 자료형
    'name' : str,                  # 규칙2：name은 str(문자열) 자료형
    'price': Match(r'^[0-9,]+$'),  # 규칙3：price가 정규 표현식에 맞는지 확인
}, required=True)                  # 규칙4：dict의 키는 필수

```


```python
# Schema 객체는 함수처럼 호출해서 사용합니다.
# 매개변수에 대상을 넣으면 유효성 검사를 수행합니다.
schema({
    'name' : '포도',
    'price': '3,000',
})  # 유효성 검사를 통과하므로 아무 문제 없음

```


```python
# 유효성 검사를 통과하지 못 하므로, MultipleInvalid 예외가 발생
schema({
    'name' : None,
    'price': '3,000',
})  
```


```python
# 유효성 검사를 통과하지 못 하므로, MultipleInvalid 예외가 발생
schema({
    'name' : '오렌지',
    'price': '3천',
})  
```

<hr>
### <font color='#0000CC'> 변화 통지 </font>
#### <font color='#0000FF'> c4-12_send_email </font>

``` python 
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# MIMEText 객체로 메일을 생성합니다.
msg = MIMEText('메일 본분입니다.')  

# 제목에 한글이 포함될 경우 Header 객체를 사용합니다.
msg['Subject'] = Header('메일 제목입니다.', 'utf-8') 
msg['From']    = 'me@example.com'
msg['To']      = 'you@example.com'

# SMTP()의 첫 번째 매개변수에 SMTP 서버의 호스트 이름을 지정합니다.
with smtplib.SMTP('localhost') as smtp:
    # 메일을 전송합니다.
    smtp.send_message(msg)

'''
with smtplib.SMTP_SSL('smtp.gmail.com') as smtp:
    # 구글 계정의 사용자 이름과 비밀번호를 지정해서 로그인합니다.
    # 2단계 인증을 설정한 경우 애플리케이션 비밀번호를 사용해 주세요.
    smtp.login('사용자 이름', '비밀번호')
    # send_message() 메서드로 메일을 전송합니다.
    smtp.send_message(msg)
'''

```

<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
