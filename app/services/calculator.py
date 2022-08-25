from app.models.calculator import Calculator

class CalculatorService(object): 
    def __init__(self) -> None: # 생성자
        pass
        
        
    def calculate(self, first, second):
        calculator = Calculator(first, second)
        print(f'첫번째수: {first}')
        print(f'두번째수: {second}')
        print(f'{first} + {second} = {calculator.sum()}')
        print(f'{first} - {second} = {calculator.subtract()}')
        print(f'{first} * {second} = {calculator.multiply()}')
        print(f'{first} / {second} = {calculator.divide()}')