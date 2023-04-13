import os
import pathlib
import unittest

from selenium import webdriver

# "find_element_by_id" doesn't work, so import another method
from selenium.webdriver.common.by import By

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

driver = webdriver.Chrome()

class WebpageTests(unittest.TestCase):

	def test_title(self):
		driver.get(file_uri("count.html"))
		self.assertEqual(driver.title, "Count")

	def test_increase(self):
		# And also new synthax for Find_elements https://selenium-python.readthedocs.io/locating-elements.html
		driver.get(file_uri("count.html"))
		increase = driver.find_element(By.ID, "increase")
		increase.click()
		self.assertEqual(driver.find_element_by_tag_name("h1").text, "1")

	def test_increase(self):
		driver.get(file_uri("count.html"))
		decrease = driver.find_element(By.ID, "decrease")
		decrease.click()
		self.assertEqual(driver.find_element(By.TAG_NAME, "h1").text, "-1")

	def test_multiple_increase(self):
		driver.get(file_uri("count.html"))
		increase = driver.find_element(By.ID, "increase")
		for i in range(3):
			increase.click()
		self.assertEqual(driver.find_element(By.TAG_NAME, "h1").text, "3")

if __name__ == "__main__":
	unittest.main()