from django.test import TestCase
from django.test import TestCase
from .models import Post
from django.urls import reverse

# here using Testcase instead of usin SimpleTestCase because we works on database\
# TestCase create a test database,it's don't need to run tests on actual database
# let's check database on dummy data


class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='just a test') # here create a object for testing purpose

    def test_text_content(self):
        post = Post.objects.get(id=1) # get the post which is 'just a test',automatically create id from django
        expected_object_name = f'{post.text}' # f strings let us put variables directly in our strings as long as the variables are surrounded by the brackets
        self.assertEqual(expected_object_name, 'just a test') # check the strings


class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text='this is another test') # create a dummy objects in model

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/') # get the url and latter check the url get Http request or not
        self.assertEqual(resp.status_code, 200) # condition check whether it exists HTTP 200 response

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home')) # get the view function which reverse home fucntio
        self.assertEqual(resp.status_code, 200) # here checking the url by name whether it get HTTP 200 requst or not

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200) # check the Http request
        self.assertTemplateUsed(resp, 'home.html') # check the view function which return home with the correct template or not