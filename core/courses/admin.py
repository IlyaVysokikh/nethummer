from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Module)
admin.site.register(Lesson)
admin.site.register(ImageContent)
admin.site.register(TextContent)
admin.site.register(VideoContent)
admin.site.register(Review)
admin.site.register(StudentsCourses)


