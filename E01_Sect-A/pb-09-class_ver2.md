
# Industry 4.0 의 중심, BigData

<div align='right'><font size=2 color='gray'>Data Processing Based Python @ <font color='blue'><a href='https://www.facebook.com/jskim.kr'>FB / jskim.kr</a></font>, 김진수</font></div>
<hr>

## <font color='brown'>클래스, Class</font>
> 
- 클래스 이해하기
- 클래스 정의 및 불러오기
- 클래스 초기화 함수 __init__( ) 재정의
- 클래스 변수와 인스턴스 변수
- 데이터 은닉과 이름 장식, Data Hiding & Name Mangling
- 객체 지향의 꽃 상속, Inheritance
- 다형성, Polymorphism

### 클래스 이해, 모든것은 객체다!


```python
# 문자열형 변수 var 생성
var = '파이썬, 클래스와 객체'
print('var       \t: ', var)
print('id(var)   \t: ', id(var))
print('type(var) \t: ', type(var))

# str, str의 타입, str의 식별자 확인
print('\nstr       \t: ', str)
print('type(str) \t: ', type(str))
print('id(str)   \t: ', id(str))

# var 지역변수 __class__ 값 확인
print('\nvar.__class__ : ', var.__class__)

var2 = var.replace('파이썬', 'Python')
print('\nvar2    \t: ', var2)

```

    var       	:  파이썬, 클래스와 객체
    id(var)   	:  2223872141184
    type(var) 	:  <class 'str'>
    
    str       	:  <class 'str'>
    type(str) 	:  <class 'type'>
    id(str)   	:  1979170544
    
    var.__class__ :  <class 'str'>
    
    var2    	:  Python, 클래스와 객체
    

### 클래스 정의 


```python
# 클래스 정의 : X
class MyClass:
    name = '희영'

    def sayHello():
        hello = "Hello, " + name + "\t It's Good day !"
        return hello


myClass = MyClass()
obj_name = myClass.name
obj_method = myClass.sayHello()

print('Object name   :', obj_name)
print('Object method :', obj_method)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-2-e2e529182c75> in <module>()
         10 myClass = MyClass()
         11 obj_name = myClass.name
    ---> 12 obj_method = myClass.sayHello()
         13 
         14 print('Object name   :', obj_name)
    

    TypeError: sayHello() takes 0 positional arguments but 1 was given



```python
# 클래스 정의 : OK
class MyClass:
    name = '찬영'

    def sayHello(self):
        hello = "Hello, " + self.name + "\t It's Good day !"
        return hello


myClass = MyClass()
obj_name = myClass.name
obj_method = myClass.sayHello()

print('Object name   :', obj_name)
print('Object method :', obj_method)
```

    Object name   : 찬영
    Object method : Hello, 찬영	 It's Good day !
    

### 객체 생성, 인스턴스화


```python
# 클래스 정의
class MyClass:
    name = str()

    def sayHello(self):
        hello = "Hello, " + self.name + "\t It's Good day !"
        print(hello)

# 객체 생성, 인스턴스화
myClass = MyClass()
myClass.name = '준영'
myClass.sayHello()

```

    Hello, 준영	 It's Good day !
    

### 클래스 초기화 함수


```python
# 클래스 초기화 함수, __init__() 재정의
class MyClass:
    def __init__(self, name):     # 초기화 함수 재정의
        self.name = name

    def sayHello(self):
        hello = "Hello, " + self.name + "\t It's Good day !"
        print(hello)

# 객체 생성, 인스턴스화
# myClass = MyClass()
myClass = MyClass('채영')
myClass.sayHello()

```

    Hello, 채영	 It's Good day !
    

### 클래스 변수와 인스턴스 변수


```python
# 클래스 변수와 인스턴스 변수
# 변수의 선언위체 따라 달라지는 유효범위
class MyChildren:
    school = '대학교'       # 클래스변수 country 선언

    def __init__(self, name):     # 초기화 함수 재정의
        self.name   = name        # 인스턴스 변수 name 선언

    def go_to_school(self):
        print(self.name + '이는 ' + self.school + '에 다닙니다.')

# 객체 인스턴스화
myChild  = MyChildren('희영')
myChild1 = MyChildren('찬영')
myChild2 = MyChildren('준영')
myChild3 = MyChildren('채영')

myChild1.school = '고등학교'
myChild2.school = '중학교'
myChild3.school = '초등학교'

# 클래스함수 호출 (인스턴스 변수 name 출력)
myChild.go_to_school()
myChild1.go_to_school()
myChild2.go_to_school()
myChild3.go_to_school()

```

    희영이는 대학교에 다닙니다.
    찬영이는 고등학교에 다닙니다.
    준영이는 중학교에 다닙니다.
    채영이는 초등학교에 다닙니다.
    

#### 클래스 변수 : 인스턴스간 공유 됨


```python
# 클래스 변수
class Dog:
    tricks = []  # 클래스 변수 선언

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)  # 클래스 변수에 값 추가


dog1 = Dog('마음이')
dog2 = Dog('진돌이')

dog1.add_trick('구르기')
dog2.add_trick('두발로 서기')
dog2.add_trick('죽은척 하기')

print(dog1.name, ':', dog1.tricks)
print(dog2.name, ':', dog2.tricks)

```

    마음이 : ['구르기', '두발로 서기', '죽은척 하기']
    진돌이 : ['구르기', '두발로 서기', '죽은척 하기']
    

#### 인스턴스 변수 : 인스턴스간 공유 안됨


```python
# 인스턴스 변수 
class Cat:
    def __init__(self, name):
        self.name = name
        self.tricks = []  # 인스턴스 변수 선언

    def add_trick(self, trick):
        self.tricks.append(trick)  # 인스턴스 변수에 값 추가


cat1 = Cat('하늘이')
cat2 = Cat('야옹이')

cat1.add_trick('구르기')
cat2.add_trick('두발로 서기')
cat2.add_trick('죽은척 하기')

print(cat1.name, ':', cat1.tricks)
print(cat2.name, ':', cat2.tricks)

```

    하늘이 : ['구르기']
    야옹이 : ['두발로 서기', '죽은척 하기']
    

<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
