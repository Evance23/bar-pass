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
def login_user(username,password):
    """
    function that checks whether a user exist and then login the user in.
    """
  
    check_user = Records.verify_user(username,password)
    return check_user

def create_new_record(account,userName,password):
    """
    Function that creates new records for a given user account
    """
    new_record = Records(account,userName,password)
    return new_record
def save_record(record):
    """
    Function to save records
    """
    record. save_details()
def display_accounts_details():
    """
    Function that returns all the saved accounts
    """
    return Records.display_records()
def delete_record(records):
    """
    Function to delete the records in the list
    """
    record.delete_record()

def find_record(account):
  
    return Records.find_record(account)
def check_records(account):
    
    return Records.if_record_exist(account)

def generate_password():
    '''
    generates a random password for the user.
    '''
    auto_password=Records.generate_password()
    return auto_password

def copy_password(account):

    return Records.copy_password(account)




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