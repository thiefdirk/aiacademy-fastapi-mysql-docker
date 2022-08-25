import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
basedir = os.path.dirname(os.path.abspath(__file__))

from app.services.calculator import CalculatorService
from app.services.user import UserService

def print_menu():
    print('0. 전체프로그램 종료')
    print('1. 계산기 프로그램')
    print('2. 로그인 프로그램') # 입력받은 아이디와 비번 콘솔에 출력하기
    menu = input('메뉴 선택')
    return menu
    
def main():
    while 1:
        menu = print_menu()
        if menu == '0':
            print('전체프로그램 종료')
            break
        elif menu == '1':
            calculatorService = CalculatorService() # 메소드 내부에 들어가는 코드는 변수, statement, expression 이다.             
            first = int(input('첫번째 수 입력')) # int()는 문자열을 정수로 변환하는 함수이다.
            second = int(input('두번째 수 입력'))
            calculatorService.calculate(first, second)
        elif menu == '2':
            userService = UserService()
            id = input('아이디 입력')
            password = input('비밀번호 입력')
            userService.user_account(id, password)

if __name__ == '__main__':
    main()
    