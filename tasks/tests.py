import unittest
from django.test import TestCase, Client
from django.test.utils import setup_test_environment
from . import views

class ViewTests(TestCase):

	fixtures = ['initial_data.json']

	def setup(self):

		self.client = Client()
		setup_test_environment()

	def test_task_list(self):

		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Hello! Welcome to Tai's Blog!")
		self.assertQuerysetEqual(response.context['tasks'], [])

	def test_authentication(self):

		response = self.client.get('/login/')
		self.assertEqual(response.status_code, 200)

		response = self.client.get('/logout/')
		self.assertEqual(response.status_code, 200)

		#response = c.get('task/1/edit')
		#self.assertEqual(response.status_code, 200)