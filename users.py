class Users:
    def __init__(self,name,sex,age):
        '''initialize user info'''
        self.name = name
        self.sex = sex
        self.age = age
        self.numlogin = 1

    def describe_user(self):
        '''describes the user'''
        print(f"{self.name} is a {self.sex} that is {self.age} years old.")

    def greet_user(self):
        '''greets the user'''
        print(f"Hello, {self.name}! Welcome!!!")

    def login_attempts(self):
        '''counts the number of login attempts'''
        print(f" login attempts: {self.numlogin}")
              
    def increment_login(self):
        '''increments login attempts by 1'''
        self.numlogin += 1

    def reset_login(self):
        '''resets the number of login attempts'''
        self.numlogin = 0


first_user = Users('Bob','Male',32)

first_user.describe_user()
first_user.greet_user()

second_user = Users('Jan','female',28)

second_user.greet_user()
second_user.describe_user()
second_user.login_attempts()
second_user.increment_login()
second_user.login_attempts()
second_user.reset_login()
second_user.login_attempts()
