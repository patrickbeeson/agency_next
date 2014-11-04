from django.core.exceptions import ValidationError
from django.test import TestCase
import tempfile
import os
from settings import base
from projects.models import Category, Project


class ProjectTest(TestCase):

    def setUp(self):
        tempfile.tempdir = os.path.join(
            base.MEDIA_ROOT, 'projects/hero_images'
        )
        tf = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
        tf_invalid = tempfile.NamedTemporaryFile(delete=False, suffix='.gif')
        tf_invalid.close()
        tf.close()
        self.hero_image = tf.name
        self.hero_image_invalid = tf_invalid.name
        Project.objects.create(
            name='Lowes Foods',
            slug='lowes-foods',
            description='Lowes Foods is a local grocery store chain.',
            hero_image=self.hero_image,
            is_featured=True
        )
        Project.objects.create(
            name='Primo Water',
            slug='primo-water',
            description='Primo Water is a water wholeseller.',
            hero_image=self.hero_image_invalid,
            is_featured=False
        )
        Category.objects.create(
            name='Digital',
            slug='digital',
            description='Digital projects.'
        )

    def test_can_create_project(self):
        project = Project.objects.get(slug='lowes-foods')
        expected = 'lowes-foods'
        self.assertEqual(project.slug, expected)

    def test_can_create_category(self):
        category = Category.objects.get(slug='digital')
        expected = 'digital'
        self.assertEqual(category.slug, expected)

    def test_invalid_file_type(self):
        project = Project.objects.get(slug='primo-water')
        self.assertRaises(ValidationError, project.full_clean)

    def test_project_not_featured_display(self):
        observed = Project.objects.all().filter(is_featured=False).count()
        expected = Project.featured.all().count()
        self.assertEqual(expected, observed, "Only one project is featured.")

    def tearDown(self):
        os.remove(self.hero_image)
        os.remove(self.hero_image_invalid)
        projects = Project.objects.all()
        categories = Category.objects.all()
        projects.delete()
        categories.delete()
