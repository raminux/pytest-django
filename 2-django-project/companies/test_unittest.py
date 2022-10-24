import json
import pytest
from django.test import TestCase
# from unittest import TestCase
from django.test import Client
from django.urls import reverse
from companies.models import Company

'''
It is important to create a pytest.ini file and add the following to it:
[pytest]
DJANGO_SETTINGS_MODULE = config.settings

Witthout that file, the following tests will not be run!
'''
'''
During the test, Django will build a test database. It is actually a replica for the original database. 
So, your production database will not be affected by tests!
'''


@pytest.mark.django_db
class BasicCompanyAPITestCase(TestCase):
   def setUp(self) -> None:
      self.client = Client()
      self.companies_url = reverse('companies-list')

   def tearDown(self):
      pass
     


class TestGetCompanies(BasicCompanyAPITestCase):
     # Test methods must start with test_ prefix!
   def test_zero_companies_should_return_empty_list(self) -> None:
      response = self.client.get(self.companies_url)
      self.assertEqual(response.status_code, 200)
      self.assertEqual(json.loads(response.content), [])
      
   def test_one_company_exsits_should_succeed(self) -> None:
      test_company = Company.objects.create(name='Amazon')
      response = self.client.get(self.companies_url)
      # To see the print outpus, add '-s' to pytest command.
      print(response)
      response_content = json.loads(response.content)[0]
      self.assertEqual(response.status_code, 200)
      self.assertEqual(response_content.get('name'), test_company.name)
      self.assertEqual(response_content.get('status'), Company.CompanyStatus.HIRING)
      self.assertEqual(response_content.get('application_link'), '')

      test_company.delete()
       
class TestPostCompanies(BasicCompanyAPITestCase):
   def test_create_company_without_arguments_should_fail(self) -> None:
      response = self.client.post(path=self.companies_url)
      self.assertEqual(response.status_code, 400)
      self.assertEqual(
         json.loads(response.content), 
         {'name': ['This field is required.']}
         )

   def test_create_existing_company_should_fail(self) -> None:
      Company.objects.create(name='apple')
      response = self.client.post(path=self.companies_url, data={'name': 'apple'})
      self.assertEqual(response.status_code, 400)
      self.assertEqual(
         json.loads(response.content),
         {'name': ['company with this name already exists.']}
      )
   
   def test_create_company_with_only_name_all_fields_should_be_default(self) -> None:
      response = self.client.post(path=self.companies_url, data={'name': 'test company name'})
      self.assertEqual(response.status_code, 201)
      response_content = json.loads(response.content)
      self.assertEqual(response_content.get('name'), 'test company name')
      self.assertEqual(response_content.get('status'), Company.CompanyStatus.HIRING)
      self.assertEqual(response_content.get('application_link'), '')
      self.assertEqual(response_content.get('notes'), '')

   def test_create_company_with_layoffs_status_should_succeed(self) -> None:
      response = self.client.post(path=self.companies_url, data={'name': 'test company name', 'status': 'Layoffs'})
      self.assertEqual(response.status_code, 201)
      response_content = json.loads(response.content)
      self.assertEqual(response_content.get('status'), Company.CompanyStatus.LAYOFFS)

   def test_create_company_with_wrong_status_should_fail(self) -> None:
      response = self.client.post(path=self.companies_url, data={'name': 'test company name', 'status': 'WrongStatus'})
      self.assertEqual(response.status_code, 400)
      self.assertIn('WrongStatus', str(response.content))
      self.assertIn('is not a valid choice', str(response.content))



'''
One of the most useful arguments of the pytest command is the 'duration' argument. 
It shows the amount of time consumed for each test. It helps us to find out where our resources consumed in long-running tests.
$ pytest -vv --durations=0

'''

'''
How to assert exceptions and logs during test?
'''

'''Some useful tips of pytest command
1- Run tests inside a specific directory
$ pytest -vv -s <directory>

2- Run tests that contain the specified words in their name
$ pytest -vv -s -k "create"
$ pytest -vv -s -k "create and not wrong"

3- Run tests inside the specified class in the specified file
$ pytest -vv -v <test_file_path>::TestClassName

4- Run tests with specific markers
$ pytest -vv -s -m xfail
'''

