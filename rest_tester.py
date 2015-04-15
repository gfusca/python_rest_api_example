import unittest
from test_user_authentication import TestAuthenticationRestApi

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(TestAuthenticationRestApi)
	unittest.TextTestRunner().run(suite)
   
