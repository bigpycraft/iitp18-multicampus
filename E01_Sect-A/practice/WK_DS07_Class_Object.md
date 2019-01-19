
# Industry 4.0 의 중심, BigData

<div align='right'><font size=2 color='gray'>Data Processing Based Python @ <font color='blue'><a href='https://www.facebook.com/jskim.kr'>FB / jskim.kr</a></font>, [김진수](bigpycraft@gmail.com)</font></div>
<hr>

# <font color='brown'>객체와 클래스</font> 
>  
- 클래스 선언과 객체 생성
- 클래스를 구성하는 변수와 함수
- 객체와 클래스를 사용하는 이유
- 클래스 상속


## <font color='blue'>클래스 선언과 객체 생성 </font>

### 객체란?
>  
- 객체는 속성(상태, 특징)과 행위(행동, 동작, 기능)로 구성된 대상을 의미한다.
- 프로그래밍 언어에서 객체를 만들 때는 주로 현실 세계를 반영해서 만든다.
- 객체의 특징인 속성은 변수로, 객체가 할 수 있는 일인 행동은 함수로 구현한다.
- 객체는 변수와 함수의 묶음이다.

cf. 객체를 만들고 이용할 수 있는 기능을 제공하는 프로그래밍 언어를 객체지향언어(Object Oriented Programming, OOP)라고 한다.

### 클래스 선언

### 객체 생성 및 활용


```python
class Bicycle(): # 클래스 선언
    pass
```


```python
my_bicycle = Bicycle()
```


```python
my_bicycle
```


```python
my_bicycle.wheel_size = 26
my_bicycle.color = 'black'
```


```python
print("바퀴 크기:", my_bicycle.wheel_size)  # 객체의 속성 출력
print("색상:", my_bicycle.color)   
```


```python
class Bicycle():
    
    def move(self, speed):
        print("자전거: 시속 {0}킬로미터로 전진".format(speed))
        
    def turn(self, direction):
        print("자전거: {0}회전".format(direction))
        
    def stop(self):
        print("자전거({0}, {1}): 정지 ".format(self.wheel_size, self.color))
```


```python
my_bicycle = Bicycle() # Bicycle 클래스의 인스턴스인 my_bicycle 객체 생성

my_bicycle.wheel_size = 26 # 객체의 속성 설정
my_bicycle.color = 'black' 

my_bicycle.move(30)  # 객체의 메서드 호출
my_bicycle.turn('좌')
my_bicycle.stop()
```


```python
bicycle1 = Bicycle() # Bicycle 클래스의 인스턴스인 bicycle1 객체 생성

bicycle1.wheel_size = 27 # 객체의 속성 설정
bicycle1.color = 'red' 

bicycle1.move(20)
bicycle1.turn('좌')
bicycle1.stop()
```


```python
bicycle2 = Bicycle() # Bicycle 클래스의 인스턴스인 bicycle2 객체 생성

bicycle2.wheel_size = 24 # 객체의 속성 설정
bicycle2.color = 'blue' 

bicycle2.move(15)
bicycle2.turn('우')
bicycle2.stop()
```

### 객체 초기화


```python
class Bicycle():    
    
    def __init__(self, wheel_size, color):
        self.wheel_size = wheel_size
        self.color = color
        
    def move(self, speed):
        print("자전거: 시속 {0}킬로미터로 전진".format(speed))
        
    def turn(self, direction):
        print("자전거: {0}회전".format(direction))
        
    def stop(self):
        print("자전거({0}, {1}): 정지 ".format(self.wheel_size, self.color))
```


```python
my_bicycle = Bicycle(26, 'black') # 객체 생성과 동시에 속성값을 지정.

my_bicycle.move(30)  # 객체 메서드 호출
my_bicycle.turn('좌')
my_bicycle.stop()
```

## <font color='blue'>클래스를 구성하는 변수와 함수 </font>

### 클래스에서 사용하는 변수


```python
class Car():
    instance_count = 0 # 클래스 변수 생성 및 초기화

    def __init__(self, size, color):
        self.size = size    # 인스턴스 변수 생성 및 초기화
        self.color = color  # 인스턴스 변수 생성 및 초기화
        Car.instance_count = Car.instance_count + 1 # 클래스 변수 이용
        print("자동차 객체의 수: {0}".format(Car.instance_count))
        
    def move(self):
        print("자동차({0} & {1})가 움직입니다.".format(self.size, self.color))
```


```python
car1 = Car('small', 'white')
car2 = Car('big', 'black')
```


```python
print("Car 클래스의 총 인스턴스 개수:{}".format(Car.instance_count)) 
```


```python
print("Car 클래스의 총 인스턴스 개수:{}".format(car1.instance_count))
print("Car 클래스의 총 인스턴스 개수:{}".format(car2.instance_count))
```


```python
car1.move()
car2.move()
```


```python
class Car2():
    count = 0; # 클래스 변수 생성 및 초기화

    def __init__(self, size, num):
        self.size = size    # 인스턴스 변수 생성 및 초기화
        self.count = num  # 인스턴스 변수 생성 및 초기화
        Car2.count = Car2.count + 1 # 클래스 변수 이용
        print("자동차 객체의 수: Car2.count = {0}".format(Car2.count))
        print("인스턴스 변수 초기화: self.count = {0}".format(self.count))
        
    def move(self):
        print("자동차({0} & {1})가 움직입니다.".format(self.size, self.count))
```


```python
car1 = Car2("big", 20)
car1 = Car2("small", 30)
```

### 클래스에서 사용하는 함수

#### 인스턴스 메서드


```python
# Car 클래스 선언
class Car():
    instance_count = 0 # 클래스 변수 생성 및 초기화
    
    # 초기화 함수(인스턴스 메서드)
    def __init__(self, size, color):
        self.size = size    # 인스턴스 변수 생성 및 초기화
        self.color = color  # 인스턴스 변수 생성 및 초기화
        Car.instance_count = Car.instance_count + 1 # 클래스 변수 이용
        print("자동차 객체의 수: {0}".format(Car.instance_count))  
       
    # 인스턴스 메서드
    def move(self, speed):
        self.speed = speed  # 인스턴스 변수 생성    
        print("자동차({0} & {1})가 ".format(self.size, self.color), end='')
        print("시속 {0}킬로미터로 전진".format(self.speed))
        
    # 인스턴스 메서드
    def auto_cruise(self):
        print("자율 주행 모드")
        self.move(self.speed) # move() 함수의 인자로 인스턴스 변수를 입력
```


```python
car1 = Car("small", "red") # 객체 생성 (car1)
car2 = Car("big", "green") # 객체 생성 (car2)

car1.move(80) #객체(car1)의 move() 메서드 호출
car2.move(100) #객체(car2)의 move() 메서드 호출

car1.auto_cruise() #객체(car1)의 auto_cruise() 메서드 호출
car2.auto_cruise() #객체(car2)의 auto_cruise() 메서드 호출
```

#### 정적 메서드


```python
# Car 클래스 선언
class Car():
        
    # def __init__(self, size, color): => 앞의 코드 활용
    # def move(self, speed): => 앞의 코드 활용
    # def auto_cruise(self): => 앞의 코드 활용
    
    # 정적 메서드
    @staticmethod
    def check_type(model_code):
        if(model_code >= 20):
            print("이 자동차는 전기차입니다.")
        elif(10 <= model_code < 20):
            print("이 자동차는 가솔린차입니다.")
        else:
            print("이 자동차는 디젤차입니다.")
```


```python
Car.check_type(25)
Car.check_type(2)
```

#### 클래스 메서드


```python
# Car 클래스 선언
class Car():
    instance_count = 0 # 클래스 변수    
  
    # 초기화 함수(인스턴스 메서드)
    def __init__(self, size, color):
        self.size = size    # 인스턴스 변수
        self.color = color  # 인스턴스 변수
        Car.instance_count = Car.instance_count + 1
       
    # def move(self, speed): => 앞의 코드 활용
    # def auto_cruise(self): => 앞의 코드 활용
    # @staticmethod
    # def check_type(model_code): => 앞의 코드 활용
    
    # 클래스 메서드
    @classmethod
    def count_instance(cls):
        print("자동차 객체의 개수: {0}".format(cls.instance_count))
```


```python
Car.count_instance() # 객체 생성 전에 클래스 메서드 호출

car1 = Car("small", "red") # 첫 번째 객체 생성
Car.count_instance() # 클래스 메서드 호출

car2 = Car("big", "green") # 두 번째 객체 생성
Car.count_instance() # 클래스 메서드 호출
```

## <font color='blue'>객체와 클래스를 사용하는 이유 </font>


```python
robot_name = 'R1'    # 로봇 이름
robot_pos = 0        # 로봇의 초기 위치

def robot_move():
    global robot_pos
    robot_pos = robot_pos + 1
    print("{0} position: {1}".format(robot_name, robot_pos))
```


```python
robot_move()
```


```python
robot1_name = 'R1'   # 로봇 이름
robot1_pos = 0       # 로봇의 초기 위치

def robot1_move():
    global robot1_pos
    robot1_pos = robot1_pos + 1
    print("{0} position: {1}".format(robot1_name, robot1_pos))

robot2_name = 'R2'   # 로봇 이름
robot2_pos = 10      # 로봇의 초기 위치

def robot2_move():
    global robot2_pos
    robot2_pos = robot2_pos + 1
    print("{0} position: {1}".format(robot2_name, robot2_pos))
```


```python
robot1_move()
robot2_move()
```


```python
class Robot():
    def __init__(self, name, pos): 
        self.name = name     # 로봇 객체의 이름
        self.pos  = pos      # 로봇 객체의 위치
       
    def move(self):
        self.pos = self.pos + 1
        print("{0} position: {1}".format(self.name, self.pos))
```


```python
robot1 = Robot('R1', 0)
robot2 = Robot('R2', 10)
```


```python
robot1.move()
robot2.move()
```


```python
myRobot3 = Robot('R3', 30)
myRobot4 = Robot('R4', 40)

myRobot3.move()
myRobot4.move()
```

## <font color='blue'>클래스 상속 </font>


```python
class Bicycle():
    
    def __init__(self, wheel_size, color):
        self.wheel_size = wheel_size
        self.color = color
        
    def move(self, speed):
        print("자전거: 시속 {0}킬로미터로 전진".format(speed))
        
    def turn(self, direction):
        print("자전거: {0}회전".format(direction))
        
    def stop(self):
        print("자전거({0}, {1}): 정지 ".format(self.wheel_size, self.color))
```


```python
class FoldingBicycle(Bicycle):
        
    def __init__(self, wheel_size, color, state): # FoldingBicycle 초기화
        Bicycle.__init__(self, wheel_size, color) # Bicycle의 초기화 재사용
        #super().__init__(wheel_size, color) # super()도 사용 가능
        self.state = state  # 자식 클래스에서 새로 추가한 변수 
        
    def fold(self):
        self.state = 'folding'
        print("자전거: 접기, state = {0}".format(self.state))

    def unfold(self):
        self.state = 'unfolding'
        print("자전거: 펴기, state = {0}".format(self.state))
```


```python
folding_bicycle = FoldingBicycle(27, 'white', 'unfolding')     # 객체 생성

folding_bicycle.move(20)    # 부모 클래스의 함수(메서드) 호출
folding_bicycle.fold()      # 자식 클래스에서 정의한 함수 호출
folding_bicycle.unfold()
```

<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
