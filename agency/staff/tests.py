from django.test import TestCase
import tempfile
import os
from settings import base
from staff.models import Employee
from django.core.exceptions import ValidationError


class StaffTest(TestCase):

    def setUp(self):
        tempfile.tempdir = os.path.join(
            base.MEDIA_ROOT, 'staff/mugshots'
        )
        tf = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
        tf_invalid = tempfile.NamedTemporaryFile(delete=False, suffix='.gif')
        tf_invalid.close()
        tf.close()
        self.mugshot = tf.name
        self.mugshot_invalid = tf_invalid.name
        Employee.objects.create(
            first_name='Patrick',
            middle_name='Scott',
            last_name='Beeson',
            title='Director of Digital Strategy',
            brief_description='Mountains require grit',
            mugshot=self.mugshot,
            is_employed=True
        )
        Employee.objects.create(
            first_name='Joe',
            middle_name='Data',
            last_name='Reporter',
            title='Director of Data Reporting',
            brief_description='I love numbers',
            mugshot=self.mugshot_invalid,
            is_employed=False
        )

    def test_can_create_employee(self):
        employee = Employee.objects.get(first_name='Patrick')
        expected = 'Patrick'
        self.assertEqual(employee.first_name, expected)

    def test_invalid_file_type(self):
        employee = Employee.objects.get(first_name='Joe')
        self.assertRaises(ValidationError, employee.full_clean)

    def test_employee_not_public_display(self):
        observed = Employee.objects.all().filter(is_employed=False).count()
        expected = Employee.public.all().count()
        self.assertEqual(expected, observed, "Only one employee is public.")

    def tearDown(self):
        os.remove(self.mugshot)
        os.remove(self.mugshot_invalid)
        employees = Employee.objects.all()
        employees.delete()
