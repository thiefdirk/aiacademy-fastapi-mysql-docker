import pandas as pd
from icecream import ic
import random
import string

class Pandas_Quiz(object):
    def __init__(self) -> None:
        pass
    
    

        '''
        Q1. 다음 결과 출력
           a  b  c
        1  1  3  5
        2  2  4  6
        ic| df1:    a  b  c
                 1  1  3  5
                 2  2  4  6
        '''
    
    def q1(self) :
        # dataframe = pd.DataFrame(data={'a':[1,2],'b':[3,4],'c':[5,6]}) 
        dataframe = pd.DataFrame.from_dict({'1':[1, 3, 5], '2':[2, 4, 6]}, orient='index', columns=['a', 'b', 'c']) # from_dict : dict -> dataframe
        print(dataframe)
        ic(dataframe)
        
        '''         
    Q2. 다음 결과 출력
        A   B   C
    1   1   2   3
    2   4   5   6
    3   7   8   9
    4  10  11  12
    ic| df2:     A   B   C
                1   1   2   3
                2   4   5   6
                3   7   8   9
                4  10  11  12
    '''
    def q2(self) :
        dataframe = pd.DataFrame.from_dict({'1':[1, 2, 3], '2':[4, 5, 6], '3':[7, 8, 9], '4':[10, 11, 12]}, orient='index', columns=['A', 'B', 'C'])
        print(dataframe)
        ic(dataframe)

    def q3(self) :
        num1 = random.sample(range(1, 100), 6, replace=True)
        
        dataframe = pd.DataFrame({'0': [num1[0], num1[1]],'1': [num1[2], num1[3]],'2': [num1[4], num1[5]]})
        ic(dataframe)
        
        
        ''' 
        
        Q4 국어, 영어, 수학, 사회 4과목을 시험치른 10명의 학생들의 성적표 작성. 단 점수 0 ~ 100이고 학생은 랜덤 알파벳 5자리 ID 로 표기
        ic| self.id(): 'HKKHc'
        ic| self.score(): 22
        ic| df4:        국어  영어  수학  사회
               lDZid  57  90  55  24
               Rnvtg  12  66  43  11
               ljfJt  80  33  89  10
               ZJaje  31  28  37  34
               OnhcI  15  28  89  19
               claDN  69  41  66  74
               LYawb  65  16  13  20
               QDBCw  44  32   8  29
               PZOTP  94  78  79  96
               GOJKU  62  17  75  49
        
        '''
    def q4(self):
        index_list = []
        score_list = []
        index_break = 0
        score_break = 0
        
        while index_break < 10:
            self.id = ''.join(random.sample(string.ascii_letters, 5)) # 알파벳 5자리 ID 로 표기
            index_list.append(self.id)
            index_break += 1
        
        while score_break < 40:
            self.score = random.randint(0, 100) # 0 ~ 100 사이의 점수           
            score_list.append(self.score)
            score_break += 1
            
        dataframe = pd.DataFrame({'국어': score_list[0:10], '영어': score_list[10:20], '수학': score_list[20:30], '사회': score_list[30:40]}, index=index_list)


        ic(self.id)
        ic(self.score)
        ic(dataframe)


        