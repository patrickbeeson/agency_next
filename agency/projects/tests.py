from django.core.exceptions import ValidationError
from django.test import TestCase
from django.test import RequestFactory
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
import tempfile
import os
from settings import base
from projects.models import Category, Project, AssetGroup, ImageAsset, TextAsset, VideoAsset
from projects.views import ProjectDetailView


class ProjectTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.staff_user = User.objects.create_user('staff', 'staff@test.com', 'pass')
        self.staff_user.is_staff = True

        tempfile.tempdir = os.path.join(
            base.MEDIA_ROOT, 'projects/hero_images'
        )
        tf = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
        tf.close()
        tf_invalid = tempfile.NamedTemporaryFile(delete=False, suffix='.gif')
        tf_invalid.close()

        self.hero_image = tf.name
        self.hero_image_invalid = tf_invalid.name
        tempfile.tempdir = os.path.join(
            base.MEDIA_ROOT, 'projects/assets/images'
        )
        tf_asset = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
        tf_asset.close()
        self.asset_image = tf_asset.name

        self.valid_project = Project.objects.create(
            name='Lowes Foods',
            slug='lowes-foods',
            description='Lowes Foods is a local grocery store chain.',
            hero_image=self.hero_image,
            is_featured=True,
            status='published'
        )
        self.valid_project_2 = Project.objects.create(
            name='Spinmaster',
            slug='spinmaster',
            description='Spinmaster makes children\'s toys.',
            hero_image=self.hero_image,
            is_featured=True,
            status='published'
        )
        self.invalid_project = Project.objects.create(
            name='Primo Water',
            slug='primo-water',
            description='Primo Water is a water wholeseller.',
            hero_image=self.hero_image_invalid,
            is_featured=False,
            status='published'
        )
        self.category = Category.objects.create(
            name='Digital',
            slug='digital',
            description='Digital projects.'
        )
        self.assetgroup = AssetGroup.objects.create(
            name='Lowes Foods digital',
            asset_group_type='centered',
            description='Digital screenshots for Lowes Foods redesign.',
            project=self.valid_project,
            has_emphasis=True
        )
        self.image_asset = ImageAsset.objects.create(
            name='Screenshot',
            description='Screenshot description.',
            image=self.asset_image,
            caption='Screenshot caption.',
            group=self.assetgroup
        )
        self.text_asset = TextAsset.objects.create(
            name='Blurb',
            description='Blurb description.',
            title='Blurb title',
            text='Blurb copy.',
            group=self.assetgroup
        )
        self.video_asset = VideoAsset.objects.create(
            name='Video',
            description='Video description.',
            video='http://vimeo.com/39043244',
            caption='Video caption.',
            group=self.assetgroup
        )
        self.assetgroup_list = AssetGroup.objects.all()
        self.project_list = Project.featured.all()

    def test_project_view_renders_template(self):
        slug = self.valid_project.slug
        pk = self.valid_project.pk
        request = self.factory.get(reverse('project_detail', kwargs={'slug': slug}))
        request.user = self.staff_user
        response = ProjectDetailView.as_view()(request, pk=pk)
        self.assertEqual(response.template_name[0], 'projects/project_detail.html')

    def test_project_view_returns(self):
        slug = self.valid_project.slug
        pk = self.valid_project.pk
        request = self.factory.get(reverse('project_detail', kwargs={'slug': slug}))
        request.user = self.staff_user
        response = ProjectDetailView.as_view()(request, pk=pk)
        self.assertEqual(response.status_code, 200)

    def test_project_view_renders_project_list(self):
        slug = self.valid_project.slug
        pk = self.valid_project.pk
        request = self.factory.get(reverse('project_detail', kwargs={'slug': slug}))
        request.user = self.staff_user
        response = ProjectDetailView.as_view()(request, pk=pk)
        self.assertEqual(
            response.context_data['project_list'][0], self.project_list[1]
        )

    def test_project_view_renders_assetgroup_list(self):
        slug = self.valid_project.slug
        pk = self.valid_project.pk
        request = self.factory.get(reverse('project_detail', kwargs={'slug': slug}))
        request.user = self.staff_user
        response = ProjectDetailView.as_view()(request, pk=pk)
        self.assertEqual(
            response.context_data['assetgroup_list'][0], self.assetgroup_list[0]
        )

    def test_can_create_project(self):
        project = self.valid_project
        expected = 'lowes-foods'
        self.assertEqual(project.slug, expected)

    def test_can_create_category(self):
        category = self.category
        expected = 'digital'
        self.assertEqual(category.slug, expected)

    def test_can_create_assetgroup(self):
        assetgroup = self.assetgroup
        expected = 'Lowes Foods digital'
        self.assertEqual(assetgroup.name, expected)

    def test_can_create_imageasset(self):
        image_asset = self.image_asset
        expected = 'Screenshot'
        self.assertEqual(image_asset.name, expected)

    def test_can_create_textasset(self):
        text_asset = self.text_asset
        expected = 'Blurb'
        self.assertEqual(text_asset.name, expected)

    def test_can_create_videoasset(self):
        video_asset = self.video_asset
        expected = 'Video'
        self.assertEqual(video_asset.name, expected)

    def test_invalid_file_type(self):
        project = self.invalid_project
        self.assertRaises(ValidationError, project.full_clean)

    def test_project_not_published_display(self):
        expected = Project.objects.all().count()
        observed = Project.published.all().count()
        self.assertEqual(expected, observed, "Two projects are published.")

    def test_project_featured_and_public(self):
        expected = 2
        observed = Project.featured.all().count()
        self.assertEqual(
            expected, observed, "Project that is featured is also public."
        )

    def tearDown(self):
        os.remove(self.asset_image)
        os.remove(self.hero_image)
        os.remove(self.hero_image_invalid)
        projects = Project.objects.all()
        users = User.objects.all()
        users.delete()
        categories = Category.objects.all()
        assetgroups = AssetGroup.objects.all()
        imageassets = ImageAsset.objects.all()
        textassets = TextAsset.objects.all()
        videoassets = VideoAsset.objects.all()
        projects.delete()
        categories.delete()
        assetgroups.delete()
        textassets.delete()
        imageassets.delete()
        videoassets.delete()
