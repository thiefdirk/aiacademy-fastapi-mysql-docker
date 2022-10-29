import pandas as pd
from icecream import ic
import random
import string
import numpy as np

class Pandas_Quiz(object):  
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
        
    #     '''
    # def q4(self):
    #     self.id = ''.join(random.sample(string.ascii_letters, 5)) # 알파벳 5자리 ID 로 표기
    #     self.score = random.randint(0, 100) # 0 ~ 100 사이의 점수           
       
        
    #     index_list = []
    #     score_list = []
    #     index_break = 0
    #     score_break = 0
        
    #     while index_break < 10:
    #         id = self.id
    #         index_list.append(id)
    #         index_break += 1
    #         self.id = 0.0
        
    #     while score_break < 40:
    #         score = self.score
    #         score_list.append(score)
    #         score_break += 1
    #         self.score = 0.0
            
    #     dataframe = pd.DataFrame({'국어': score_list[0:10], '영어': score_list[10:20], '수학': score_list[20:30], '사회': score_list[30:40]}, index=index_list)
    #     ic(self.id)
    #     ic(self.score)
    #     ic(dataframe)
    def get_id(self):
        return ["".join(([random.choice(string.ascii_letters)for i in range(5)])) for i in range(10)]

    def get_score(self):
        return np.random.randint(0, 100,(10,4))  

    
    def q4(self):
        index_list = self.get_id()
        score_list = self.get_score()            
        dataframe = pd.DataFrame(score_list, index=index_list, columns=['국어', '영어', '수학', '사회'])
        id = self.get_id()[0]
        score = self.get_score()[0][0]
        ic(id)
        ic(score)
        ic(dataframe)
        return dataframe
        
    def q5(self, columns):
        # index_list = self.get_id()
        # score_list = self.get_score()            
        # dataframe = pd.DataFrame(score_list, index=index_list, columns=['국어', '영어', '수학', '사회'])
        score = self.q4()
        print(score[''+columns])
        
    def q6(self, id):
        print(f'{id}의 성적출력')
        score = self.q4()
        print(score.iloc[0]) 
        
    def q7(self):
        score = self.q4()
        person_total = pd.DataFrame(score.sum(axis=1), columns=['총점'])
        total = pd.concat([score, person_total], axis = 1)
        subject_total = pd.DataFrame({'국어' : np.sum(total, axis=0)[0],
                                      '영어' : np.sum(total, axis=0)[1],
                                      '수학' : np.sum(total, axis=0)[2],
                                      '사회' : np.sum(total, axis=0)[3],
                                      '총점' : np.sum(total, axis=0)[4],}, index=['과목총점'])
        total_ = pd.concat([total, subject_total], axis = 0)
        ic(total_)
        
    
        
            

###########