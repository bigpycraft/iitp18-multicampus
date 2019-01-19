
# Industry 4.0 의 중심, BigData

<div align='right'><font size=2 color='gray'>Data Processing Based Python @ <font color='blue'><a href='https://www.facebook.com/jskim.kr'>FB / jskim.kr</a></font>, [김진수](bigpycraft@gmail.com)</font></div>
<hr>

# <font color='brown'>파이썬을 계산기처럼 이용</font> 
>  
- 간단한 사칙연산
- 거듭제곱과 나머지
- 과학적 표기법
- 진수 표현과 변환
- 논리 연산 및 비교 연산


## <font color='blue'>간단한 사칙 연산 </font>


```python
1 + 1
```


```python
5 -2
```


```python
15 * 2
```


```python
10 / 2
```


```python
1.2 + 5.3
```


```python
3.5 - 5.0
```


```python
1.4 * 2
```


```python
5 / 2
```


```python
2 + 3 * 4
```


```python
3 / 2 * 4 - 5 / 2
```


```python
10 / 5 + (5 - 2) * 2
```


```python
(5 * 4 - 15) + ((5 - 2) * (9-7))
```


```python
type(3)
```


```python
type(1.2)
```

## <font color='blue'>거듭 제곱과 나머지 </font>


```python
2 * 2 * 2 * 2 * 2
```


```python
2 ** 5
```


```python
1.5 ** 2 
```


```python
2 ** (1/2)
```


```python
13 % 5
```


```python
13 // 5
```

## <font color='blue'>과학적 표기법 </font>


```python
3 * 10 ** 8
```


```python
3e8
```


```python
1e15
```


```python
1e16
```


```python
1e-4
```


```python
1e-5
```

## <font color='blue'>진수 표현과 변환 </font>


```python
17
```


```python
0b10001
```


```python
0o21
```


```python
0x11
```


```python
bin(17)
```


```python
oct(17)
```


```python
hex(17)
```


```python
0b10 * 0o10 + 0x10 - 10
```


```python
bin(0b10 * 0o10 + 0x10 - 10)
```


```python
oct(0b10 * 0o10 + 0x10 - 10)
```


```python
hex(0b10 * 0o10 + 0x10 -10)
```

## <font color='blue'>논리 연산 및 비교 연산 </font>


```python
print(True)
```


```python
print(False)
```


```python
type(True)
```


```python
print(True and False)
print(True or False)
print(not True)
```


```python
print(5 == 3)
print(5 != 3)
print(5 < 3)
print(5 > 3)
print(5 <= 3)
print(5 >= 3)
```


```python
print( 1 > 0 and -2 < 0)
```


```python
print((3 < 0) and ((-5 > 0) and (1 > 5)))
print((3 > 0) or ((-5 > 0) and (1 > 5)))
print(((3 > 0) or (-5 > 0)) and ((4 > 8) or ( 3 < 0)))
```

<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
