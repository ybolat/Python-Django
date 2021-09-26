from django.urls import path
from django.contrib.auth.views import auth_login
from .views import *

urlpatterns = [
    path('api/courses/all/', CoursesListAPI.as_view(), name='api-courses-list'),
    path('api/comments/all', CommentsListAPI.as_view(), name='api-comment-details'),
    path('api/comments/comment/<int:pk>/', CommentDetailsAPI.as_view(), name='api-comment-details'),
    path('', IndexView.as_view(), name='index'),
    path("register/", registerView.as_view(), name="registration"),
    path('', auth_login, name="login"),
    path('course/<int:id>/purchase', purchase_courses, name="purchase"),
    path("modules/<int:id>", videos_of_module, name="modules"),
    path('course/<int:pk>/', GetCourseByID.as_view(), name='get_course_by_id'),
    path('course/<int:id>/rate', rate_course, name='rate_course'),
    path('course/<int:id>/leaving_comment', leave_comment, name='leave_comment'),
    path('all_course/', AllCourses.as_view(), name="allCourses"),
    path('aboutUs', AboutView.as_view(), name="aboutUs"),
    path('help', HelpView.as_view(), name="help"),
    path("contactUs", ContactsView.as_view(), name="contactUs"),
    path("my_curses/", my_courses, name="my_courses"),
    path('search/', search_by_course_text, name='search_by_course_text'),
    path('search/<str:text>/', search_success, name='search_success'),
    path("course/<int:id>/notify", send_email, name="send_email")
]
