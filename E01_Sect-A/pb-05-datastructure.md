
<center>
<b><font size=6>Industry 4.0 의 중심, BigData</font></b>
</center>

<div align='right'><font size=2 color='gray'>Data Processing Based Python @ <font color='blue'><a href='https://www.facebook.com/jskim.kr'>FB / jskim.kr</a></font>, 김진수</font></div>
<hr>

## <font color='brown'>데이터구조, Data Structure</font>
> 
- 리스트형, List Type
- 튜플형, Tuple Type
- 세트형, Set Type
- 사전형, Dictionary Type

### 리스트형, List

#### 리스트형 선언 및 인덱싱


```python
# 리스트형 선언 및 색인
bts_members = ['RM', '슈가', '진', '제이홉', '지민', '뷔', '정국']

# 변수의 타입 확인
print('멤버 :', bts_members)
print('타입 :', type(bts_members))
print('크기 :', len(bts_members))
```

    멤버 : ['RM', '슈가', '진', '제이홉', '지민', '뷔', '정국']
    타입 : <class 'list'>
    크기 : 7
    


```python
print('리스트멤버 호출')
print(bts_members[0])
print(bts_members[1])
print(bts_members[2])
print(bts_members[3])
```

    리스트멤버 호출
    RM
    슈가
    진
    제이홉
    


```python
print('리스트멤버 호출(역순)')
print(bts_members[-1])
print(bts_members[-2])
print(bts_members[-3])
print(bts_members[-4])
```

    리스트멤버 호출(역순)
    정국
    뷔
    지민
    제이홉
    

#### 리스트형 추가/삭제


```python
# 리스트형 추가/삭제
sistar_members = ['효린', '소유']
print('씨스타 \t:', sistar_members)

sistar_members.append('다솜')
print('append \t:', sistar_members)
sistar_members.insert(1, '보라')
print('insert \t:', sistar_members)

sistar_members.remove('소유')
print('remove \t:', sistar_members)

pickup = sistar_members.pop(0)
print('pop   \t:', sistar_members, end=' ---> ')
print(pickup)

```

    씨스타 	: ['효린', '소유']
    append 	: ['효린', '소유', '다솜']
    insert 	: ['효린', '보라', '소유', '다솜']
    remove 	: ['효린', '보라', '다솜']
    pop   	: ['보라', '다솜'] ---> 효린
    

#### 리스트 슬라이싱


```python
# 리스트 슬라이싱
rainbow = ['빨강', '주황', '노랑', '초록', '파랑', '남색', '보라']
print('\n무지개색깔 \t :', rainbow)

result = rainbow[2:5]
print('rainbow[2:5] :', result)

result = rainbow[:3]
print('rainbow[ :3] :', result)

result = rainbow[:]
print('rainbow[ : ] :', result)

result = rainbow[::2]
print('rainbow[::2] :', result)

result = rainbow[-3:]
print('rainbow[-3:] :', result)

result = rainbow[::-1]
print('rainbow[::-1]:', result)

```

    
    무지개색깔 	 : ['빨강', '주황', '노랑', '초록', '파랑', '남색', '보라']
    rainbow[2:5] : ['노랑', '초록', '파랑']
    rainbow[ :3] : ['빨강', '주황', '노랑']
    rainbow[ : ] : ['빨강', '주황', '노랑', '초록', '파랑', '남색', '보라']
    rainbow[::2] : ['빨강', '노랑', '파랑', '보라']
    rainbow[-3:] : ['파랑', '남색', '보라']
    rainbow[::-1]: ['보라', '남색', '파랑', '초록', '노랑', '주황', '빨강']
    

#### 리스트 응용


```python
solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성', '지구']
print('태양계 :', solarsys)

# 리스트에서 특정 요소의 위치 구하기(index)
planet = '지구'
pos = solarsys.index(planet)
print('%s 행성은 태양계에서 %d번째에 위치하고 있습니다.' %(planet, pos))
pos = solarsys.index(planet, 5)
print('%s 행성은 태양계에서 %d번째에 위치하고 있습니다.' %(planet, pos))

# 리스트에서 특정 위치의 요소를 변경하기
solarsys.pop(-1)
print('태양계 :', solarsys)

planet = '화성'
pos = solarsys.index(planet)
solarsys [pos] = 'Mars'
print('태양계 :', solarsys)

# 리스트에서 특정 구간에 있는 요소 추출하기
solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
rock_planets = solarsys[1:5]
gas_planets  = solarsys[5: ]

print('암석형 행성: ', end=''); print(rock_planets);
print('가스형 행성: ', end=''); print(gas_planets);

# 리스트의 특정 위치에 요소 삽입하기(insert)
solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
pos = solarsys.index('목성')
solarsys.insert(pos, '소행성')
print('태양계 :', solarsys)

```

    태양계 : ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성', '지구']
    지구 행성은 태양계에서 3번째에 위치하고 있습니다.
    지구 행성은 태양계에서 9번째에 위치하고 있습니다.
    태양계 : ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
    태양계 : ['태양', '수성', '금성', '지구', 'Mars', '목성', '토성', '천왕성', '해왕성']
    암석형 행성: ['수성', '금성', '지구', '화성']
    가스형 행성: ['목성', '토성', '천왕성', '해왕성']
    태양계 : ['태양', '수성', '금성', '지구', '화성', '소행성', '목성', '토성', '천왕성', '해왕성']
    

#### 중첩리스트


```python
#3x3 2차원 행렬을 중첩리스트로 선언
city = [
    ['서울',  '도쿄',  '베이징'],
    ['런던',  '파리',  '로마'  ],
    ['워싱턴','시카고','잭슨빌']
]

print('city      :', city)
print('city[0]   :', city[0])
print('city[1]   :', city[1])
print('city[-1]  :', city[-1])
print('city[0][0]:', city[0][0])
print('city[0][1]:', city[0][1])
print('city[0][2]:', city[0][2])
print('city[1][1]:', city[1][1])
print('city[2][0]:', city[2][0])
```

    city      : [['서울', '도쿄', '베이징'], ['런던', '파리', '로마'], ['워싱턴', '시카고', '잭슨빌']]
    city[0]   : ['서울', '도쿄', '베이징']
    city[1]   : ['런던', '파리', '로마']
    city[-1]  : ['워싱턴', '시카고', '잭슨빌']
    city[0][0]: 서울
    city[0][1]: 도쿄
    city[0][2]: 베이징
    city[1][1]: 파리
    city[2][0]: 워싱턴
    

### 튜플형, Tuple

#### 튜플형 선언 및 인덱싱


```python
#튜플 생성(튜플형, tuple type)
girl_group = ('트와이스', '레드벨벳', '에이핑크', '걸스데이', '우주소녀')

print('girl_group    \t: ', girl_group)
print('girl_group[:2] \t: ', girl_group[:2])
print('girl_group[-2:] : ', girl_group[-2:])
```

    girl_group    	:  ('트와이스', '레드벨벳', '에이핑크', '걸스데이', '우주소녀')
    girl_group[:2] 	:  ('트와이스', '레드벨벳')
    girl_group[-2:] :  ('걸스데이', '우주소녀')
    

#### 튜플형 변경


```python
# 튜플값 변경 시도, TypeError 발생
girl_group[2] = '블랙핑크'
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-9-e245171553c8> in <module>()
          1 # 튜플값 변경 시도, TypeError 발생
    ----> 2 girl_group[2] = '블랙핑크'
    

    TypeError: 'tuple' object does not support item assignment



```python
girl_group = list(girl_group)
girl_group[2] = '블랙핑크'
girl_group = tuple(girl_group)
print('girl_group   \t: ', girl_group)
```

    girl_group   	:  ('트와이스', '레드벨벳', '블랙핑크', '걸스데이', '우주소녀')
    

#### 튜플형 응용


```python
width  = 20
height = 30
area = width * height

print('너비 :', width);  
print('높이 :', height);
print('넓이 :', area)

```

    너비 : 20
    높이 : 30
    넓이 : 600
    


```python
data   = (15, 50)
width, height = data
area = width * height

print('너비 :', width);  
print('높이 :', height);
print('넓이 :', area)

```

    너비 : 15
    높이 : 50
    넓이 : 750
    

### 세트형, Set

#### 세트형 생성


```python
#세트형 생성
lang = {'Java', 'Java', 'Python', 'C++', 'Python'}
print(lang)
print(type(lang))
print('Python'in lang)
print('Javascript'in lang)

```

    {'Java', 'C++', 'Python'}
    <class 'set'>
    True
    False
    

#### 세트형 집합 연산자


```python
# 세트형 집합 연산자
a = set('abracadabra')
b = set('alacazam')

print('집합 a =', a);  print('집합 b =', b);
print('합집합, a | b =', a | b)
print('교집합, a & b =', a & b)
print('차집합, a - b =', a - b)
print('여집합, a ^ b =', a ^ b)

```

    집합 a = {'a', 'r', 'd', 'c', 'b'}
    집합 b = {'a', 'c', 'l', 'z', 'm'}
    합집합, a | b = {'a', 'r', 'd', 'c', 'b', 'l', 'z', 'm'}
    교집합, a & b = {'a', 'c'}
    차집합, a - b = {'b', 'r', 'd'}
    여집합, a ^ b = {'b', 'r', 'l', 'd', 'z', 'm'}
    

#### 중복 제거 및 정렬


```python
# 중복 제거 및 정렬
beast = ["lion", "tiger", "wolf", "tiger", "lion", "bear", "lion" ]
print('beast =', beast)

unique_beast = list(set(beast))
print('unique_beast =', unique_beast)
sorted_beast = sorted(unique_beast)
print("sorted_beast =", sorted_beast)

```

    beast = ['lion', 'tiger', 'wolf', 'tiger', 'lion', 'bear', 'lion']
    unique_beast = ['lion', 'wolf', 'bear', 'tiger']
    sorted_beast = ['bear', 'lion', 'tiger', 'wolf']
    

### 사전형, Dict

#### 사전형 생성


```python
# 사전형 생성
bans = { '잎새반':'찬영이',
         '열매반':'예영이',
         '햇살반':'준영이',
         '열매반':'채영이', }

print(type(bans))
print('반의수 : ', len(bans))

# 읽기
print('잎새반 : ', bans['잎새반'])
print('열매반 : ', bans['열매반'])
print('bans 읽기 :', bans)

# 추가
bans['꽃잎반'] = '희영이'
print('bans 추가 :', bans)

# 변경
bans['잎새반'] = '서영이'
print('bans 변경 :', bans)

# 삭제
del bans['햇살반']
print('bans 삭제 :', bans)

```

    <class 'dict'>
    반의수 :  3
    잎새반 :  찬영이
    열매반 :  채영이
    bans 읽기 : {'잎새반': '찬영이', '열매반': '채영이', '햇살반': '준영이'}
    bans 추가 : {'잎새반': '찬영이', '열매반': '채영이', '햇살반': '준영이', '꽃잎반': '희영이'}
    bans 변경 : {'잎새반': '서영이', '열매반': '채영이', '햇살반': '준영이', '꽃잎반': '희영이'}
    bans 삭제 : {'잎새반': '서영이', '열매반': '채영이', '꽃잎반': '희영이'}
    

#### 사전형 함수


```python
customer = {
    "name"    : "김진수",
    'gender'  : '남자',
    "email"   : "bigpycraft@gmail.com",
    "company" : "빅파이크래프트",
    "address" : "서울시 중구 청파로"
}

print('customer.keys()   \t= ', customer.keys())
print('customer.values() \t= ', customer.values())
print('customer.items()  \t= ', customer.items())
print('-'*50)

for key, value in customer.items():
    print('%s\t : %s' %(key, value))

```

    customer.keys()   	=  dict_keys(['name', 'gender', 'email', 'company', 'address'])
    customer.values() 	=  dict_values(['김진수', '남자', 'bigpycraft@gmail.com', '빅파이크래프트', '서울시 중구 청파로'])
    customer.items()  	=  dict_items([('name', '김진수'), ('gender', '남자'), ('email', 'bigpycraft@gmail.com'), ('company', '빅파이크래프트'), ('address', '서울시 중구 청파로')])
    --------------------------------------------------
    name	 : 김진수
    gender	 : 남자
    email	 : bigpycraft@gmail.com
    company	 : 빅파이크래프트
    address	 : 서울시 중구 청파로
    

<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
