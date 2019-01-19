
# Industry 4.0 의 중심, BigData

<div align='right'><font size=2 color='gray'>Data Processing Based Python @ <font color='blue'><a href='https://www.facebook.com/jskim.kr'>FB / jskim.kr</a></font>, 김진수</font></div>
<hr>

## <font color='brown'>제어문</font>
> 
- if문
- while문
- for문
- Break문, continue문, pass문
- 제어문과 자료구조의 조합

### IF 문

#### 조건값 : 비교연산자


```python
# condition = True
condition = False

if condition:
    print("조건을 충족함, condition met")

if not condition:
    print("조건 충족 못함, condition not met")
```

    조건 충족 못함, condition not met
    


```python
# if - else
num_a = 100
num_b = 200

if num_a > num_b:
    print('숫자A가 숫자B보다 더 큰수입니다.')
else:
    print('숫자A는 숫자B와 같거나 더 작은수입니다.')

```

    숫자A는 숫자B와 같거나 더 작은수입니다.
    


```python
# if - elif -else
num_a = 100
num_b = 200

if num_a > num_b:
    print('숫자A가 더 큰수입니다.')
    max = num_a
elif num_a < num_b:
    print('숫자B가 더큰수입니다.')
    max = num_b
else:
    print('숫자A와 숫자B는 같습니다.')

print('숫자A와 숫자B중 최대값은', max, '입니다.')

```

    숫자B가 더큰수입니다.
    숫자A와 숫자B중 최대값은 200 입니다.
    

#### 조건값 : 논리연산자


```python
# if - else 문 예시
signal_color = input('색을 영문으로 나타내어 보세요.')

if signal_color == 'blue':
    print('신호등은 파란색 입니다. 건너가 주세요.')
else:
    print('신호등은 빨간색 입니다. 기다려 주세요.')
```

    색을 영문으로 나타내어 보세요.blue
    신호등은 파란색 입니다. 건너가 주세요.
    


```python
# if - elif  -else 문 예시
signal_color = input('색을 영문으로 나타내어 보세요. (blue/red) ')

if signal_color == 'blue':
    print('신호등은 파란색 입니다. 건너가 주세요.')
elif signal_color == 'red':
    print('신호등은 빨간색 입니다, 기다려 주세요.')
else:
    print('잘못된 색입니다')
```

    색을 영문으로 나타내어 보세요. (blue/red) red
    신호등은 빨간색 입니다, 기다려 주세요.
    


```python
# nested if 문 예시
signal_color = input('색을 영문으로 나타내어 보세요.')

if signal_color == 'blue':
    print('신호등은 파란색 입니다. 건너가 주세요.')
    is_pass = input('건널 준비가 되셨나요? (yes/no) ')
    
    if is_pass == 'yes':
        print('네, 건너겠습니다.')
    else:
        print('다음 번에 건너겠습니다.')
elif signal_color == 'red':
    print('신호등은 빨간색 입니다, 기다려 주세요.')
else:
    print('잘못된 색입니다')
```

    색을 영문으로 나타내어 보세요.blue
    신호등은 파란색 입니다. 건너가 주세요.
    건널 준비가 되셨나요? (yes/no) yes
    네, 건너겠습니다.
    

#### 응용 : BMI 판정 프로그램


```python
weight = float(input("체중(kg)은 ? "))
height = float(input("키(cm)는 ? "))

# BMI 계산
height = height / 100  # m 으로 고친다
bmi = weight / (height * height)

# BMI 값에 따라 결과로 분기 --- (*1)
result = ""
if bmi < 18.5:
    result = "마름"
if (18.5 <= bmi) and (bmi < 25):
    result = "보통"
if (25 <= bmi) and (bmi < 30):
    result = "가벼운 비만"
if bmi >= 30:
    result = "심한 비만"

# 결과 표시
print('-'*50)
print("BMI :", bmi)
print("판정:", result)

```

    체중(kg)은 ? 68
    키(cm)는 ? 172
    --------------------------------------------------
    BMI : 22.985397512168742
    판정: 보통
    

#### 응용 : 입장료 계산 정프로그램


```python
# 고객 수 입력
children = int(input("어린이 요금(13세 미만)은 몇 명? "))
normal = int(input("보통 요금(13세~64세)은 몇 명? "))
elder = int(input("경로우대요금(65세 이상)은 몇 명? "))

# 집계
total_num = children + normal + elder
children_price = children * 500
normal_price = normal * 1000
elder_price = elder * 700
total_price = children_price + normal_price + elder_price

# 할인 대상인지 확인 ----------- (*1)
if total_num >= 10:
    print("단체 할인됩니다.")
    total_price = total_price * 0.8
else:
    print("단체 할인되지 않습니다.")

# 결과 표시
print('-'*50)
print("어린이 요금 \t: {0}명x 500 = {1}원".format(children, children_price))
print("보통 요금   \t: {0}명x1000 = {1}원".format(normal, normal_price))
print("경로우대요금\t: {0}명x 700 = {1}원".format(elder, elder_price))
print('-'*50)
print("합계: {0}人 {1}원".format(total_num, total_price))
```

    어린이 요금(13세 미만)은 몇 명? 3
    보통 요금(13세~64세)은 몇 명? 5
    경로우대요금(65세 이상)은 몇 명? 2
    단체 할인됩니다.
    --------------------------------------------------
    어린이 요금 	: 3명x 500 = 1500원
    보통 요금   	: 5명x1000 = 5000원
    경로우대요금	: 2명x 700 = 1400원
    --------------------------------------------------
    합계: 10人 6320.0원
    

#### 응용 : 윤년 판정 프로그램

- Case 1


```python
year = int(input("서기 몇 년? "))

# 윤년 판정
is_leap = False
# (1) 4로 나누어 떨어지면 윤년 -- (*1)
if year % 4 == 0:
    # (2) 100으로 나누어 떨어지면 윤년이 아님 --- (*2)
    if year % 100 == 0:
        # (3) 400으로 나누어 떨어지면 윤년 -------------- (*3)
        if year % 400 == 0:
            is_leap = True
        else: # ---------------------------------- (*3)에 대응됨
            is_leap = False
    else: # ------------------------------- (*2)에 대응됨
        is_leap = True
else: # -------------------- (*1)에 대응됨
    is_leap = False

# 결과 표시
if is_leap: # ---- (*4)
    print("윤년입니다.")
else:
    print("윤년이 아닙니다.")

```

    서기 몇 년? 2000
    윤년입니다.
    

- Case 2


```python
year = int(input("서기 몇 년 ? "))

# 윤년 판정 --- (*1)
is_leap = False
if year % 400 == 0:
    is_leap = True
elif year % 100 == 0:
    is_leap = False
elif year % 4 == 0:
    is_leap = True
else:
    is_leap = False

# 결과 표시
if is_leap:
    print("윤년입니다.")
else:
    print("윤년이 아닙니다.")

```

    서기 몇 년 ? 2010
    윤년이 아닙니다.
    

- Case 3


```python
year = int(input("서기 몇 년 ? "))

# 윤년 판정
is_leap = (year % 400 == 0)or((year % 100 != 0)and(year % 4 == 0))

# 결과 표시
if is_leap:
    print("윤년입니다.")
else:
    print("윤년이 아닙니다.")

```

    서기 몇 년 ? 2020
    윤년입니다.
    

### While 문


```python
# while Ex01
idx = 0

while idx < 5:
    print(idx)
    idx += 1

print('프로그램 종료!')
```

    0
    1
    2
    3
    4
    프로그램 종료!
    


```python
# while Ex02. 루프탈출
num, sum = 1, 0

while True:
    sum += num
    if sum > 100:
        break
    else:
        num += 1

print('num 값이 %d 일때 while문 탈출 !!' % num)
```

    num 값이 14 일때 while문 탈출 !!
    


```python
# while Ex03
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
idx, sum = 0, 0

while idx < len(numbers):
    num = numbers[idx]
    sum += idx
    idx += 1

print('numbers의 합계는', sum, '입니다.')

```

    numbers의 합계는 45 입니다.
    


```python
# while Ex04
sigmal_color = ''

while sigmal_color != 'blue' and sigmal_color != 'red':
    sigmal_color = input('색을 영문으로 입력하세요 (blue/red) : ')

    if sigmal_color == 'blue':
        print('신호등은 파란색 입니다. 길을 건너세요!!')
    elif sigmal_color == 'red':
        print('신호등은 빨간색 입니다. 기다리세요.')
    else:
        print('잘못된 색입니다. 다시 입력해 주세요!!')

print('프로그램을 종료합니다.')

```

    색을 영문으로 입력하세요 (blue/red) : yellow
    잘못된 색입니다. 다시 입력해 주세요!!
    색을 영문으로 입력하세요 (blue/red) : blue
    신호등은 파란색 입니다. 길을 건너세요!!
    프로그램을 종료합니다.
    

### For 문

#### range() 함수


```python
result = list(range(10))
print('range(10)     :', result)

result = list(range(5,10))
print('range(5,10)   :', result)

result = list(range(1,10,2))
print('range(1,10,2) :', result)

```

    range(10)     : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    range(5,10)   : [5, 6, 7, 8, 9]
    range(1,10,2) : [1, 3, 5, 7, 9]
    


```python
scope = [1, 2, 3, 4, 5]

for x in scope:
    print(x)
```

    1
    2
    3
    4
    5
    


```python
scope = list('abcde')

for x in scope:
    print(x)
```

    a
    b
    c
    d
    e
    

#### break vs. continue vs. pass


```python
# break vs. continue vs. pass
scope = list(range(1, 100))

for num in scope:
    
    if num <= 10:
        if num%2 == 0:
            pass
            print(num, 'is even number.')
        else:
            continue
            print(num, 'is odd number.')
    else:
        print(num, 'is bigger than ten')
        break
        print('after break')

print('프로그램을 종료합니다.')
```

    2 is even number.
    4 is even number.
    6 is even number.
    8 is even number.
    10 is even number.
    11 is bigger than ten
    프로그램을 종료합니다.
    


```python
# for Ex1
bts_members = ['RM', '슈가', '진', '제이홉', '지민', '뷔', '정국']
num = 0

for member in bts_members:
    num += 1
    print('멤버%d ====> %s  \t(이름길이:%d)' % (num, member, len(member)))

```

    멤버1 ====> RM  	(이름길이:2)
    멤버2 ====> 슈가  	(이름길이:2)
    멤버3 ====> 진  	(이름길이:1)
    멤버4 ====> 제이홉  	(이름길이:3)
    멤버5 ====> 지민  	(이름길이:2)
    멤버6 ====> 뷔  	(이름길이:1)
    멤버7 ====> 정국  	(이름길이:2)
    


```python
# for Ex2
size = len(bts_members)

for idx in range(size):
    print('멤버%d ====> %s  \t(이름길이:%d)' % (idx+1, bts_members[idx], len(bts_members[idx])))
```

    멤버1 ====> RM  	(이름길이:2)
    멤버2 ====> 슈가  	(이름길이:2)
    멤버3 ====> 진  	(이름길이:1)
    멤버4 ====> 제이홉  	(이름길이:3)
    멤버5 ====> 지민  	(이름길이:2)
    멤버6 ====> 뷔  	(이름길이:1)
    멤버7 ====> 정국  	(이름길이:2)
    

#### draw triangle with for


```python
# 삼각형1
for i in range(1, 10, 2):
    mark = "*" * i
    print(mark)

```

    *
    ***
    *****
    *******
    *********
    


```python
# 삼각형2
for i in range(1, 10, 2):
    mark = " " * int((10-i)/2) + "*" * i
    print(mark)
    
```

        *
       ***
      *****
     *******
    *********
    

#### nested for


```python
# 중첩 for문
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for x in range(3):
    for y in range(3):
        # print('matrix[', x, '][', y, ']:', matrix[x][y], end=', \t')
        print('matrix[%d][%d]:'%(x, y), matrix[x][y], end=' \t')
    else:
        print('')

```

    matrix[0][0]: 1 	matrix[0][1]: 2 	matrix[0][2]: 3 	
    matrix[1][0]: 4 	matrix[1][1]: 5 	matrix[1][2]: 6 	
    matrix[2][0]: 7 	matrix[2][1]: 8 	matrix[2][2]: 9 	
    


```python
reset
```

    Once deleted, variables cannot be recovered. Proceed (y/[n])? y
    

### Turtle Exam


```python
# if 문
import turtle

in_color = input('원의 색깔을 입력하세요. (R/G/B/etc)  ')
is_filled = input('원의 색깔로 채우겠습니까? (Yes/No)  ')

if in_color == 'R' or in_color == 'r':
    color = 'red'
elif in_color == 'G' or in_color == 'g':
    color = 'green'
elif in_color == 'B' or in_color == 'b':
    color = 'blue'
else:
    color = 'black'

turtle.begin_fill()

turtle.color(color)
turtle.pensize(10)
turtle.circle(100)

if is_filled == 'Y' or is_filled == 'y':
    turtle.end_fill()
else:
    pass

turtle.done()

```


```python
# for 문
import turtle as t

num_circle = 30
radius = 180

t.bgcolor("blue")
t.color("yellow")
t.speed(0)

for _ in range(num_circle):
    t.circle(radius)
    t.left(360/num_circle)

t.done()

```


```python
# for : dot-line
import turtle as t

t.pensize(3)
t.color('red')

for i in range(10):
    t.forward(15)
    t.penup()
    t.forward(15)
    t.pendown()

t.done()

```


```python
# for : draw polygon
import turtle as t

print('다각형을 그리는 예제입니다.')
var1 = input('변의 수를 입력해주세요? [3-8] ')
var2 = input('한변의 길이를 입력해주세요? [100-200] ')
# var2 = str(150)

num_of_side = int(var1)
len_of_side = int(var2)

angle = 360.0 / num_of_side
c_mod = num_of_side % 3
color = 'red' if c_mod==0 else 'green' if c_mod==1 else 'blue'

t.begin_fill()
t.color(color)
t.pensize(5)

for i in range(num_of_side):
    t.forward(len_of_side)
    t.left(angle)

t.end_fill()

t.done()

```


```python
# nested for : draw dot points
import turtle

t = turtle.Turtle()
t.shape('turtle')

dot_distance = 50
width  = 5
height = 4

t.penup()
for y in range(height):
    for i in range(width):
        t.dot()
        t.forward(dot_distance)

    t.backward(dot_distance * width)
    t.right(90)
    t.forward(dot_distance)
    t.left(90)

turtle.done()

```


```python
# whilte : move with keyboard
import turtle as t

# 좌,우,상,하 = A,D,W,S
print('거북이를 키보드로 움직여 보아요')
print('\tA : 왼쪽으로 이동')
print('\tD : 오른쪽으로 이동')
print('\tW : 위쪽으로 이동')
print('\tS : 아래쪽으로 이동')
print('\tX : 프로그램 종료')

input('엔터키를 누르면 시작합니다!')
t.shape("turtle")
t.pensize(5)
t.color('green')
t.speed(1500)

while True:
    direction = input('[A,S,D,F] :')
    if 'X' == direction.upper():
        break
    elif 'D' == direction.upper():
        t.setheading(0)
    elif 'W' == direction.upper():
        t.setheading(90)
    elif 'A' == direction.upper():
        t.setheading(180)
    elif 'S' == direction.upper():
        t.setheading(270)
    else:
        continue

    t.forward(50)

print('\n프로그램을 종료하였습니다!')
t.done()

```

<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
