from django.test import TestCase
from polls.models import *


class TestModels(TestCase):
        
        def test_create_post(self):
                firstPost = Post.objects.create(title="How to build a city",content="A city of Macondo is the smallest city of the world, but veri charming and peaceful",pub_date="1989-10-02 17:30")
                expected = "A city of Macondo is the smallest city of the world, but veri charming and peaceful"
                self.assertEqual(firstPost.content, expected)
        
        def test_create_post_with_author(self):
                a = Author(name="José Buendia", email="joseb@gmail.com")
                a.save()
                p = Post.objects.create(title="Vai", content="pra casa", pub_date="2024-02-27 09:48", author=a)
                self.assertEqual(p.author.name, "José Buendia")

        def test_create_author(self):
                firstAuthor = Author.objects.create(name="José Buendia", email="joseb@gmail.com")
                self.assertEqual(firstAuthor.name, "José Buendia")

        def test_getPostsJSON(self):
                a = Author(name="José Buendia", email="joseb@gmail.com")
                a.save()
                p = Post.objects.create(title="Vai", content="pra casa", pub_date="2024-02-27 09:48", author=a)
                allPostsJSON = p.getPostsJSON()
                allPostsDict = json.loads(allPostsJSON)
                self.assertEqual(allPostsDict[0]["author_name"], "José Buendia")
