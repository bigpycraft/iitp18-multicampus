
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

    색을 영문으로 나타내어 보세요.yellow
    잘못된 색입니다
    

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
    

<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
