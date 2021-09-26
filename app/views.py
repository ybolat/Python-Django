from datetime import timezone, datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, TemplateView
from .forms import *
from .permissions import IsStaffOrNot
from .serializers import *
from rest_framework import status, generics, permissions
from rest_framework.decorators import api_view  # making sure to receive Request, add context to Response
from rest_framework.response import Response  # is needed to return client defined response
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class IndexView(ListView):
    template_name = "app/index.html"
    context_object_name = "latest_courses"
    queryset = Courses.objects.order_by('course_name')


class registerView(CreateView):
    form_class = SimpleUserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registration.html'


class GetCourseByID(DetailView):
    model = Courses
    template_name = "app/course.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments_of_course'] = Comment.objects.filter(comment_on_course=self.object.id)
        context['modules_of_course'] = Module.objects.filter(module_of_course=self.object.id)
        crs_obj = self.get_object()
        crs_obj.save()
        return context


class AllCourses(ListView):
    template_name = 'app/all_course.html'
    context_object_name = 'all_course'
    queryset = Courses.objects.order_by('course_name')


def my_courses(request):
    result = Purchased_Courses.objects.filter(pc_user=request.user.id)
    return render(request, "app/my_courses.html",
                  {"result": result, "empty_result": "There is no courses"})


def videos_of_module(request, id):
    id2 = Module.objects.get(pk=id).module_of_course.id
    if check_for_purchased(request, id2):
        result = Videos.objects.filter(video_of_module=Module.objects.get(pk=id))
        return render(request, "app/modules.html",
                      {"result": result, "empty_result": "There is no videos"})
    else:
        return render(request, "app/search.html", {"empty_res": "You didnt purchased this course"})


def purchase_courses(request, id):
    if request.method == 'POST':
        course = Courses.objects.get(pk=id)
        try:
            Purchased_Courses.objects.get(pc_user=request.user,
                                          pc_course=course)
        except:
            purchase_object = Purchased_Courses(pc_user=request.user,
                                                pc_course=course)
            purchase_object.save()

        return redirect("index")


def send_email(request, id):
    if request.method == 'POST':
        users = SimpleUser.objects.order_by('id')
        course = Courses.objects.get(pk=id)
        msg = MIMEMultipart()
        message = 'У нас новый курс, Название курса :' + course.course_name + " http://127.0.0.1:8000/course/" + str(course.id)
        msg.attach(MIMEText(message, 'plain'))
        server = smtplib.SMTP('smtp.mail.ru: 25')
        server.starttls()
        for user in users:
            to_email = user.email
            server.login("ngfnotify@mail.ru", "faraonlovewith02")
            server.sendmail("ngfnotify@mail.ru", to_email, msg.as_string())
        server.quit()
        return redirect("index")

def check_for_purchased(request, id):
    check = True
    try:
        Purchased_Courses.objects.get(pc_user=request.user.id,
                                      pc_course=Courses.objects.get(pk=id))
    except:
        check = False
    return check

def leave_comment(request, id):
    if check_for_purchased(request, id):
        if request.method == 'POST' and len(request.POST.get("comment_text")) > 0:
            print(request.POST.get("comment_text"), type(request.POST.get("comment_text")), type(request.user.id))
            comment_object = Comment(comment_text=request.POST.get("comment_text"),
                                     comment_on_course=Courses.objects.get(pk=id),
                                     comment_user=SimpleUser.objects.get(pk=request.user.id))
            comment_object.save()
            return redirect("get_course_by_id", pk=id)
        else:
            return render(request, "app/search.html", {"empty_res": "There is no course"})
    else:
        return render(request, "app/search.html", {"empty_res": "You didnt purchased this course"})


def rate_course(request, id):
    if check_for_purchased(request, id):
        if request.method == 'POST':
            if request.POST.get("rate_val"):
                print(type(request.POST.get("rate_val")))
                course_obj = Courses.objects.get(pk=id)
                course_obj.sum_rating = course_obj.sum_rating + float(request.POST.get("rate_val"))
                course_obj.count_rating = course_obj.count_rating + 1;
                course_obj.save()
                return redirect("get_course_by_id", pk=id)
            else:
                return render(request, "app/search.html", {"empty_res": "There is no course"})
    else:
        return render(request, "app/search.html", {"empty_res": "You didnt purchased this course"})


class ContactsView(TemplateView):
    template_name = "app/contacts.html"

class HelpView(TemplateView):
    template_name = "app/help.html"

class AboutView(TemplateView):
    template_name = "app/about.html"


def search_by_course_text(request):
    if request.method == "POST" and len(request.POST.get("search_field")) > 0:
        searching_text = request.POST.get("search_field")
        return redirect("search_success", text=searching_text)
    else:
        return render(request, "app/search.html",
                      {"empty_res": "There is no article"})


def search_success(request, text):
    if len(text) > 0:
        search_res = Courses.objects.filter(course_name__contains=text)
        return render(request, "app/search.html",
                      {"search_res": search_res, "empty_res": "There is no article"})


class CoursesListAPI(generics.ListCreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrNot]

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(generics.ListCreateAPIView, self).get_serializer(*args, **kwargs)


class CommentsListAPI(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrNot]

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(generics.ListCreateAPIView, self).get_serializer(*args, **kwargs)


class CommentDetailsAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrNot]

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(generics.RetrieveUpdateDestroyAPIView, self).get_serializer(*args, **kwargs)


class UsersListAPI(generics.ListAPIView):
    queryset = SimpleUser.objects.all()
    serializer_class = SimpleUserSerializer


class UserDetailsAPI(generics.RetrieveAPIView):
    queryset = SimpleUser.objects.all()
    serializer_class = SimpleUserSerializer
