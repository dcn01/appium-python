#android_calculator_appium.py
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
import unittest

class AndroidCalculatorTest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Remote(
		command_executor='http://127.0.0.1:4723/wd/hub',
		desired_capabilities={'browserName': 'Android',
								'version': '4.2',
								'platform': 'Windows"',
								'app-package': 'com.android.calculator2',
								'app-activity': 'com.android.calculator2.Calculator' })

	def test_add_operation(self):
		driver = self.driver
		driver.find_element_by_name("2").click()
		driver.find_element_by_name("+").click()
		driver.find_element_by_name("4").click()
		driver.find_element_by_name("=").click()
		result = driver.find_element_by_tag_name("EditText").text
		print(result)
		self.assertIn("6",result)

	def tearDown(self):
		self.driver.close()
		
if __name__ == "__main__":
    unittest.main()