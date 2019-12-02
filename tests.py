from add import add
import unittest

class TestAdd(unittest.TestCase):
	def testInit(self):
		elem1 = 1
		elem2 = 3
		additionResult = 4
		wrongAdditionResult = 5
		computeResult = add.add(elem1,elem2).get()
		self.assertEqual(computeResult,additionResult)

if __name__ == '__main__':
	unittest.main()
