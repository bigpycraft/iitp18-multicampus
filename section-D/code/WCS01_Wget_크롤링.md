
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
    <option value="CH01" selected> 01.크롤링과 스크레이핑이란?                      </option>
    <option value="CH02"> 02.파이썬으로 시작하는 크롤링/스크레이핑         </option>
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

## <font color='#0000AA'>크롤링과 스크레이핑 이란? </font>
>  
<font color='#0000CC'>
- 크롤링과 스크레이핑 개념
- Wget으로 크롤링
- UNIX / LINUX 명령어 


```python
! python --version
```

### <font color='0000CC'> 크롤링과 스크레이핑
* 크롤링 
<br/> - 웹 페이지의 하이퍼링크를 순회하면서 웹 페이지를 다운로드하는 작업
<br/><br/>
* 스크레이핑
<br/> - 다운로드한 웹 페이지에서 필요한 정보를 추출하는 작업

### <font color='0000CC'> Wget으로 크롤링
> GNU Wget : HTTP통신 또는 FTP 통신을 사용해 서버에서 파일 또는 콘텐츠를 다운로드할 때 사용하는 소프트웨어
* wget for windows : https://eternallybored.org/misc/wget/
* 사용법
<br/> - url 페이지 크롤링 : 화면에 출력, 파일에 저장
<br/> - wget option  ::  cf. 10page
<br/> - tree



```python
! wget --version
```


```python
# ! mkdir download
# 파일명에 -(하이픈)을 지정하면 파일로 저장하지 않고 표준 출력에 출력
! wget https://movie.naver.com/ -q -O -
```


```python
# 파일에 저장
! wget https://movie.naver.com/ -O ./download/naver_movie.html
```


```python
! tree
```


```python
! type .\download\naver_movie.html
```

### <font color='0000CC'> UNIX / LINUX Basics

#### 표준 스트림
>  기본적으로 표준 입력은 키보드에서의 입력, 표준 출력은 콘솔 화면으로 출력
<br/>
<br/> - 표준 출력 리다이렉트 : 명령어 실행 결과(표준 출력)을 파일에 저장하기
<br/>  &nbsp;&nbsp; \$ 명령어 > 경로
<br/>
<br/> - 표준 입력 리다이렉트 : 파일의 내용을 명령어의 표준 입력으로 지정하기
<br/>  &nbsp;&nbsp; \$ 명령어 < 경로


```python
% ls | grep .ipynb
```


```python
! pip freeze > packages.txt
```


```python
# ! cat packages.txt
! type packages.txt
```

<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
