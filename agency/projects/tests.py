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
        tf = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
        tf.close()
        self.hero_image = tf.name
        Project.objects.create(
            name='Lowes Foods',
            slug='lowes-foods',
            description='Lowes Foods is a local grocery store chain.',
            hero_image=self.hero_image,
            is_featured=True
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

    def test_project_featured_display(self):
        observed = Project.objects.get(name='Lowes Foods')
        expected = Project.featured.get(name='Lowes Foods')
        self.assertEqual(observed, expected)

    def tearDown(self):
        os.remove(self.hero_image)
        projects = Project.objects.all()
        categories = Category.objects.all()
        projects.delete()
        categories.delete()
