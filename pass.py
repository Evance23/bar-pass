import random
from user import User , Records

 
def create_new_user(username,password):
    '''
    Function to create a new user with a username and password
    '''
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''
    Function to save a new user
    '''
    user.save_user()
def display_user():
    """
    Function to display existing user
    """
    return User.display_user()




    
def main():
    print('\n')
    print(" Welcome to Bar-Pass!!!")
    print("To proceed, select the following: \n \t\t CA-Create New Account  \n \t\t LI-Login to your account")
    short_code=input("").lower().strip()


    if short_code == "ca":
        username = input("User_name: ")
        while True:
            print(" \n\t\t TP-To type your own pasword: \n\t\t GP-To generate random Password")
            password_Choice = input()
            if password_Choice =='tp':
                password = input("Enter Password\n")
                break
            elif password_Choice == 'gp':
                password = generate_password()
                break








if __name__ == '__main__':
        main()