
# Industry 4.0 의 중심, BigData

<div align='right'><font size=2 color='gray'>Data Processing Based Python @ <font color='blue'><a href='https://www.facebook.com/jskim.kr'>FB / jskim.kr</a></font>, [김진수](bigpycraft@gmail.com)</font></div>
<hr>

## <font color='brown'>데이터형, Data Type</font>
> 
- 숫자형, Numeric Type
- 논리형, Boolean Type
- 문자열형, String Type
- 데이터형 에러, Data Type Error
- 데이터형 변환, Data Type Converting
- 변할 수 없는(Immutable) vs. 변할 수 있는(Mutable)

### 숫자형


```python
# 기본연산
x = 50
y = 4.

print("x = ", x)
print("y = ", y)
print("x + y = " , x+y)
print("x - y = " , x-y)
print("x * y = " , x*y)
print("x / y = " , x/y)
```

    x =  50
    y =  4.0
    x + y =  54.0
    x - y =  46.0
    x * y =  200.0
    x / y =  12.5
    


```python
print("x //y = " , x//y)
print("x % y = " , x%y)
print("-x = "    , -x)
print("+x = "    , +x)
print("x ** y = ", x**y)
print("pow(x,y) = ", pow(x,y))
```

    x //y =  12.0
    x % y =  2.0
    -x =  -50
    +x =  50
    x ** y =  6250000.0
    pow(x,y) =  6250000.0
    

### 논리형


```python
# 비교연산자와 논리연산자
x = 4
y = 9

print("x == y = ", x==y)
print("x != y = ", x!=y)

print("x < y  = ", x<y)
print("x > y  = ", x>y)

print("int(True)  = ", int(True))
print("int(False) = ", int(False))
```

    x == y =  False
    x != y =  True
    x < y  =  True
    x > y  =  False
    int(True)  =  1
    int(False) =  0
    

### 문자형


```python
# 이스케이프 문자 
text1 = "안녕하세요!\n하나금융\t임직원여러분 !"

text2 = '''
빅데이터를 위한 파이썬과정에서
만나뵙게되어 반갑습니다.
끝까지 '화이팅' 하세요!!!
'''
print(text1)
print(text2)
```

    안녕하세요!
    하나금융	임직원여러분 !
    
    빅데이터를 위한 파이썬과정에서
    만나뵙게되어 반갑습니다.
    끝까지 '화이팅' 하세요!!!
    
    


```python
# 문자형함수1
test = '파이썬 프로그래밍 재미있다!'    # 문자열을 변수에 저장

result = test.startswith('파이썬')        # 문자열이 '파이썬으로 시작하는지 확인
print(result)
result = test.endswith('!')               # 문자열이 '!'로 끝나는지 확인
print(result)
result = test.endswith('어려워요!')       # 문자열이 '어려워요!'로 끝나는지 확인
print(result)
result = test.replace('파이썬', 'Python')   # 문자열중 '파이썬'을 'Python'으로 변경
print(result)
```

    True
    True
    False
    Python 프로그래밍 재미있다!
    


```python
# 문자형함수2
test = 'Python Programming is Interesting!'

result = test.upper()      # 문자열을 모두 대문자로 변경
print(result)
result = test.lower()      # 문자열을 모두 소문자로 변경
print(result)
result = '/'.join(test)      # 문자열의 각 문자 사이에 '/'문자 집어 넣기
print(result)
```

    PYTHON PROGRAMMING IS INTERESTING!
    python programming is interesting!
    P/y/t/h/o/n/ /P/r/o/g/r/a/m/m/i/n/g/ /i/s/ /I/n/t/e/r/e/s/t/i/n/g/!
    

### 데이터형 변환


```python
# 데이터형 확인
num_data = 350
str_data = '350'

print(type(num_data))
print(type(str_data))
```

    <class 'int'>
    <class 'str'>
    


```python
# 에러발생
sum = num_data + str_data
sum
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-8-3fe5cbb0bcd1> in <module>()
          1 # 에러발생
    ----> 2 sum = num_data + str_data
          3 sum
    

    TypeError: unsupported operand type(s) for +: 'int' and 'str'



```python
# 데이터형 변환
sum = int(str_data) + num_data
print('합계는? ', str(sum))
```

    합계는?  700
    

### Immutable vs. Mutable


```python
# Immutable 예제
hello = '안녕하세요!'    # hello 문자열형 변수 선언

print(hello)             # hello 값 확인
print(id(hello))         # hello 객체 식별자 확인

hello = '반값습니다!'    # hello 값 변경

print(hello)             # hello 값 확인
print(id(hello))         # hello 객체 식별자 확인
```

    안녕하세요!
    1640034586672
    반값습니다!
    1640034588576
    


```python
# Mutable 예제
hello_list = ['안녕하세요!']    # 리스트형 선언

print(hello_list)               # 리스트 값 확인
print(id(hello_list))           # 리스트 객체 식별자 확인

hello_list[0] = '반갑습니다!'   # 리스트 첫번째 항목 값 변경하기

print(hello_list)               # 리스트 값 확인
print(id(hello_list))           # 리스트 객체 식별자 확인
```

    ['안녕하세요!']
    1640034008456
    ['반갑습니다!']
    1640034008456
    

<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
