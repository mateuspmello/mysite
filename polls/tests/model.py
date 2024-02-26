from django.test import TestCase
from polls.models import Post
from django.contrib.admin.sites import AdminSite
from django.contrib.admin.options import ModelAdmin


class TestPostTestCase(TestCase):
        
        def test_model_str(self):
                title = Post.objects.create(title="Born",content="AAAA",pub_date="1989-10-02 17:30")
                self.assertEqual(str(title), "Born")
                