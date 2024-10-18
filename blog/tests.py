from django.test import TestCase
from django.urls import reverse

class PostDetailViewTests(TestCase):

    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detail', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Meu Primeiro Post')
