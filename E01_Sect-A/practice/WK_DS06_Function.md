
# Industry 4.0 의 중심, BigData

<div align='right'><font size=2 color='gray'>Data Processing Based Python @ <font color='blue'><a href='https://www.facebook.com/jskim.kr'>FB / jskim.kr</a></font>, [김진수](bigpycraft@gmail.com)</font></div>
<hr>

# <font color='brown'>함수</font> 
>  
- 함수 정의와 호출
- 변수의 유효 범위
- 람다(lambda) 함수
- 유용한 내장 함수

## <font color='blue'>함수 정의와 호출 </font>

### 함수의 기본 구조


### 인자도 반환 값도 없는 함수


```python
def my_func():
    print("My first function!")
    print("This is a function.")
```


```python
my_func()
```

### 인자는 있으나 반환 값이 없는 함수


```python
def my_friend(friendName):
    print("{}는(은) 나의 친구입니다.".format(friendName))
```


```python
my_friend("진수")
my_friend("희영")
```


```python
def my_student_info(name, school_ID, phoneNumber):
    print("------------------------")
    print("- 학생이름:", name)
    print("- 학급번호:", school_ID)
    print("- 전화번호:", phoneNumber)
```


```python
my_student_info("진수", "01", "010-5670-3847")
my_student_info("희영", "02", "010-1234-5678")
```


```python
def my_student_info(name, school_ID,  phoneNumber):
    print("****************************")
    print("* 학생이름:", name)
    print("* 학급번호:", school_ID)
    print("* 전화번호:", phoneNumber)
```


```python
my_student_info("진수", "01", "010-5670-3847")
my_student_info("희영", "02", "010-1234-5678")
```

### 인자도 있고 반환 값도 있는 함수


```python
def my_calc(x,y):
    z = x*y
    return z
```


```python
my_calc(3,4)
```


```python
def my_student_info_list(student_info):
    print("****************************")
    print("* 학생이름:", student_info[0])
    print("* 학급번호:", student_info[1])
    print("* 전화번호:", student_info[2])
    print("****************************")
```


```python
student1_info = ["찬영", "01", "010-2345-6789"]
my_student_info_list(student1_info)
```


```python
my_student_info_list(["준영", "02", "010-2345-9876"])
```

## <font color='blue'>변수의 유효 범위 </font>


```python
a = 5 # 전역 변수

def func1():
    a = 1 # 지역 변수. func1()에서만 사용
    print("[func1] 지역 변수 a =", a)

def func2():
    a = 2 # 지역 변수. func2()에서만 사용
    print("[func2] 지역 변수 a =", a)  
    
def func3():
    print("[func3] 전역 변수 a =", a)   
    
def func4():
    global a  # 함수 내에서 전역 변수 변경 위해 선언
    a = 4      # 전역 변수의 값 변경
    print("[func4] 전역 변수 a =",a)
```


```python
func1() #함수 func1() 호출
func2() #함수 func2() 호출
print("전역 변수 a =", a) # 전역 변수 출력 
```


```python
func3() #함수 func3() 호출
func4() #함수 func4() 호출
func3() #함수 func3() 호출
```

## <font color='blue'>람다(lambda) 함수 </font>


```python
(lambda x : x**2) (3)
```


```python
mySquare = lambda x : x**2
mySquare(2)
```


```python
mySquare(5)
```


```python
mySimpleFunc = lambda x,y,z : 2*x + 3*y + z
mySimpleFunc(1,2,3)
```

## <font color='blue'>유용한 내장 함수 </font>

### 형 변환 함수

#### 정수형으로 변환


```python
[int(0.123), int(3.5123456), int(-1.312367)]
```


```python
[int('1234'), int('5678'), int('-9012')]
```

#### 실수형으로 변환


```python
[float(0), float(123), float(-567)]
```


```python
[float('10'), float('0.123'), float('-567.89')]
```

#### 문자형으로 변환


```python
[str(123), str(459678), str(-987)]
```


```python
[str(0.123), str(345.678), str(-5.987)]
```

#### 리스트, 튜플, 세트형으로 변환


```python
list_data  = ['abc', 1, 2, 'def']
tuple_data = ('abc', 1, 2, 'def')
set_data   = {'abc', 1, 2, 'def'}
```


```python
[type(list_data), type(tuple_data), type(set_data)]
```


```python
print("리스트로 변환: ", list(tuple_data), list(set_data))
```


```python
print("튜플로 변환:", tuple(list_data), tuple(set_data))
```


```python
print("세트로 변환:", set(list_data), set(tuple_data))
```

### bool 함수

#### 숫자를 인자로 bool 함수 호출


```python
bool(0) # 인자: 숫자 0
```


```python
bool(1) # 인자: 양의 정수
```


```python
bool(-10) # 인자: 음의 정수
```


```python
bool(5.12) # 인자: 양의 실수
```


```python
bool(-3.26) # 인자: 음의 실수
```

#### 문자열을 인자로 bool 함수 호출


```python
bool('a') # 인자: 문자열 'a'
```


```python
bool(' ') # 인자: 빈 문자열(공백)
```


```python
bool('') # 인자: 문자열 없음
```


```python
bool(None) #인자: None
```

#### 리스트, 튜플, 세트를 인자로 bool 함수 호출


```python
myFriends = []
bool(myFriends) # 인자: 항목이 없는 빈 리스트 
```


```python
myFriends = ['James', 'Robert', 'Lisa', 'Mary']
bool(myFriends) # 인자: 항목이 있는 리스트 
```


```python
myNum = ()
bool(myNum) # 인자: 항목이 없는 빈 튜플 
```


```python
myNum = (1,2,3)
bool(myNum) # 인자: 항목이 있는 튜플 
```


```python
mySetA = {}
bool(mySetA) # 인자: 항목이 없는 빈 세트 
```


```python
mySetA = {10,20,30}
bool(mySetA) # 인자: 항목이 있는 세트 
```

#### bool 함수의 활용


```python
def print_name(name):
    if bool(name):
        print("입력된 이름:", name)
    else:
        print("입력된 이름이 없습니다.")    
```


```python
print_name("진수")
```


```python
print_name("")
```

### 최솟값과 최댓값을 구하는 함수


```python
myNum = [10, 5, 12, 0, 3.5, 99.5, 42]
[min(myNum), max(myNum)]
```


```python
myStr = 'zxyabc'
[min(myStr), max(myStr)]
```


```python
myNum = (10, 5, 12, 0, 3.5, 99.5, 42)
[min(myNum), max(myNum)]
```


```python
myNum = {"Abc", "abc", "bcd", "efg"}
[min(myNum), max(myNum)]
```

### 절댓값과 전체 합을 구하는 함수


```python
[abs(10), abs(-10)]
```


```python
[abs(2.45), abs(-2.45)]
```


```python
sumList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum(sumList)
```

### 항목의 개수를 구하는 함수


```python
len("ab cd") # 문자열
```


```python
len([1, 2, 3, 4, 5, 6, 7, 8]) # 리스트
```


```python
len((1, 2, 3, 4, 5)) # 튜플
```


```python
len({'a', 'b', 'c', 'd'}) # 세트
```


```python
len({1:"Thomas", 2:"Edward", 3:"Henry"}) # 딕셔너리
```

### 내장 함수의 활용


```python
scores = [90, 80, 95, 85] # 과목별 시험 점수

score_sum = 0                     # 총점 계산을 위한 초깃값 설정
subject_num = 0                   # 과목수 계산을 위한 초깃값 설정
for score in scores:
    score_sum = score_sum + score # 과목별 점수 모두 더하기
    subject_num = subject_num + 1 # 과목수 계산
    
average = score_sum / subject_num # 평균(총점 / 과목수) 구하기

print("총점:{0}, 평균:{1}".format(score_sum,average))
```


```python
scores = [90, 80, 95, 85] # 과목별 시험 점수

print("총점:{0}, 평균:{1}".format(sum(scores), sum(scores)/len(scores)))
```


```python
print("최하 점수:{0}, 최고 점수:{1}".format(min(scores), max(scores)))
```

<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
