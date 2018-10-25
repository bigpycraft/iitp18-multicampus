
# Industry 4.0 의 중심, BigData

<div align='right'><font size=2 color='gray'>Data Processing Based Python @ <font color='blue'><a href='https://www.facebook.com/jskim.kr'>FB / jskim.kr</a></font>, 김진수</font></div>
<hr>

## <font color='brown'>함수, Function</font>
> 
- 함수 정의하기
- 기본 인자 값 활용하기, Default Argument Value
- 여러 개의 인자 값 및 키워드 인자 활용하기, Keyword Argument
- 가변 인자 리스트 활용하기, Arbitrary Argument Lists
- 언패킹 인자 리스트 활용하기, Unpacking Argument Lists
- 변수의 유효 범위, Scope
- 문서화를 위한 문자열 활용하기, Documentation Strings (docstring)

###  Range( ) 함수


```python
# range() 인자값 1개
result1 = list(range(10))

# range() 인자값 2개
result2 = list(range(5, 10))

# range() 인자값 3개
result3 = list(range(1, 10, 2))

print('range(10)     \t= ', result1)
print('range(5,10)   \t= ', result2)
print('range(1,10,2) \t= ', result3)

```

    range(10)     	=  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    range(5,10)   	=  [5, 6, 7, 8, 9]
    range(1,10,2) 	=  [1, 3, 5, 7, 9]
    

### 함수 생성


```python
# 함수 생성1
def add_txt(arg1, arg2):
    print(arg1, arg2)

param1 = '대~한민국~'
param2 = '짝짝~짝~ 짝.짝!!'
add_txt(param1, param2)

```

    대~한민국~ 짝짝~짝~ 짝.짝!!
    


```python
# 함수 생성2
def add_num(num1, num2):
    result = num1 + num2
    return result

param1 = 40
param2 = 50
sum = add_num(param1, param2)
print('%d와 %d의 합은 %d입니다.' % (param1, param2, sum))
```

    40와 50의 합은 90입니다.
    

### 함수 호출


```python
# 함수 호출1,  No Return Function
def sayHello():
    print('Hi, Guys !!')

sayHello()
# print(sayHello())

```

    Hi, Guys !!
    


```python
# 함수 호출2
def exchangeUSDtoKRW(dollar):
    won = dollar * 1065
    return won

usd = 2000
krw = exchangeUSDtoKRW(usd)
print('환전한 금액은 %d 원 입니다.'%(krw))
```

    환전한 금액은 2130000 원 입니다.
    


```python
# Error 발생
krw = exchangeUSDtoKRW()
print('환전한 금액은 %d 원 입니다.'%(krw))
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-6-23fadb77b0d9> in <module>()
          1 # Error 발생
    ----> 2 krw = exchangeUSDtoKRW()
          3 print('환전한 금액은 %d 원 입니다.'%(krw))
    

    TypeError: exchangeUSDtoKRW() missing 1 required positional argument: 'dollar'



```python
# 인세를 계산하는 함수
def calc_royalty(price, sales, per):
    rate = per / 100
    royalty = int(price * sales * rate)
    return royalty

# 사용자가 정보를 입력한다
i = input("책의 정가는？")
price = int(i)

i = input("발행 부수는？")
sales = int(i)

i = input("인세율(퍼센트)은？")
per = float(i)

# 결과 표시
v = calc_royalty(price, sales, per)
print("인세는 ", v, "원입니다.")

```

    책의 정가는？27000
    발행 부수는？1000
    인세율(퍼센트)은？30
    인세는  8100000 원입니다.
    

### Default Argument 


```python
def orderMenu(menu):
    print('손님, %s를 주문하였습니다' % (menu))

orderMenu('카페모카')
# TypeError
# orderMenu()
```

    손님, 카페모카를 주문하였습니다
    


```python
# Default Argument
def orderCoffee(menu='카페라떼'):
    print('손님, %s를 주문하였습니다.' % (menu))

orderCoffee()
```

    손님, 카페라떼를 주문하였습니다.
    

### Keyword Argument


```python
# Keyword Arguments, 키워드 인자 활용하기
def introduceMyCar(brand, seats=4, type='세단'):
    print('나의 차는 {b} {s}인승 {t}이다'.format(
        b = brand,
        s = seats,
        t = type
    ))
    # print('나의 차는', brand, '의', seats, '인승', type, '이다')

# 위치 인자 값 1개
introduceMyCar('아우디')

# 키워드 인자 값 1개
introduceMyCar(brand='렉서스')

# 위치 인자 값 1개, 키워드 인자 값 1개, 혼용으로 사용 가능
introduceMyCar('제규어', seats=2)

# 키워드 인자 값 2개
introduceMyCar(brand='머큐리', type='머슬카')

# 순서 바뀐 키워드 인자 값2개, 순서가 바뀐 경우는 반드시 키워드 인자값 사용
introduceMyCar(type='미니벤', brand='카니발')

# 순서를 지킨 위치 인자 값 3개, 순서가 같다면 모두 위치 인지 값 사용 가능
introduceMyCar('카니발', 9, '미니벤')

# 순서 바뀐 키워드 인자 값3개, 순서가 바뀐 경우는 반드시 키워드 인자값 사용
introduceMyCar('쉐보레', type='SUV ', seats=7)

```

    나의 차는 아우디 4인승 세단이다
    나의 차는 렉서스 4인승 세단이다
    나의 차는 제규어 2인승 세단이다
    나의 차는 머큐리 4인승 머슬카이다
    나의 차는 카니발 4인승 미니벤이다
    나의 차는 카니발 9인승 미니벤이다
    나의 차는 쉐보레 7인승 SUV 이다
    

### Arbitrary Argument 


```python
# Arbitrary Arguments, 가변 인자 리스트 활용
def introduceMyFamily(my_name, *family_names, **family_info):
    print('안녕하세요, 저는 %s 입니다.'%(my_name))
    print('-'*35)
    print('제 가족들의 이름은 아래와 같아요. ')
    
    for name in family_names:
        print('* %s ' % (name), end='\t')
    else:
        print()
    print('-' * 35)
    
    for key in family_info.keys():
        print('- %s : %s ' %(key, family_info[key]))

introduceMyFamily('진수', '희영', '찬영', '준영', '채영',
                  주소='롯데캐슬', 가훈='극기상진', 소망='세계일주')


```

    안녕하세요, 저는 진수 입니다.
    -----------------------------------
    제 가족들의 이름은 아래와 같아요. 
    * 희영 	* 찬영 	* 준영 	* 채영 	
    -----------------------------------
    - 주소 : 롯데캐슬 
    - 가훈 : 극기상진 
    - 소망 : 세계일주 
    

### unpacking


```python
def add(a, b):
    return a + b

data = (10, 20)    # tuple
#print(add(data))
print(add(*data))  # unpacking

```

    30
    


```python
def introduce(name, greeting):
    return "{name}님, {greeting}".format(
        name=name,
        greeting=greeting,
    )

introduce_dict = {
    "name" : "김진수",
    "greeting" : "안녕하세요",
}
print(introduce(**introduce_dict))
```

    김진수님, 안녕하세요
    

### Scope of variable & global variable


```python
# 지역변수와 전역변수
param   = 10
strdata = '전역변수'

def func1():
    strdata = '지역변수'
    print('func1.strdata = %s, id = %d' % (strdata, id(strdata)))

def func2(param):
    param = 20
    print('func2.param = %d, id = %d' % (param, id(param)))

def func3():
    global param
    param = 30
    print('func3.param = %d, id = %d' % (param, id(param)))

```


```python
func1()
print('main1.strdata = %s, id = %d' % (strdata, id(strdata)))
```

    func1.strdata = 지역변수, id = 2842107397704
    main1.strdata = 전역변수, id = 2842107398328
    


```python
func2(param)
print('main2.param = %d, id = %d' % (param, id(param)))
```

    func2.param = 20, id = 1629840128
    main2.param = 10, id = 1629839808
    


```python
func3()
print('main3.param = %d, id = %d' % (param, id(param)))
```

    func3.param = 30, id = 1629840448
    main3.param = 30, id = 1629840448
    

### Documentation Strings (docstring)


```python
# Documentation Strings (docstring)
def my_function():
    """ 아무것도 하지 않지만, 문서만 기술한 함수

    본 함수는 docstring을 설명하기 위한 함수로 아무 행위도 하지 않는다.
    """
    pass

print(my_function.__doc__)
```

     아무것도 하지 않지만, 문서만 기술한 함수
    
        본 함수는 docstring을 설명하기 위한 함수로 아무 행위도 하지 않는다.
        
    


```python
# 문서화를 위한 문자열 활용
def introduce_your_family(name, *family_names, **family_info):
    '''
    가족을 소개하는 함수입니다.
    Args:
        name: 자기이름 입력하기
        *family_names: 가족이름 입력하기
        **family_info: 가족소개하기

    Returns: 없습니다.
    '''
    pass
```

### Turtle Exam


```python
# 아티스트가 된 거북이 (거북이 직접 움직이기)
import turtle as t

def turn_right():
    t.setheading(0)
    t.forward(10)

def turn_up():
    t.setheading(90)
    t.forward(10)

def turn_left():
    t.setheading(180)
    t.forward(10)

def turn_down():
    t.setheading(270)
    t.forward(10)

def blank():
    t.clear()

t.shape("turtle")
t.speed(10)
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up,"Up")
t.onkeypress(turn_left,"Left")
t.onkeypress(turn_down,"Down")
t.onkeypress(blank, "Escape")
t.listen()
t.mainloop()

```


```python
# 마우스클릭으로 이어그리기
import turtle as t

t.speed(1)
t.pensize(5)
t.shape("turtle")

# t.hideturtle()
t.onscreenclick(t.goto)
t.mainloop()

```

<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
