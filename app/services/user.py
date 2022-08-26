from app.models.user import User
from app.schemas.user import Loginsequence

class UserService(object): 
    def __init__(self) -> None: 
        pass
        
        
    def login(self, id, password): 
        loginsequence = Loginsequence()
        loginsequence.login(id, password)