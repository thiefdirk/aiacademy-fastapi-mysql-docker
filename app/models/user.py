class User(object):
    def __init__(self, id, password):
        self.id = id
        self.password = password

    def useraccount(self):
        return self.id, self.password