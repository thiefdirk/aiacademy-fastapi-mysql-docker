from app.models.user import User

class UserService(object): 
    def __init__(self) -> None: # 생성자
        pass
        
        
    def useraccount(self, id, password): 
        user = User(id, password)
        print(f'아이디: {id}')
        print(f'패스워드: {password}')