from django.test import TestCase
from .model import *
# Create your tests here.
class CallIndex(TestCase):
        def test_index(self):
                response = self.client.get("/polls/")
                actual = response.content
                expected_content = b"<!DOCTYPE html>\n<html>\n<body>\n\n<h1>Hello World!</h1>\n\n</body>\n</html>"
                self.assertEqual(actual, expected_content)
                self.assertEqual(response.status_code, 200)
        
        def test_get_post(self):
                Post.objects.create(title="Peppa",content="pig",pub_date="1989-10-02 17:30")
                response = self.client.get("/polls/posts")
                actual = response.content
                expected_content = b'[{"model": "polls.post", "pk": 1, "fields": {"title": "Peppa", "pub_date": "1989-10-02T17:30:00Z", "content": "pig", "author": null}}]'
                self.assertEqual(actual, expected_content)
                self.assertEqual(response.status_code, 200)
        
        def test_get_post_with_author(self):
                a = Author(name="José Buendia", email="jb@gmail.com")
                a.save()
                Post.objects.create(title="Peppa",content="pig",pub_date="1989-10-02 17:30", author=a)
                response = self.client.get("/polls/posts")
                actual = response.content
                expected_content = b'[{"model": "polls.post", "pk": 2, "fields": {"title": "Peppa", "pub_date": "1989-10-02T17:30:00Z", "content": "pig", "author": 1}}]'
                self.assertEqual(actual, expected_content)
                self.assertEqual(response.status_code, 200)
                