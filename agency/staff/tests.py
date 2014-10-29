from django.test import TestCase
import tempfile
import os
from settings import base
from staff.models import Employee


class StaffTest(TestCase):

    def setUp(self):
        self.path = os.path.join(base.MEDIA_ROOT, 'staff/mugshots')
        self.mugshot = os.path.join(
            self.path, os.path.basename(tempfile.mkstemp(suffix='.jpg')[1]))
        Employee.objects.create(
            first_name='Patrick',
            middle_name='Scott',
            last_name='Beeson',
            title='Director of Digital Strategy',
            brief_description='Mountains require grit',
            mugshot=self.mugshot,
            is_employed=True
        )

    def test_employee_name(self):
        employee = Employee.objects.get(first_name='Patrick')
        expected = 'Patrick'
        self.assertEqual(employee.name, expected)

    def test_employee_public_display(self):
        employee = Employee.objects.get(first_name='Patrick').count()
        expected = Employee.public.count()
        self.assertEqual(employee, expected)

    def tearDown(self):
        os.remove(self.mugshot)
        employees = Employee.objects.all()
        employees.delete()
