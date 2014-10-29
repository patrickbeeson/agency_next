from django.test import TestCase
import tempfile
import os
from settings import base
from projects.models import Category, Project


class ProjectTest(TestCase):

    def setUp(self):
        self.path = os.path.join(base.MEDIA_ROOT, 'projects/hero_images')
        self.hero_image = os.path.join(
            self.path, os.path.basename(tempfile.mkstemp(suffix='.jpg')[1]))
        Project.objects.create(
            name='Lowes Foods',
            slug='lowes-foods',
            description='Lowes Foods is a local grocery store chain.',
            hero_image=self.mugshot,
            is_featured=True
        )
        Category.objects.create(
            name='Digital',
            slug='digital',
            description='Digital projects.'
        )

    def test_project_creation(self):
        project = Project.objects.get(slug='lowes-foods')
        expected = 'lowes-foods'
        self.assertEqual(project.slug, expected)

    def test_category_creation(self):
        category = Category.objects.get(slug='digital')
        expected = 'digital'
        self.assertEqual(category.slug, expected)

    def test_project_featured_display(self):
        project = Project.objects.get(name='Lowes Foods').count()
        expected = Project.featured.count()
        self.assertEqual(project, expected)

    def tearDown(self):
        os.remove(self.hero_image)
        projects = Project.objects.all()
        categories = Category.objects.all()
        projects.delete()
        categories.delete()
