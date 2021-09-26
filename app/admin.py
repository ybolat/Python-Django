from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Courses)
admin.site.register(Comment)
admin.site.register(Module)
admin.site.register(Videos)
admin.site.register(SimpleUser)
admin.site.register(Purchased_Courses)