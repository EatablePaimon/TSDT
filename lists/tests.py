from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest  # (#1)
from django.template.loader import render_to_string

class HomePageTest(TestCase):
    # def test_home_page_return_correct_html(self):  # (#2)
    #     request = HttpRequest()  # (#1)
    #     response = home_page(request)  # (#2)
    #     html = response.content.decode('utf-8')  # (#3)
    #     self.assertTrue(html.startswith('<html>'))  # (#4)
    #     self.assertIn('<title>To-Do lists</title>', html)  # (#5)
    #     self.assertTrue(html.endswith('</html>'))  # (#4)
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response,'home.html')
# Create your tests here.
