from django.test import TestCase
from .models import Person
# Create your tests here.

class PersonTestCase(TestCase):
    def test_person_info(self):
        All = Person.objects.all()
        self.assertEqual(All.count(),0)
