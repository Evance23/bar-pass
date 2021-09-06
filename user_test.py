import unittest
from user import User
from user import Records

class UserTest(unittest.TestCase):
    
    '''
    test class that defines test cases for the user class
    '''
    def setUp(self):
        self.new_user = User('User','0123')

    def test_init(self):
        '''
        test case to check if its initialized properly
        '''
        self.assertEqual(self.new_user.username,'User')
        self.assertEqual(self.new_user.password,'0123')