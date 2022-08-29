from app.services.calculator import CalculatorService
from app.services.user import UserService
from app.services.grade import GradeService
from app.services.pandas_quiz import Pandas_Quiz
import icecream as ic
from app.constants.menus import LOGIN, LOGOUT, CALCULATOR, GRADE, \
    QUIZ_1, QUIZ_2, QUIZ_3, QUIZ_4, QUIZ_5, QUIZ_6, QUIZ_7
class Url:
    
    def router(self, menu):
        if menu == LOGIN:
            UserService().login(
                input('id'), 
                input('password'))
        elif menu == CALCULATOR:
            CalculatorService().calculate(
                int(input('첫번째 값 입력: ')), 
                int(input('두번째 값 입력: ')))
        elif menu == GRADE:
            name = input('이름')
            korean = int(input('국어'))
            english = int(input('영어'))
            math = int(input('수학'))
            print(f'이름: {name} \
                학점: {GradeService().get_grade(name,korean, english, math)}')
        elif menu == QUIZ_1: Pandas_Quiz().q1()
        elif menu == QUIZ_2: Pandas_Quiz().q2()
        elif menu == QUIZ_3: Pandas_Quiz().q3()
        elif menu == QUIZ_4: 
            Pandas_Quiz().q4()
        elif menu == QUIZ_5: 
            col = input('과목명')
            Pandas_Quiz().q5(col)
        elif menu == QUIZ_6: 
            col = input('이름')
            Pandas_Quiz().q6(col)
        elif menu == QUIZ_7: Pandas_Quiz().q7()
        

            