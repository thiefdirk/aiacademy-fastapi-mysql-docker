import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
basedir = os.path.dirname(os.path.abspath(__file__))

from app.services.calculator import CalculatorService
from app.services.user import UserService
from app.schemas.user import Loginsequence
from app.services.score import ScoreService
from app.services.grade import GradeService

def print_menu():
    print('0. 전체프로그램 종료')
    print('1. 계산기 프로그램')
    print('2. 로그인 프로그램') # 입력받은 아이디와 비번 콘솔에 출력하기
    print('3. 성적 프로그램')
    menu = input('메뉴 선택')
    return menu
    
def main():
    while 1:
        menu = print_menu()
        if menu == '0':
            print('전체프로그램 종료')
            break
        elif menu == '1':
            calculatorService = CalculatorService() # 메소드 내부에 들어가는 코드는 변수, 문(괄호없음), 식(메소드 안에있는것, 괄호있음) 이다.             
            first = int(input('첫번째 수 입력')) # int()는 문자열을 정수로 변환하는 함수이다.
            second = int(input('두번째 수 입력'))
            calculatorService.calculate(first, second)
        elif menu == '2':
            userService = UserService()
            id = input('아이디 입력')
            password = input('비밀번호 입력')
            userService.login(id, password)
        # elif menu == '3':
        #     scoreservice = ScoreService()
        #     name = input('이름 입력')
        #     kor = int(input('국어 점수 입력'))
        #     eng = int(input('영어 점수 입력'))
        #     math = int(input('수학 점수 입력'))
        #     scoreservice.score(name, kor, eng, math)
        elif menu == '3':
            gradeservice = GradeService()
            name = input('이름 입력')
            korean = int(input('국어 점수 입력'))
            english = int(input('영어 점수 입력'))
            math = int(input('수학 점수 입력'))
            grade = gradeservice.get_grade(name, korean, english, math)
            print(grade)
            

if __name__ == '__main__':
    main()
# 이렇게 작성하면 이 파일을 실행하면 main()이 실행된다.

