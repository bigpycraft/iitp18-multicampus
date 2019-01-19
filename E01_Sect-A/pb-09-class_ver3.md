
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
    id(var)   	:  1856463357928
    type(var) 	:  <class 'str'>
    
    str       	:  <class 'str'>
    type(str) 	:  <class 'type'>
    id(str)   	:  2003746544
    
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
    

# OOP, 객체지향 프로그래밍
> 객체지향 프로그래밍 5가지 특징
- 캡슐화 : 데이터와 함수 등 객체와 관련된 것을 하나로 묶는 것
- 은닉화 : 클래스 속성값을 바로 접근할 수 없도록 접근을 제한하는 것
- 상속   : 클래스의 기능확장을 위한 방법중 하나, 부모클래스 기능을 자식클랙스가 그대로 가져오는 것
- 다형성 : 상속을 통해 오버로딩, 오버라이딩을 복합적으로 사용함으로써 여러가지를 처리하는 것
- 추상화 : 인터페이스와 구현을 분리

### 이름 장식, Name Mangling


```python
# dir() : 클래스 내부에 들어있는 객체들을 확인하는 명령문
class MyCountry:
    country = 'Korea'

result = dir(MyCountry)
print(result)

num = 0
for internal_element in result:
    num += 1
    print(num, internal_element)
```

    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'country']
    1 __class__
    2 __delattr__
    3 __dict__
    4 __dir__
    5 __doc__
    6 __eq__
    7 __format__
    8 __ge__
    9 __getattribute__
    10 __gt__
    11 __hash__
    12 __init__
    13 __init_subclass__
    14 __le__
    15 __lt__
    16 __module__
    17 __ne__
    18 __new__
    19 __reduce__
    20 __reduce_ex__
    21 __repr__
    22 __setattr__
    23 __sizeof__
    24 __str__
    25 __subclasshook__
    26 __weakref__
    27 country
    


```python
# 이름장식 Name Mangling  : __가 있는 것에 한하여 이름을 변경해 버리는 이름 장식 기법
# 변형된 규칙 : _[클래스명]__[변수명]
class MyCountry:
    __country = 'Korea'

result = dir(MyCountry)
print(result)

# 클래스 내부 변형변수는 정의시 사용했던 변수명으로는 접근이 불가능
# MyCountry.__country

num = 0
for internal_element in result:
    num += 1
    print(num, internal_element)

```

    ['_MyCountry__country', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
    1 _MyCountry__country
    2 __class__
    3 __delattr__
    4 __dict__
    5 __dir__
    6 __doc__
    7 __eq__
    8 __format__
    9 __ge__
    10 __getattribute__
    11 __gt__
    12 __hash__
    13 __init__
    14 __init_subclass__
    15 __le__
    16 __lt__
    17 __module__
    18 __ne__
    19 __new__
    20 __reduce__
    21 __reduce_ex__
    22 __repr__
    23 __setattr__
    24 __sizeof__
    25 __str__
    26 __subclasshook__
    27 __weakref__
    

### 정보은닉 및 캡슐화,  Data Hiding & Encapsulation


```python
# 정보은닉 Data Hiding 혹은 캡슐화 Encapsulation
# 클래스안의 변수를 핸들링(수정/호출)하기 위한 메소드를 선언하여 호출하는 방식
class MyFavorite:
    __hobby = '야구'
    __drink = '맥주'

    def get_hobby(self):
        return self.__hobby

    def get_drink(self):
        return self.__drink

    def set_hobby(self, hobby):
        self.__hobby = hobby

    def set_drink(self, drink):
        self.__drink = drink

myInfo = MyFavorite()
my_hobby = myInfo.get_hobby()
my_drink = myInfo.get_drink()
print('예전엔 %s를 좋아하고, %s를 즐겨마셨어요.'%(my_hobby, my_drink))

# myInfo.__hobby = '골프'
# myInfo.__drink = '소주'
myInfo.set_hobby('골프')
myInfo.set_drink('소주')
my_hobby = myInfo.get_hobby()
my_drink = myInfo.get_drink()
print('지금은 %s를 좋아하고, %s를 즐겨마십니다.'%(my_hobby, my_drink))

```

    예전엔 야구를 좋아하고, 맥주를 즐겨마셨어요.
    지금은 골프를 좋아하고, 소주를 즐겨마십니다.
    

### 상속, Inheritance


```python
# 부모클래스, Animal
class Animal:
    tribe = '동물'
    def __init__(self, name):
        self.name = name

    def getInfo(self):
        print('나는', self.tribe,  self.name, '입니다.')

# Animal의 자식클래스, Carnivore 클래스
class Carnivore(Animal):
    def __init__(self, name):
        self.name = name
        self.tribe = '육식동물'

    def favoriteFood(self):
        print('나는 고기를 좋아합니다.')

# Animal의 자식클래스, Herbivore 클래스
class Herbivore(Animal):
    def __init__(self, name):
        self.name = name
        self.tribe = '초식동물'

    def favoriteFood(self):
        print('나는 풀을 좋아합니다.')

```


```python
print('-' * 50, "\n[Carnivore 객체 생성]")
tiger = Carnivore('호랑이')
tiger.getInfo()
tiger.favoriteFood()

print('-' * 50, "\n[Herbivore 객체 생성]")
rabit = Herbivore('토끼')
rabit.getInfo()
rabit.favoriteFood()

```

    -------------------------------------------------- 
    [Carnivore 객체 생성]
    나는 육식동물 호랑이 입니다.
    나는 고기를 좋아합니다.
    -------------------------------------------------- 
    [Herbivore 객체 생성]
    나는 초식동물 토끼 입니다.
    나는 풀을 좋아합니다.
    

### 다형성, Polymorphism


```python
#  Developer 부모 클래스 선언
class Developer:
    def __init__(self, name):
        self.name = name

    def coding(self):
        print('%s는 코딩을 좋아합니다.' % self.name)
        print(self.name + ' is developer!!')


# PythonDeveloper 자식 클래스 선언
class PythonDeveloper(Developer):
    def coding(self):
        print('%s는 Python 코딩을 좋아합니다.' % self.name)


# JavaDeveloper 자식 클래스 선언
class JavaDeveloper(Developer):
    def coding(self):
        print('%s는 JAVA 코딩을 좋아합니다.' % self.name)


# CPPDeveloper 자식 클래스 선언
class CPPDeveloper(Developer):
    def coding(self):
        print('%s는 C++ 코딩을 좋아합니다.' % self.name)
```


```python
pDeveloper = PythonDeveloper('찬영이')
jDeveloper = JavaDeveloper('준영이')
cDeveloper = CPPDeveloper('채영이')

pDeveloper.coding()
jDeveloper.coding()
cDeveloper.coding()

```

    찬영이는 Python 코딩을 좋아합니다.
    준영이는 JAVA 코딩을 좋아합니다.
    채영이는 C++ 코딩을 좋아합니다.
    

### 게임 유닛 만들기


```python
# Unit 부모클래스 선언
class Unit:
    def __init__(self, name, energy,  is_fly):
        self.name = name
        self.energy = energy
        self.is_fly = is_fly
        self.is_alive = True

    def get_tribe(self):
        print(self.name + ' is a basic tribe !!')

    def get_energy(self):
        if self.energy > 0:
            print(self.name + '의 현재 에너지는 ', self.energy, '입니다!')
        else:
            self.is_alive = False
            print(self.name + ' 유닛은 전사했습니다. ㅠㅠ')
        #return self.energy


# 테란 종족 클래스
class Terran(Unit):
    def get_tribe(self):
        print(self.name + ' is a Terran !!')

    def be_attactted(self):
        self.energy -= 3

# 프로토스 종족 클래스
class Protoss(Unit):
    def get_tribe(self):
        print(self.name + ' is a Protoss !!')

    def be_attactted(self):
        self.energy -= 2

# 저그 종족 클래스
class Zerg(Unit):
    def get_tribe(self):
        print(self.name + ' is a Zerg !!')

    def be_attactted(self):
        self.energy -= 4

```


```python
import time
from tqdm import tqdm_notebook

# 종족별 유닛 생성
marine  = Terran('골리앗', 15, False)
corsair = Protoss('커세어', 20, True)
hydra   = Zerg('히드라', 10, False)

for x in tqdm_notebook(range(5)):
    
    if x == 0:
        print('게임 시작, 유닛의 에너지는 다음과 같습니다!! \n' + '-'*50)
        marine.get_energy()
        corsair.get_energy()
        hydra.get_energy()
        time.sleep(2)
        continue
    
    marine.be_attactted()
    corsair.be_attactted()
    hydra.be_attactted()

    print('\n유닛간에 %d차 공방전이 이루어졌습니다! \n'%(x) + '-'*50)
    time.sleep(1)
    marine.get_energy();    time.sleep(1)
    corsair.get_energy();   time.sleep(1)
    hydra.get_energy();     time.sleep(1)

    if(marine.is_alive & corsair.is_alive & hydra.is_alive):
        time.sleep(1)
    else:
        break

print('='*50, '\nGG, 게임이 종료되었습니다 !!!')

```


    A Jupyter Widget


    게임 시작, 유닛의 에너지는 다음과 같습니다!! 
    --------------------------------------------------
    골리앗의 현재 에너지는  15 입니다!
    커세어의 현재 에너지는  20 입니다!
    히드라의 현재 에너지는  10 입니다!
    
    유닛간에 1차 공방전이 이루어졌습니다! 
    --------------------------------------------------
    골리앗의 현재 에너지는  12 입니다!
    커세어의 현재 에너지는  18 입니다!
    히드라의 현재 에너지는  6 입니다!
    
    유닛간에 2차 공방전이 이루어졌습니다! 
    --------------------------------------------------
    골리앗의 현재 에너지는  9 입니다!
    커세어의 현재 에너지는  16 입니다!
    히드라의 현재 에너지는  2 입니다!
    
    유닛간에 3차 공방전이 이루어졌습니다! 
    --------------------------------------------------
    골리앗의 현재 에너지는  6 입니다!
    커세어의 현재 에너지는  14 입니다!
    히드라 유닛은 전사했습니다. ㅠㅠ
    ================================================== 
    GG, 게임이 종료되었습니다 !!!
    

<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
