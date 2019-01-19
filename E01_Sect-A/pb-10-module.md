
# Industry 4.0 의 중심, BigData

<div align='right'><font size=2 color='gray'>Data Processing Based Python @ <font color='blue'><a href='https://www.facebook.com/jskim.kr'>FB / jskim.kr</a></font>, 김진수</font></div>
<hr>

## <font color='brown'>모듈과 패키지, Module & Package</font>
>  
- 모듈 이해하기
- 모듈 정의 및 불러오기
- 모듈을 파이썬 환경 밖에서 실행할 때
- dir() 함수를 통한 모듈 속 들여다 보기
- 모듈들의 집합, 패키지(Packages)

### 모듈 생성
> 피보나치 수열을 위한 모듈

- fibo.py


```python
def fib(n):
    '''
    n 까지의 피보나치 수열을 출력 하는 함수
    :param n: Integer
    :return:  None
    '''
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()


def fib2(n):
    '''
    n 까지의 피보나치 수열을 반환 하는  함수
    :param n: Integer
    :return: List
    '''
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

```

### 모듈 불러오기

- fibo_ex1.py


```python
import fibo
```


```python
fibo.fib(100)
```

    1 1 2 3 5 8 13 21 34 55 89 
    


```python
fib = fibo.fib
fib(200)
```

    1 1 2 3 5 8 13 21 34 55 89 144 
    

- fibo_ex2.py


```python
from fibo import *
```


```python
fib(300)
```

    1 1 2 3 5 8 13 21 34 55 89 144 233 
    


```python
fib2(400)
```




    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]



- fibo_ex3.py


```python
from fibo import fib as f1, fib2 as f2
```


```python
f1(500)
```

    1 1 2 3 5 8 13 21 34 55 89 144 233 377 
    


```python
f2(600)
```




    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]



<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
