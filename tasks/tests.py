import unittest
from django.test import TestCase, Client
from django.test.utils import setup_test_environment
from .forms import TaskForm

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

	def test_add(self):

		response = self.client.get('/add/')
		self.assertEqual(response.status_code, 200)

		#Add a task
		response = self.client.post('/add/', {'title': 'test',})
		self.assertEqual(response.status_code, 302)

		#Add a task with an invalid title
		response = self.client.post('/add/', {'name': 23,})
		self.assertEqual(response.status_code, 200)


	def test_complete(self):

		#Test that we get the right response for a non-existent task
		response = self.client.get('complete/44')
		self.assertEqual(response.status_code, 404)

class FormTests(TestCase):

		def test_forms(self):
			data = {'title': 'test', 'text': 'this is a test'}
			form = TaskForm(data=data)
			self.assertTrue(form.is_valid())

			#now test the form with false field and then entry data
			data = {'name': 'test', 'text': 'this is a test'}
			form = TaskForm(data=data)
			self.assertTrue(not form.is_valid())