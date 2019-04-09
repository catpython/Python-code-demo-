import unittest
from b4 import Myclass

class TestMathFunc(unittest.TestCase):
  
	def test_add(self):
		self.assertTrue(Myclass.isMatch(self,"aa","*"))
		print()
		self.assertFalse(Myclass.isMatch(self,"ww","*b"))
		print()
		self.assertEqual(True, Myclass.isMatch(self,"adceb","*a*b"))
		print()
		self.assertNotEqual(True, Myclass.isMatch(self,"cb","?a"))
		print()
	
		
		
if __name__ == '__main__':	
	unittest.main()