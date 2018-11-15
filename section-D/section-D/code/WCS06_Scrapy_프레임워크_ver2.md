
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
    <option value="CH05"> 05.크롤링/스크레이핑 실전과 데이터 활용          </option>
    <option value="CH06" selected> 06.Scrapy 프레임워크                             </option>
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

## <font color='#0000AA'>Scrapy 프레임워크 </font>
>  
<font color='#0000CC'>
- Scrapy 개요
- Spider 만들고 실행하기
- 실전적인 크롤링
- 추출한 데이터 처리하기
- Scrapy 설정
- Scrapy 확장하기
- 크롤링으로 데이터 수집하고 활용하기
- 이미지 수집과 활용


<hr>
### <font color='0000CC'> Scrapy 개요 </font>
- 파이썬에서 제공하는 크롤링/스크레이핑 프레임워크
- Scrapy는 파이썬2에만 지원되었지만, 2016년 5월 배포된 1.1버전부터 파이썬3에도 지원 시작


```python
! pip install scrapy
```

    Requirement already satisfied: scrapy in c:\python\anaconda3-50\lib\site-packages (1.5.1)
    Requirement already satisfied: Twisted>=13.1.0 in c:\python\anaconda3-50\lib\site-packages (from scrapy) (18.7.0)
    Requirement already satisfied: w3lib>=1.17.0 in c:\python\anaconda3-50\lib\site-packages (from scrapy) (1.19.0)
    Requirement already satisfied: queuelib in c:\python\anaconda3-50\lib\site-packages (from scrapy) (1.5.0)
    Requirement already satisfied: lxml in c:\python\anaconda3-50\lib\site-packages (from scrapy) (4.1.0)
    Requirement already satisfied: pyOpenSSL in c:\python\anaconda3-50\lib\site-packages (from scrapy) (17.2.0)
    Requirement already satisfied: cssselect>=0.9 in c:\python\anaconda3-50\lib\site-packages (from scrapy) (1.0.3)
    Requirement already satisfied: six>=1.5.2 in c:\python\anaconda3-50\lib\site-packages (from scrapy) (1.11.0)
    Requirement already satisfied: parsel>=1.1 in c:\python\anaconda3-50\lib\site-packages (from scrapy) (1.5.0)
    Requirement already satisfied: PyDispatcher>=2.0.5 in c:\python\anaconda3-50\lib\site-packages (from scrapy) (2.0.5)
    Requirement already satisfied: service_identity in c:\python\anaconda3-50\lib\site-packages (from scrapy) (17.0.0)
    Requirement already satisfied: zope.interface>=4.4.2 in c:\python\anaconda3-50\lib\site-packages (from Twisted>=13.1.0->scrapy) (4.5.0)
    Requirement already satisfied: constantly>=15.1 in c:\python\anaconda3-50\lib\site-packages (from Twisted>=13.1.0->scrapy) (15.1.0)
    Requirement already satisfied: incremental>=16.10.1 in c:\python\anaconda3-50\lib\site-packages (from Twisted>=13.1.0->scrapy) (17.5.0)
    Requirement already satisfied: Automat>=0.3.0 in c:\python\anaconda3-50\lib\site-packages (from Twisted>=13.1.0->scrapy) (0.7.0)
    Requirement already satisfied: hyperlink>=17.1.1 in c:\python\anaconda3-50\lib\site-packages (from Twisted>=13.1.0->scrapy) (18.0.0)
    Collecting PyHamcrest>=1.9.0 (from Twisted>=13.1.0->scrapy)
      Downloading https://files.pythonhosted.org/packages/9a/d5/d37fd731b7d0e91afcc84577edeccf4638b4f9b82f5ffe2f8b62e2ddc609/PyHamcrest-1.9.0-py2.py3-none-any.whl (52kB)
    Requirement already satisfied: attrs>=17.4.0 in c:\python\anaconda3-50\lib\site-packages (from Twisted>=13.1.0->scrapy) (18.2.0)
    Requirement already satisfied: cryptography>=1.9 in c:\python\anaconda3-50\lib\site-packages (from pyOpenSSL->scrapy) (2.0.3)
    Requirement already satisfied: pyasn1-modules in c:\python\anaconda3-50\lib\site-packages (from service_identity->scrapy) (0.2.2)
    Requirement already satisfied: pyasn1 in c:\python\anaconda3-50\lib\site-packages (from service_identity->scrapy) (0.4.4)
    Requirement already satisfied: setuptools in c:\python\anaconda3-50\lib\site-packages (from zope.interface>=4.4.2->Twisted>=13.1.0->scrapy) (36.5.0.post20170921)
    Requirement already satisfied: idna>=2.5 in c:\python\anaconda3-50\lib\site-packages (from hyperlink>=17.1.1->Twisted>=13.1.0->scrapy) (2.6)
    Requirement already satisfied: asn1crypto>=0.21.0 in c:\python\anaconda3-50\lib\site-packages (from cryptography>=1.9->pyOpenSSL->scrapy) (0.22.0)
    Requirement already satisfied: cffi>=1.7 in c:\python\anaconda3-50\lib\site-packages (from cryptography>=1.9->pyOpenSSL->scrapy) (1.10.0)
    Requirement already satisfied: pycparser in c:\python\anaconda3-50\lib\site-packages (from cffi>=1.7->cryptography>=1.9->pyOpenSSL->scrapy) (2.18)
    Installing collected packages: PyHamcrest
    Successfully installed PyHamcrest-1.9.0
    


```python
! scrapy version
```

    Scrapy 1.5.1
    

<hr>
#### <font color='#0000FF'> c6-01_myspider.py </font>
> Scrapinghub 블로그에서 글의 타이틀을 추출하는 Spider
- 아래 myspider.py 코드는 Scrapy 사이트에서 제공하는 공식 예제 코드에 주석을 붙인 것이다.
- 실행 : scrapy runspider myspider.py -o items.j1

<hr>
``` python
%%writefile  ./modules/myspider.py
import scrapy

class BlogSpider(scrapy.Spider):
    # spider의 이름
    name = 'blogspider'

    # 크롤링을 시작할 URL 리스트
    start_urls = ['https://blog.scrapinghub.com']
    
    def parse(self, response):
        """
        최상위 페이지에서 카테고리 페이지의 링크를 추출합니다.
        """
        for url in response.css('ul li a::attr("href")').re('.*/category/.*'):
            yield scrapy.Request(response.urljoin(url), self.parse_titles)
    
    def parse_titles(self, response):
        """
        카페고리 페이지에서 카테고리 타이틀을 모두 추출합니다.
        """
        for post_title in response.css('div.entries > ul > li a::text').extract():
            yield {'title': post_title}

```


```python
%%writefile  ./modules/myspider.py
import scrapy

class BlogSpider(scrapy.Spider):
    # spider의 이름
    name = 'blogspider'

    # 크롤링을 시작할 URL 리스트
    start_urls = ['https://blog.scrapinghub.com']

    def parse(self, response):
        """
        최상위 페이지에서 카테고리 페이지의 링크를 추출합니다.
        """
        for url in response.css('ul li a::attr("href")').re('.*/category/.*'):
            yield scrapy.Request(response.urljoin(url), self.parse_titles)

    def parse_titles(self, response):
        """
        카페고리 페이지에서 카테고리 타이틀을 모두 추출합니다.
        """
        for post_title in response.css('div.entries > ul > li a::text').extract():
            yield {'title': post_title}
            
            
```

    Overwriting ./modules/myspider.py
    


```python
! scrapy runspider ./modules/myspider.py -o ./modules/data/items.jl
```

    2018-11-16 01:25:18 [scrapy.utils.log] INFO: Scrapy 1.5.1 started (bot: scrapybot)
    2018-11-16 01:25:18 [scrapy.utils.log] INFO: Versions: lxml 4.1.0.0, libxml2 2.9.4, cssselect 1.0.3, parsel 1.5.0, w3lib 1.19.0, Twisted 18.7.0, Python 3.6.3 |Anaconda custom (64-bit)| (default, Oct 15 2017, 03:27:45) [MSC v.1900 64 bit (AMD64)], pyOpenSSL 17.2.0 (OpenSSL 1.0.2p  14 Aug 2018), cryptography 2.0.3, Platform Windows-10-10.0.10586-SP0
    2018-11-16 01:25:18 [scrapy.crawler] INFO: Overridden settings: {'FEED_FORMAT': 'jl', 'FEED_URI': './modules/data/items.jl', 'SPIDER_LOADER_WARN_ONLY': True}
    2018-11-16 01:25:18 [scrapy.middleware] INFO: Enabled extensions:
    ['scrapy.extensions.corestats.CoreStats',
     'scrapy.extensions.telnet.TelnetConsole',
     'scrapy.extensions.feedexport.FeedExporter',
     'scrapy.extensions.logstats.LogStats']
    2018-11-16 01:25:19 [scrapy.middleware] INFO: Enabled downloader middlewares:
    ['scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
     'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
     'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
     'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
     'scrapy.downloadermiddlewares.retry.RetryMiddleware',
     'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
     'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
     'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
     'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
     'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
     'scrapy.downloadermiddlewares.stats.DownloaderStats']
    2018-11-16 01:25:19 [scrapy.middleware] INFO: Enabled spider middlewares:
    ['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
     'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
     'scrapy.spidermiddlewares.referer.RefererMiddleware',
     'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
     'scrapy.spidermiddlewares.depth.DepthMiddleware']
    2018-11-16 01:25:19 [scrapy.middleware] INFO: Enabled item pipelines:
    []
    2018-11-16 01:25:19 [scrapy.core.engine] INFO: Spider opened
    2018-11-16 01:25:19 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
    2018-11-16 01:25:19 [scrapy.extensions.telnet] DEBUG: Telnet console listening on 127.0.0.1:6023
    2018-11-16 01:25:19 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://blog.scrapinghub.com> (referer: None)
    2018-11-16 01:25:19 [scrapy.core.engine] INFO: Closing spider (finished)
    2018-11-16 01:25:19 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
    {'downloader/request_bytes': 219,
     'downloader/request_count': 1,
     'downloader/request_method_count/GET': 1,
     'downloader/response_bytes': 10274,
     'downloader/response_count': 1,
     'downloader/response_status_count/200': 1,
     'finish_reason': 'finished',
     'finish_time': datetime.datetime(2018, 11, 15, 16, 25, 19, 730045),
     'log_count/DEBUG': 2,
     'log_count/INFO': 7,
     'response_received_count': 1,
     'scheduler/dequeued': 1,
     'scheduler/dequeued/memory': 1,
     'scheduler/enqueued': 1,
     'scheduler/enqueued/memory': 1,
     'start_time': datetime.datetime(2018, 11, 15, 16, 25, 19, 533338)}
    2018-11-16 01:25:19 [scrapy.core.engine] INFO: Spider closed (finished)
    


```python
! type .\modules\data\items.jl
```

####  yield generator test source


```python
#python 3 version source
#yield generator test source
#yield_Basic_Test.py
 
def number_generator(n):
    print("Function Start")
    while n < 6:
        yield  {"n" : n}
        n += 1
    print("Function End")
     
if __name__ == "__main__":
    for i in number_generator(0):
        print(i)
         

```

    Function Start
    {'n': 0}
    {'n': 1}
    {'n': 2}
    {'n': 3}
    {'n': 4}
    {'n': 5}
    Function End
    

<hr>
### <font color='0000CC'> Spider 만들고 실행하기 </font>
* 타겟사이트 : https://www.engadget.com
* 명령어실행 : 
<br/> (base) C:\ > scrapy startproject myproject
* Item만들기

```
C:\> scrapy --help
Scrapy 1.5.1 - project: myproject

Usage:
  scrapy <command> [options] [args]

Available commands:
  bench         Run quick benchmark test
  check         Check spider contracts
  crawl         Run a spider
  edit          Edit spider
  fetch         Fetch a URL using the Scrapy downloader
  genspider     Generate new spider using pre-defined templates
  list          List available spiders
  parse         Parse URL (using its spider) and print the results
  runspider     Run a self-contained spider (without creating a project)
  settings      Get settings values
  shell         Interactive scraping console
  startproject  Create new project
  version       Print Scrapy version
  view          Open URL in browser, as seen by Scrapy

Use "scrapy <command> -h" to see more info about a command
```

```
# spider 만들기
C:\> mkdir webcrawler
C:\> cd webcralwer
C:\webcralwer> scrapy startproject myproject
C:\webcralwer> cd myproject
C:\webcralwer\myproject> tree

# pycharm or spyder 로 작업하는게 낫다
```


```python
# scrapy.cfg

# 페이지 다운로드 간격을 1초로 지정
DOWNLOAD_DELAY = 1

```


```python
# myproject/items.py
import scrapy

class Headline(scrapy.Item):
    """
    뉴스 헤드라인을 나타내는 Item 객체
    """
    title = scrapy.Field()
    body = scrapy.Field()

```

C:\webcralwer\myproject> scrapy genspider news engadget.com


```python
# myproject/spiders/news.py
import scrapy

class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['engadget.com']
    start_urls = ['http://engadget.com/']

    def parse(self, response):
        """
        메인 페이지의 토픽 목록에서 링크를 추출하고 출력합니다.
        """
        link = response.css('a.o-hit__link::attr("href")').extract()
        link = filter(lambda x : x != "#", link)
        link = list(link)
        print(link)
```

C:\webcralwer\myproject> scrapy crawl news



```python
# myproject/spiders/news.py
import scrapy


class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['engadget.com']
    start_urls = ['http://engadget.com/']

    def parse(self, response):
        """
        메인 페이지의 토픽 목록에서 링크를 추출하고 출력합니다.
        """
        link = response.css('a.o-hit__link::attr("href")').extract()
        # link = filter(lambda x : x != "#", link)
        # link = list(link)
        # print(link)

        for url in link:
            # 광고 페이지 제외
            if url.find("products") == 1:
                continue
            # 의미 없는 페이지 제외
            if url == "#":
                continue
            # 기사 페이지
            yield scrapy.Request(response.urljoin(url), self.parse_topics)

    def parse_topics(self, response):
        pass
```

C:\webcralwer\myproject> scrapy crawl news



```python
# -*- coding: utf-8 -*-
import scrapy
from webcrawler.wc06_2.myproject.items import Headline

class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['engadget.com']
    start_urls = ['http://engadget.com/']

    def parse(self, response):
        """
        메인 페이지의 토픽 목록에서 링크를 추출하고 출력합니다.
        """
        link = response.css('a.o-hit__link::attr("href")').extract()
        # link = filter(lambda x : x != "#", link)
        # link = list(link)
        # print(link)

        for url in link:
            # 광고 페이지 제외
            if url.find("products") == 1:
                continue
            # 의미 없는 페이지 제외
            if url == "#":
                continue
            # 기사 페이지
            yield scrapy.Request(response.urljoin(url), self.parse_topics)

    def parse_topics(self, response):
        pass
        item = Headline()
        item['title'] = response.css('head title::text').extract_first()
        item['body'] = " ".join(response.css('.o-article_block p')\
            .xpath('string()')\
            .extract())
        yield item

```

C:\webcralwer\myproject> scrapy shell https://www.engadget.com/2017/08/17/hyundai-shifts-focus-from-fuel-cell-cars-to-evs/

<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
