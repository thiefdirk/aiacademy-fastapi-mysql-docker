class Loginsequence(object):
    def __init__(self) -> None:
        pass
    
    def login(self, id, password):
        id_ = 'bob5610'
        password_ = '1234'
        if id == id_ and password == password_:
            print('로그인 성공')
        else:
            print('로그인 실패')