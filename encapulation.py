class user:

    def __init__(self,username,password) :
        self.username = username
        self.__password = password

    def change_password(self,old_password, new_password):

        if self.__verify_password(old_password):
            self.__password = new_password
            print("Password changed successfully")
        else :
            print("Old password is in correct.")

    def __verify_password(self,password):
        return self.__password == password
    
    def get_username(self):
        return self.username
    
    def __set_password(self,password):
        self.__password = password

    def display_user(self):
        print(f"username:{self.username}")

user1 = user("james","james2015")

try:
    print(user1.__password)
except AttributeError as e:
    print(e)

user1.display_user()
user1.change_password("wrongpasdd","sdagrh")
user1.change_password("james2015","james2017")

try:
    user1.__verify_password("james2017")
except AttributeError as e:
    print(e)

user1.change_password("james2017","james2018")
