from django.contrib.auth.models import AbstractUser
from django.db import models

class SimpleUser(AbstractUser):

    def __str__(self):
        return self.username

    def get_name(self):
        return self.username

class Courses(models.Model):
    course_name = models.CharField(max_length=1000)
    course_description = models.TextField('description')
    course_date = models.DateTimeField('date created', auto_now_add=True)
    sum_rating = models.FloatField(default=0.0)
    count_rating = models.FloatField(default=0.0)
    course_requirements = models.TextField('requirements')

    def __str__(self):
        return self.course_name

    def get_rating(self):
        return int(self.sum_rating / self.count_rating * 100) / 100

class Comment(models.Model):
    comment_text = models.TextField('comment_text')
    comment_on_course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(SimpleUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_text

class Module(models.Model):
    module_title = models.TextField('module_title')
    module_of_course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    number_of_lecture = models.IntegerField(default=0)

    def __str__(self):
        return self.module_title

class Videos(models.Model):
    video_of_module = models.ForeignKey(Module, on_delete=models.CASCADE)
    video_title = models.TextField('video_title')
    video_link = models.TextField('link')

    def __str__(self):
        return self.video_title

class Purchased_Courses(models.Model):
    pc_date = models.DateTimeField('date purchased', auto_now_add=True)
    pc_user = models.ForeignKey(SimpleUser, on_delete=models.CASCADE)
    pc_course = models.ForeignKey(Courses, on_delete=models.CASCADE)