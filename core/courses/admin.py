from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Module)
admin.site.register(Content)
admin.site.register(File)
admin.site.register(Image)
admin.site.register(Review)
admin.site.register(StudentsCourses)


