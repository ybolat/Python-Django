from django.test import TestCase, Client
from django.urls import reverse
from app.models import *
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        course = Courses.objects.create(
            course_name="course_name",
            course_description="course_description",
            sum_rating=1.0,
            count_rating=1.0,
            course_requirements="text"
        )
        Module.objects.create(
            module_title="module_title",
            module_of_course=course,
            number_of_lecture=0
        )

    def test_IndexView_view(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/index.html')

    def test_registerView_view(self):
        response = self.client.get(reverse('registration'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/registration.html')

    def test_GetCourseByID_view(self):
        response = self.client.get(reverse('get_course_by_id', args=[1]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/course.html')

    def test_my_courses_view(self):
        response = self.client.get(reverse('my_courses'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/my_courses.html')

    def test_videos_of_module_view(self):
        response = self.client.get(reverse('modules', args=[1]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/search.html')

    def test_send_email_view(self):
        response = self.client.post(reverse('send_email', args=[1]))
        self.assertEquals(response.status_code, 302)

    def test_ContactsView(self):
        response = self.client.get(reverse('contactUs'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/contacts.html')

    def test_HelpView(self):
        response = self.client.get(reverse('help'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/help.html')

    def test_AboutView(self):
        response = self.client.get(reverse('aboutUs'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/about.html')

    def test_search_successView(self):
        response = self.client.get(reverse('search_success', args=[1]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/search.html')