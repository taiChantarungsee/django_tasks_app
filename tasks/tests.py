import unittest
from django.test import TestCase, Client
from django.test.utils import setup_test_environment
from . import views

class ViewTests(TestCase):
	def setup(self):
		setup_test_environment()

	def test_url(self):
		#We assign Client() to c to keep things simple: the class will not be very big.
		c = Client()
		response = c.get('/')
		self.assertEqual(response.status_code, 200)