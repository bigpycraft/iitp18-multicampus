
# Industry 4.0 의 중심, BigData

<div align='right'><font size=2 color='gray'>Data Processing Based Python @ <font color='blue'><a href='https://www.facebook.com/jskim.kr'>FB / jskim.kr</a></font>, [김진수](bigpycraft@gmail.com)</font></div>
<hr>

# <font color='brown'>변수와 자료형</font> 
>  
- 변수
- 문자열
- 리스트
- 튜플
- 세트
- 딕셔너리

## <font color='blue'>변수 </font>


```python
12340 * 1/2
```


```python
12340 * 1/4
```


```python
12340 * 1/5
```


```python
abc = 12340
print(abc)
```


```python
abc
```


```python
print(abc * 1/2)
print(abc * 1/4)
print(abc * 1/5)
```


```python

```

## <font color='blue'>문자열 </font>

### 문자열 만들기


```python
print("String Test")
```


```python
print('String Test')
```


```python
string1 = "String Test 1"
string2 = 'String Test 2'
print(string1)
print(string2)
```


```python
type(string1)
```


```python
type(string2)
```


```python
string3 = 'This is a "double" quotation test'
string4 = "This is a 'single' quotation test"
print(string3)
print(string4)
```


```python
long_string1 = '''[삼중 작은따옴표를 사용한 예]
파이썬에는 삼중 따옴표로 여러 행의 문자열을 입력할 수 있습니다.
큰따옴표(")와 작은따옴표(')도 입력할 수 있습니다.''' 

long_string2 = """[삼중 큰따옴표를 사용한 예]
파이썬에는 삼중 따옴표로 여러 행의 문자열을 입력할 수 있습니다.
큰따옴표(")와 작은따옴표(')도 입력할 수 있습니다.""" 

print(long_string1)
print(long_string2)
```

### 문자열 다루기


```python
a = 'Enjoy '
b = 'python!'
c = a + b
print(c)
```


```python
print(a * 3)
```


```python

```

## <font color='blue'>리스트 </font>

### 리스트 만들기


```python
# 1번 학생의 국어, 영어, 수학, 과학 점수가 각각 90,95,85,80
student1 = [90,95,85,80] 
student1
```


```python
type(student1)
```


```python
student1[0]
```


```python
student1[1]
```


```python
student1[-1]
```


```python
student1[1] = 100 # 두 번째 항목에 새로운 데이터 할당
student1
```


```python
myFriends = ['James', 'Robert', 'Lisa', 'Mary']
myFriends
```


```python
myFriends[2]
```


```python
myFriends[3]
```


```python
myFriends[-1]
```


```python
mixedList = [0, 2, 3.14, 'python', 'program', True, myFriends]
mixedList
```

### 리스트 다루기

#### 리스트 더하기와 곱하기


```python
list_con1= [1,2,3,4]
list_con2 = [5,6,7,8]
list_con = list_con1 + list_con2 # 리스트 연결

print(list_con)
```


```python
list_con1= [1,2,3,4]
list_con = list_con1 * 3 # 리스트 반복

print(list_con)
```

#### 리스트 중 일부 항목 가져오기


```python
list_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list_data)
print(list_data[0:3])
print(list_data[4:8])
print(list_data[:3])
print(list_data[7:])
print(list_data[::2])
```

####  리스트에서 항목 삭제하기


```python
## <font color='blue'>변수 </font>print(list_data)
del list_data[6]
print(list_data)
```

#### 리스트에서 항목의 존재 여부 확인하기


```python
list_data1 = [1, 2, 3, 4, 5]
print(5 in list_data1)
print(6 in list_data1)
```

#### 리스트 메서드 활용하기


```python
myFriends = ['James', 'Robert', 'Lisa', 'Mary']
print(myFriends)
myFriends.append('Thomas')
print(myFriends)
```


```python
myFriends = ['James', 'Robert', 'Lisa', 'Mary']
print(myFriends)
myFriends.insert(1,'Paul')
print(myFriends)
```


```python
myFriends = ['James', 'Robert', 'Lisa', 'Mary']
print(myFriends)
myFriends.extend(['Laura', 'Betty'])
print(myFriends)
```


```python

```

## <font color='blue'>튜플 </font>

### 튜플 만들기


```python
tuple1 = (1,2,3,4)
tuple1
```


```python
type(tuple1)
```


```python
tuple1[1]
```


```python
tuple2 = 5,6,7,8
print(tuple2)
```


```python
type(tuple2)
```


```python
tuple3 = (9,) # 반드시 쉼표(',') 필요
tuple4 = 10,  # 반드시 쉼표(',') 필요
print(tuple3)
print(tuple4)
```

### 튜플 다루기


```python
tuple5 = (1,2,3,4)
tuple5[1] = 5 # 한번 생성된 튜플의 요소는 변경되지 않음
```


```python
del tuple5[1] # 한번 생성된 튜플 요소는 삭제되지 않음
```


```python
tuple6 = ('a', 'b', 'c', 'd', 'e', 'f')
tuple6.index('c')
```


```python
tuple7 = ('a', 'a', 'a', 'b', 'b', 'c', 'd')
tuple7.count('a')
```


```python

```

## <font color='blue'>세트 </font>

### 세트 만들기


```python
set1 = {1, 2, 3}
set1a = {1, 2, 3, 3}
print(set1)
print(set1a)
```


```python
type(set1)
```

### 세트의 교집합, 합집합, 차집합 구하기


```python
A = {1, 2, 3, 4, 5}         # Set A
B = {4, 5, 6, 7, 8, 9, 10}  # Set B
A.intersection(B)  # 집합 A에 대한 집합 B의 교집합(A∩B)
```


```python
A.union(B) # 집합 A에 대한 집합 B의 합집합(A∪B)
```


```python
A.difference(B) # 집합 A에 대한 집합 B의 차집합(A-B)
```


```python
A = {1, 2, 3, 4, 5}         # Set A
B = {4, 5, 6, 7, 8, 9, 10}  # Set B
A & B  # 집합 A에 대한 집합 B의 교집합(A∩B)
```


```python
A | B  # 집합 A에 대한 집합 B의 합집합(A∪B)
```


```python
A - B  # 집합 A에 대한 집합 B의 차집합(A-B)
```

### 리스트, 튜플, 세트 간 타입 변환


```python
a = [1,2,3,4,5]
```


```python
type(a)
```


```python
b = tuple(a)
b
```


```python
type(b)
```


```python
c = set(a)
c
```


```python
type(c)
```


```python
list(b)
```


```python
list(c)
```


```python

```

## <font color='blue'>딕셔너리 </font>

### 딕셔너리 만들기


```python
country_capital = {"영국":"런던", "프랑스":"파리", "스위스": "베른", "호주":"멜버른", "덴마크": "코펜하겐"}
country_capital
```


```python
type(country_capital)
```


```python
country_capital["영국"]
```


```python
dict_data1 = {1:"버스", 3: "비행기", 4:"택시", 5: "자전거"}
dict_data1
```


```python
dict_data1[3]
```


```python
dict_data2 = {1:10, 2: 20, 3:30, 4: 40, 5:50}
print(dict_data2)
print(dict_data2[4])
```


```python
dict_data3 = {"list_data1":[11,12,13], "list_data2": [21,22,23]}
print(dict_data3)
print(dict_data3["list_data2"])
```


```python
mixed_dict = {1:10, 'dict_num': {1:10, 2:20}, "dict_list_tuple": {"A":[11,12,13], "B":(21,22,23)}, "dict_string": "이것은 책입니다."}
mixed_dict
```

### 딕셔너리 다루기

#### 딕셔너리에 데이터 추가하고 변경하기


```python
country_capital["독일"]= "베를린"
country_capital
```


```python
country_capital["호주"]= "캔버라"
country_capital
```

#### 딕셔너리에서 데이터 삭제하기


```python
del country_capital["덴마크"]
country_capital
```

#### 딕셔너리 메서드 활용하기


```python
fruit_code = {"사과":101, "배":102, "딸기":103, "포도":104, "바나나":105}
```


```python
print(fruit_code.keys())
```


```python
print(fruit_code.values())
```


```python
print(fruit_code.items())
```


```python
list(fruit_code.keys())
```


```python
list(fruit_code.values())
```


```python
list(fruit_code.items())
```


```python
fruit_code2 = {"오렌지":106, "수박":107}
```


```python
fruit_code.update(fruit_code2)
fruit_code
```


```python
fruit_code2.clear()
print(fruit_code2)
type(fruit_code2)
```

<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
