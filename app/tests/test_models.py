from django.test import TestCase
from app.models import *

class TestModels(TestCase):

    def setUp(self):
        self.user = SimpleUser.objects.create(
            email="email",
            password="password",
            username="username"
        )
        self.courses = Courses.objects.create(
            course_name="course_name",
            course_description="course_description",
            sum_rating=1.0,
            count_rating=1.0,
            course_requirements="text"
        )
        self.modulle = Module.objects.create(
            module_title='module_title',
            module_of_course=self.courses,
            number_of_lecture=0
        )
        self.videos = Videos.objects.create(
            video_of_module=self.modulle,
            video_title='video_title',
            video_link='link'
        )

    def test_SimpleUser_modele(self):
        self.assertEquals(self.user.username, 'username')
        self.assertEquals(self.user.email, 'email')
        self.assertEquals(self.user.password, 'password')
        self.assertEquals(self.user.get_name(), 'username')

    def test_Courses_module(self):
        self.assertEquals(self.courses.course_name, 'course_name')
        self.assertEquals(self.courses.course_description, 'course_description')
        self.assertEquals(self.courses.sum_rating, 1.0)
        self.assertEquals(self.courses.count_rating, 1.0)
        self.assertEquals(self.courses.course_requirements, 'text')
        self.assertEquals(self.courses.get_rating(), 1.0)

    def test_Comment_module(self):
        self.comment = Comment.objects.create(
            comment_text='comment_text',
            comment_on_course=self.courses,
            comment_user=self.user
        )

        self.assertEquals(self.comment.comment_text, 'comment_text')
        self.assertEquals(self.comment.comment_on_course, self.courses)
        self.assertEquals(self.comment.comment_user, self.user)

    def test_Module_module(self):
        self.assertEquals(self.modulle.module_title, 'module_title')
        self.assertEquals(self.modulle.module_of_course, self.courses)
        self.assertEquals(self.modulle.number_of_lecture, 0)

    def test_Videos_module(self):
        self.assertEquals(self.videos.video_of_module, self.modulle)
        self.assertEquals(self.videos.video_title, 'video_title')
        self.assertEquals(self.videos.video_link, 'link')

