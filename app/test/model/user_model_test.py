from django.test import TestCase
from app.model.snippet import Snippet


class SnippetModelTest(TestCase):
    def setUp(self) -> None:
        self.snippet: Snippet = Snippet.objects.create()

    def test_create(self):
        pass
