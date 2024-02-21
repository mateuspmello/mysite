from django.test import TestCase
from django.test import Client

# Create your tests here.
class CallIndex(TestCase):
        def test_index(self):
                client = Client()
                response = client.get("/")
                actual = response.content
                expected_content = b"<!DOCTYPE html>\n<html>\n<body>\n\n<h1>Hello World!</h1>\n\n</body>\n</html>"
                self.assertEqual(actual, expected_content)
                self.assertEqual(response.status_code, 200)