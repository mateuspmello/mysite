from django.test import TestCase
from .model import *
# Create your tests here.
class CallIndex(TestCase):
        def test_index(self):
                response = self.client.get("/api/")
                actual = response.content
                expected_content = b"<!DOCTYPE html>\n<html>\n<body>\n\n<h1>Hello World!</h1>\n\n</body>\n</html>"
                self.assertEqual(actual, expected_content)
                self.assertEqual(response.status_code, 200)
        
        def test_get_post(self):
                Post.objects.create(title="Peppa",content="pig",pub_date="1989-10-02 17:30")
                response = self.client.get("/api/posts")
                actual = response.content
                expected_content = b'[{"title": "Peppa", "content": "pig"}]'
                self.assertEqual(actual, expected_content)
                self.assertEqual(response.status_code, 200)
        
        def test_get_post_with_author(self):
                a = Author(name="Jose Buendia", email="jb@gmail.com")
                a.save()
                Post.objects.create(title="Peppa",content="pig",pub_date="1989-10-02 17:30", author=a)
                Post.objects.create(title="Papai",content="pig",pub_date="2024-10-02 17:30", author=a)
                response = self.client.get("/api/posts")
                actual = json.loads(response.content)
                expected_content = [{'title': 'Peppa', 'content': 'pig', 'author_name': 'Jose Buendia', 'author_email': 'jb@gmail.com'},
                                {'title': 'Papai', 'content': 'pig', 'author_name': 'Jose Buendia', 'author_email': 'jb@gmail.com'}]
                self.assertEqual(actual, expected_content)
                self.assertEqual(response.status_code, 200)
                