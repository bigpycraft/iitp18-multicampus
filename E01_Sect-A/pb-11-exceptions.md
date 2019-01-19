
# Industry 4.0 의 중심, BigData

<div align='right'><font size=2 color='gray'>Data Processing Based Python @ <font color='blue'><a href='https://www.facebook.com/jskim.kr'>FB / jskim.kr</a></font>, 김진수</font></div>
<hr>

## <font color='brown'>에러와 예외처리, Errors & Exceptions</font>
>  
- 구문 에러, Syntax Errors
- 예외, Exceptions
- try-except 구문으로 예외상황 제어, Exceptions Handling in Program
- try-except 구문으로 예외상황 제어, Exceptions Handling in Function 
- else와 finally 활용하기
- 사용자 정의 예외, User-defined Exceptions!

### 구문 에러, Syntax Errors


```
# print() 함수의 괄호 누락
print 'I can do coding with python. Wow~~~'
```


      File "<ipython-input-1-c0abefaa7ede>", line 2
        print 'I can do coding with python. Wow~~~'
                                                  ^
    SyntaxError: Missing parentheses in call to 'print'. Did you mean print('I can do coding with python. Wow~~~')?
    



```
# 콜론(:) 누락
if 1>0
    print("1은 0보다 크다.")
```


      File "<ipython-input-2-0c27e6b29d97>", line 2
        if 1>0
              ^
    SyntaxError: invalid syntax
    



```
# 들여쓰기 실수
if 1>0:
    print('1은 0보다 크다.')
  print('당연하쥐!')
```


      File "<tokenize>", line 4
        print('당연하쥐!')
        ^
    IndentationError: unindent does not match any outer indentation level
    


### 예외, Exceptions


```
# 정의하지 않은 변수 stragne 호출
print(strange)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-4-20527d0147e7> in <module>()
          1 # 정의하지 않은 변수 stragne 호출
    ----> 2 print(strange)
    

    NameError: name 'strange' is not defined



```
# 숫자와 문자열의 덧셈, 불가하다.
2 + '2'
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-5-abdd20d17bfa> in <module>()
          1 # 숫자와 문자열의 덧셈, 불가하다.
    ----> 2 2 + '2'
    

    TypeError: unsupported operand type(s) for +: 'int' and 'str'


### try-except 구문으로 예외상황 제어, Exceptions Handling in Program


```
try:
    print('안녕하세요.')
    print(param)
except:
    print('예외가 발생했습니다!')

```

    안녕하세요.
    예외가 발생했습니다!
    


```
try:
    print('안녕하세요.')
    print(param)
except:
    print('예외가 발생했습니다!')
else:
    print('예외가 발생하지 않았습니다.')

```

    안녕하세요.
    예외가 발생했습니다!
    


```
try:
    print('안녕하세요.')
    print(param)
except:
    print('예외가 발생했습니다!')
finally:
    print('무조건 실행하는 코드')

```

    안녕하세요.
    예외가 발생했습니다!
    무조건 실행하는 코드
    


```
try:
    print(param)
except Exception as e:
    print(e)        # name 'param' is not defined 가 출력됨

```

    name 'param' is not defined
    


```
import time
count = 1
try:
    while True:
        print(count)
        count += 1
        time.sleep(0.5)
except KeyboardInterrupt:   # Ctrl-C가 입력되면 발생하는 오류
    print('사용자에 의해 프로그램이 중단되었습니다.')

```

    1
    2
    3
    4
    5
    6
    사용자에 의해 프로그램이 중단되었습니다.
    

### try-except 구문으로 예외상황 제어, Exceptions Handling in Function


```
# 예외상황 테스트를 위한 함수
def exception_test():
    print("[1] Can you add 2 and '2' in python? ")
    print("[2] Try it~! ", 2+'2')     # 예외 발생
    print("[3] It's not possible to add integer and string together. ")
    
exception_test()
```

    [1] Can you add 2 and '2' in python? 
    


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-11-c971d69df651> in <module>()
          5     print("[3] It's not possible to add integer and string together. ")
          6 
    ----> 7 exception_test()
    

    <ipython-input-11-c971d69df651> in exception_test()
          2 def exception_test():
          3     print("[1] Can you add 2 and '2' in python? ")
    ----> 4     print("[2] Try it~! ", 2+'2')     # 예외 발생
          5     print("[3] It's not possible to add integer and string together. ")
          6 
    

    TypeError: unsupported operand type(s) for +: 'int' and 'str'



```
# 예외상황에 대한 처리를 구현한 함수
def exception_test2():
    print("[1] Can you add 2 and '2' in python? ")
    
    try:
        print("[2] Try it~! ", 2+'2')     # TypeError 발생
    except TypeError:
        print("[2] I got TypeError! ")    # 에러 메시지 출력
    
    
    print("[3] It's not possible to add integer and string together. ")
    
exception_test2()
```

    [1] Can you add 2 and '2' in python? 
    [2] I got TypeError! 
    [3] It's not possible to add integer and string together. 
    


```
# 예외상황에 대한 에러메시지를 상세히 나타낸 함수
def exception_test3():
    print("[1] Can you add 2 and '2' in python? ")
    
    try:
        print("[2] Try it~! ", 2+'2')     # TypeError 발생
    except TypeError as err:
        print("[2] TypeError: {}".format(err))    # 에러 메시지 출력
    
    
    print("[3] It's not possible to add integer and string together. ")
    
exception_test3()
```

    [1] Can you add 2 and '2' in python? 
    [2] TypeError: unsupported operand type(s) for +: 'int' and 'str'
    [3] It's not possible to add integer and string together. 
    


```
import traceback 

# 처음에 보았던 트레이스백 메시지와 함께 나타낸 함수
def exception_test4():
    print("[1] Can you add 2 and '2' in python? ")
    
    try:
        print("[2] Try it~! ", 2+'2')     # TypeError 발생
    except TypeError:
        print("[2] I got TypeError! Check below! ")    # 에러 메시지 출력
        traceback.print_exc()                          # 트레이스백 메시지 출력
    
    print("[3] It's not possible to add integer and string together. ")
    
exception_test4()
```

    [1] Can you add 2 and '2' in python? 
    [2] I got TypeError! Check below! 
    [3] It's not possible to add integer and string together. 
    

    Traceback (most recent call last):
      File "<ipython-input-14-c6979eb4973d>", line 8, in exception_test4
        print("[2] Try it~! ", 2+'2')     # TypeError 발생
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    

### else와 finally 활용하기


```
# 예외 처리 방식에서의 else 옵션 구문 활용
def exception_test5(file_path):
    try:
        f = open(file_path, 'r')            # 파일 열기 시도
    except IOError:
        print('cannot open', file_path)     # 에러 메시지 출력
    else:
        print('File has', len(f.readlines()), 'lines')    # 파일 라인 수 출력
        f.close()                           # 파일 닫기
        
# 정상 상황
exception_test5('README.txt')
```

    File has 3 lines
    


```
# 없는 파일을 찾을때
exception_test5('README-XXX.txt')
```

    cannot open README-XXX.txt
    


```
# 예외 처리 방식에서의 finally 옵션 구문 활용
def exception_test6(file_path):
    try:
        f = open(file_path, 'r')            # 파일 열기 시도
    except IOError:
        print('cannot open', file_path)     # 에러 메시지 출력
    else:
        print('File has', len(f.readlines()), 'lines')    # 파일 라인 수 출력
        f.close()                           # 파일 닫기
    finally:
        # 예외 발생 상관 없이 무조건 실행
        print('I just tried to read this file.', file_path)
        
# 정상 상황
exception_test6('README.txt')
```

    File has 3 lines
    I just tried to read this file. README.txt
    


```
# 없는 파일을 찾을때
exception_test6('README-XXX.txt')
```

    cannot open README-XXX.txt
    I just tried to read this file. README-XXX.txt
    

### 사용자 정의 예외, User-defined Exceptions


```
# 예외 클래스 
class TooBigNumError(Exception):
    def __init__(self, val):
        self.val = val
    def __str__(self):
        return 'too big number {}. Use 1~10! '.format(self.val)

```


```
raise TooBigNumError(15)
```


    ---------------------------------------------------------------------------

    TooBigNumError                            Traceback (most recent call last)

    <ipython-input-20-6e086af09243> in <module>()
    ----> 1 raise TooBigNumError(15)
    

    TooBigNumError: too big number 15. Use 1~10! 



```
# 사용자 정의 예외를 위한 테스트 함수
def user_defined_exception_test():
    num = int(input('1부터 10 사이의 점수를 입력하세요! : '))   # 숫자 입력
    if num > 10:
        raise TooBigNumError(num)                              # 에러 발생
    print('숫자 {} 를 입력하셨군요! '.format(num))             # 정상인 경우 출력문
```


```
# 정상 Case 입력
user_defined_exception_test()
```

    1부터 10 사이의 점수를 입력하세요! : 7
    숫자 7 를 입력하셨군요! 
    


```
# 에러 Case 입력
user_defined_exception_test()
```

    1부터 10 사이의 점수를 입력하세요! : 15
    


    ---------------------------------------------------------------------------

    TooBigNumError                            Traceback (most recent call last)

    <ipython-input-23-0749cb398f53> in <module>()
          1 # 에러 Case 입력
    ----> 2 user_defined_exception_test()
    

    <ipython-input-21-3abc451a1afb> in user_defined_exception_test()
          3     num = int(input('1부터 10 사이의 점수를 입력하세요! : '))   # 숫자 입력
          4     if num > 10:
    ----> 5         raise TooBigNumError(num)                              # 에러 발생
          6     print('숫자 {} 를 입력하셨군요! '.format(num))             # 정상인 경우 출력문
    

    TooBigNumError: too big number 15. Use 1~10! 


<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
