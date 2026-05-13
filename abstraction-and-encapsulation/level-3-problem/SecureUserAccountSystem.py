class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def verify_password(self, password):
        return self.__password == password


u = User("Alex", "secure123")
print(u.verify_password("secure123"))