from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app.views import *


class TestUrls(SimpleTestCase):

    def test_index_url(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func.view_class, IndexView)

    def test_registration_url(self):
        url = reverse('registration')
        self.assertEquals(resolve(url).func.view_class, registerView)

    def test_purchase_url(self):
        url = reverse('purchase', args=[1])
        self.assertEquals(resolve(url).func, purchase_courses)

    def test_modules_url(self):
        url = reverse('modules', args=[1])
        self.assertEquals(resolve(url).func, videos_of_module)

    def test_rate_course_url(self):
        url = reverse('rate_course', args=[1])
        self.assertEquals(resolve(url).func, rate_course)

    def test_get_course_by_id_url(self):
        url = reverse('get_course_by_id', args=[1])
        self.assertEquals(resolve(url).func.view_class, GetCourseByID)

    def test_leave_comment_url(self):
        url = reverse('leave_comment', args=[1])
        self.assertEquals(resolve(url).func, leave_comment)

    def test_allCourses_url(self):
        url = reverse('allCourses')
        self.assertEquals(resolve(url).func.view_class, AllCourses)

    def test_aboutUs_url(self):
        url = reverse('aboutUs')
        self.assertEquals(resolve(url).func.view_class, AboutView)

    def test_help_url(self):
        url = reverse('help')
        self.assertEquals(resolve(url).func.view_class, HelpView)

    def test_contactUs_url(self):
        url = reverse('contactUs')
        self.assertEquals(resolve(url).func.view_class, ContactsView)

    def test_my_curses_url(self):
        url = reverse('my_courses')
        self.assertEquals(resolve(url).func, my_courses)

    def test_search_by_course_text_url(self):
        url = reverse('search_by_course_text')
        self.assertEquals(resolve(url).func, search_by_course_text)

    def test_search_success_url(self):
        url = reverse('search_success', args=["hello"])
        self.assertEquals(resolve(url).func, search_success)

    def test_send_email_url(self):
        url = reverse('send_email', args=[1])
        self.assertEquals(resolve(url).func, send_email)


