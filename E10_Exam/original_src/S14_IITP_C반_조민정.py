
# coding: utf-8

# ## 실습 1. 2^1000의 각 자리수의 합 구하기

# In[2]:


data1 = 2**1000

def sum(data1):
    result = 0
    for i in str(data1):
        result +=int(i)
    return result

print("2의 1000제곱 모든 자리수의 합은", sum(data1))


# ## 실습 2. 로또번호를 주문하는 클래스(Class Lotto) 생성

# In[27]:


import random

class Lotto:
    
    def __init__(self):
        self.num_buy = 0
        self.num_list = []
    
    def checking(self):
        while True:
            num_buy2=input("로또 게임 수를 적어주세요")
            is_number = True
            check_num = list('0123456789')

            for char in list(num_buy2):
                is_number = is_number * int(char in check_num)
                if is_number:
                    if int(num_buy2)>=1 and int(num_buy2)<=10:
                        self.num_buy = int(num_buy2)
                        return self.num_buy
                        break
                    else:
                        continue
                else:
                    continue
                
        
    
    def rangenum(self):
        while True:
            number_range = True
            check_range = list('0123456789')

    def lonum(self):
        for x in range(self.num_buy):
            LottoNum = random.sample(range(1, 46), 6)
            LottoNum.sort()
            self.num_list.append(LottoNum)
    
    def answer(self):
        print("%d개의 로또번호" %self.num_buy)
        for i in range(len(self.num_list)):
            print("{buy_amount}:{num_list}".format(
                self.num_buy,
                buy_amount = (i+1),
                num_list = self.num_list[i]))


# In[28]:


result = Lotto()
result.checking()
result.lonum()
result.answer()


# ## 실습 3. 특정기념일로부터 얼마나 경과되었는지 알려주는 함수 생성

# In[24]:


from datetime import datetime

def getMemorialDay(year, month, day, memory='기념일', is_msg=True):
    m_day = datetime(year,month,day)
    today = datetime.now()
    day1 = today - m_day
    days = abs(day1.days)
    days2 = format(days, ",")
    months = days//30
    years = days//365
    
    memory=str(memory)
    days=int(days)
    months=int(months)
    years=int(years)
    
   
    if day1.days>0:
        print("오늘은 {memory}으로부터 {remain_day}일 경과되었고, 달수로는 {remain_month}개월 째, 연수로는 {remain_year}년 경과되었습니다!".format(
            memory       = memory, 
            remain_day    = days, 
            remain_month = months, 
            remain_year  = years
        ))
        # print("오늘은 {0}으로부터 {1}일 경과되었고, 달수로는 {2}개월 째, 연수로는 {3}년 경과되었습니다!".format(memory, days, months, years))
        # print("오늘은 %s으로부터 %d일 경과되었고, 달수로는 %d개월 째, 연수로는 %d년 경과되었습니다!" % (memory, days, months, years))
    else:
        print(" {memory}까지는 {future_day}일 남았습니다!".format(
            memory = memory,
            future_day = days))


# In[25]:


getMemorialDay(2014,4,16,"세월호침몰사고일")


# In[26]:


getMemorialDay(2018,12,25,"크리스마스")


# ## 실습 4. reduce를 사용하여 히스토그램(histogram) 함수 작성

# In[8]:


data = ["cat", "cat", "cat", "sheep", "sheep", "duck", "duck", "duck", "duck" ]


# In[9]:


from functools import reduce

def word_count(dic, element):
    if element in dic:
        dic[element]+=1
    else :
        dic[element]=1        
    return dic

def draw_histogram(data):
    dic = reduce(word_count,data,{})
    print(dic)
    for element in dic.keys():
        print(element + ' '*(10-len(element)) + '='*dic[element])


# In[10]:


draw_histogram(data)


# ##### >>아직 Reduce 개념이 잘 이해가 안 가서 다른 친구들 도움을 많이 받았습니다ㅜㅜ
