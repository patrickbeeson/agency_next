from django.test import TestCase
import tempfile
import os
from settings import base
from staff.models import Employee


class StaffTest(TestCase):

    def setUp(self):
        tempfile.tempdir = os.path.join(
            base.MEDIA_ROOT, 'staff/mugshots'
        )
        tf = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
        tf.close()
        self.mugshot = tf.name
        Employee.objects.create(
            first_name='Patrick',
            middle_name='Scott',
            last_name='Beeson',
            title='Director of Digital Strategy',
            brief_description='Mountains require grit',
            mugshot=self.mugshot,
            is_employed=True
        )

    def test_can_create_employee(self):
        employee = Employee.objects.get(first_name='Patrick')
        expected = 'Patrick'
        self.assertEqual(employee.first_name, expected)

    def test_employee_public_display(self):
        observed = Employee.objects.get(first_name='Patrick')
        expected = Employee.public.get(first_name='Patrick')
        self.assertEqual(observed, expected)

    def tearDown(self):
        os.remove(self.mugshot)
        employees = Employee.objects.all()
        employees.delete()
