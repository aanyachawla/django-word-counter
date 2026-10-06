from django.test import TestCase
from django.urls import reverse

class WordCounterTests(TestCase):
    def test_home_page_loads(self):
        response = self.client.get(reverse("word_counter"))
        self.assertEqual(response.status_code, 200)

    def test_word_count(self):
        response = self.client.post(
            reverse("word_counter"),
            {"text": "Hello world"}
        )
        self.assertContains(response, "2")
