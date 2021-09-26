from django.test import TestCase
from app.models import *

class TestModels(TestCase):

    def setUp(self):
        self.user = SimpleUser.objects.create(
            email="email",
            password="password",
            username="username"
        )

    def test_SimpleUser_modele(self):
        self.assertEquals(self.user.username, 'username')
        self.assertEquals(self.user.email, 'email')
        self.assertEquals(self.user.password, 'password')
        self.assertEquals(self.user.get_name(), 'username')

    def test_Courses_module(self):
        self.courses = Courses.objects.create(
        course_name="course_name",
        course_description = "course_description",
        sum_rating = 1.0,
        count_rating = 1.0,
        course_requirements = "text"
        )
        self.assertEquals(self.courses.course_name, 'course_name')
        self.assertEquals(self.courses.course_description, 'course_description')
        self.assertEquals(self.courses.sum_rating, 1.0)
        self.assertEquals(self.courses.count_rating, 1.0)
        self.assertEquals(self.courses.course_requirements, 'text')
        self.assertEquals(self.courses.get_rating(), 1.0)

