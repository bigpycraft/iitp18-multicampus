
# Industry 4.0 의 중심, BigData

<div align='right'><font size=2 color='gray'>Data Processing Based Python @ <font color='blue'><a href='https://www.facebook.com/jskim.kr'>FB / jskim.kr</a></font>, [김진수](bigpycraft@gmail.com)</font></div>
<hr>

# <font color='brown'>제어문</font> 
>  
- 조건에 따라 분기하는 if문
- 지정된 범위만큼 반복하는 for문
- 조건에 따라 반복하는 while문
- 반복문을 제어하는 break 와 continue
- 간단하게 반복하는 한 줄 for문


## <font color='blue'>조건에 따라 분기하는 if 문 </font>

### 단일 조건에 따른 분기(if)


```python
x = 95
if x >= 90:
    print("Pass")
```

### 단일 조건 및 그 외 조건에 따른 분기(if ~ else)


```python
x = 75
if x >= 90:
    print("Pass")
else:
    print("Fail")
```

### 여러 조건에 따른 분기(if ~ elif ~ else)


```python
x = 85
if x >= 90:
    print("Very good")
elif  (x >= 80) and (x < 90):
    print("Good")
else:
    print("Bad")
```


```python
x = 85
if x >= 90:
    print("Very Good")
elif  80 <= x < 90:
    print("Good")
else:
    print("Bad")
```

### 중첩 조건에 따른 분기


```python
x = 100
if x >= 90:
    if x==100 :
        print("Perfect")
    else:
        print("Very Good")
elif (x >= 80) and (x < 90):
    print("Good")
else:
    print("Bad")
```

## <font color='blue'>지정된 범위만큼 반복하는 for 문 </font>

### 반복문의 필요성


```python
a = 0 # 변수 a를 0으로 초기화
print(a) # 변수 a 출력

a = a + 1 # 변수 a에 1을 더한 후, 다시 a에 대입
print(a)  # 변수 a 출력

a = a + 1 # 같은 코드 반복
print(a)

a = a + 1 # 같은 코드 반복
print(a)

a = a + 1 # 같은 코드 반복
print(a)

a = a + 1 # 같은 코드 반복
print(a)
```

### for 문의 구조



#### 리스트 이용


```python
for a in [0, 1, 2, 3, 4, 5]:
    print(a)
```


```python
myFriends = ['James', 'Robert', 'Lisa', 'Mary']  # 리스트를 변수에 할당
for myFriend in myFriends:
    print(myFriend)
```

#### range() 함수 이용


```python
print(range(0, 10, 1))
```


```python
print(list(range(0, 10, 1)))
```


```python
for a in range(0, 6, 1):
    print(a)
```


```python
for a in range(0, 6, 2):
    print(a)
```


```python
print(list(range(0, 10, 1)))
print(list(range(0, 10)))
print(list(range(10)))
```


```python
print(list(range(0, 20, 5)))    # Line 1
print(list(range(-10, 0, 2)))   # Line 2
print(list(range(3, -10, -3)))  # Line 3
print(list(range(0, -5, 1)))    # Line 4
```

### 중첩 for 문


```python
x_list = ['x1', 'x2']
y_list = ['y1', 'y2']

print("x y")
for x in x_list:
    for y in y_list:
        print(x,y)
```

### 여러 개의 리스트 다루기


```python
names = ['James', 'Robert', 'Lisa', 'Mary'] 
scores = [95, 96, 97, 94]
```


```python
for k in range(len(names)):
    print(names[k], scores[k])
```


```python
for name, score in zip(names, scores):
    print(name, score)
```

## <font color='blue'>조건에 따라 반복하는 while 문 </font>

### while 문의 구조


```python
i = 0     # 초기화
sum = 0   # 초기화

print("i sum")
while (sum < 20):  # 조건 검사
    i = i + 1      # i를 1씩 증가
    sum = sum + i  # 이전의 sum과 현재 i를 더해서 sum을 갱신
    print(i, sum)  # i와 sum을 출력
```

## <font color='blue'>반복문을 제어하는 break와 continue </font>

### 반복문을 빠져나오는 break


```python
k=0
while True: 
    k = k + 1  # k는 1씩 증가
    
    if(k > 3): # k가 3보다 크면 
        break  # break로 while 문을 빠져나옴
        
    print(k)   # k 출력
```


```python
for k in range(10):  
    if(k > 2):   # k 가 2보다 크면 
        break    # break로 for 문을 빠져나옴 
        
    print(k)     # k 출력        
```

### 다음 반복을 실행하는 continue


```python
for k in range(5):
    if(k == 2):
        continue
        
    print(k)
```


```python
k = 0
while True:
    k = k + 1
    
    if(k == 2):
        print("continue next")
        continue
    if(k > 4):
        break
        
    print(k)
```

## <font color='blue'>간단하게 반복하는 한 줄 for 문 </font>

### 리스트 컴프리헨션의 기본 구조


```python
numbers = [1,2,3,4,5]
square = []

for i in numbers:
    square.append(i**2)
    
print(square)
```


```python
numbers = [1,2,3,4,5]
square = [i**2 for i in numbers]
print(square)
```

### 조건문을 포함한 리스트 컴프리헨션


```python
numbers = [1,2,3,4,5]
square = []

for i in numbers:
    if i >= 3:
        square.append(i**2)
    
print(square)
```


```python
numbers = [1,2,3,4,5]
square  = [i**2 for i in numbers if i>=3]

print(square)
```

<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
