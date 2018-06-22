import hello
import unittest

class HelloTestCase(unittest.TestCase):
	def setUp(self):
		hello.app.testing = True
		self.app = hello.app.test_client()
	
	def tearDown(self):
		pass
#indent de oshikari wo uketa
	def test_top(self):
		response = self.app.get('/')
		html = response.data.decode('utf-8')
		self.assertIn('user list', html)
		self.assertIn('UNKOMAN', html)

	if __name__ == '__main__':
		unittest.main()
