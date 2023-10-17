from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from accounts.models import CustomUser


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Категория')

    def __str__(self):
        return f'{self.title}'


class Course(models.Model):
    title = models.CharField(max_length=150)
    tutor = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Преподаватель',
        related_name='tutor_courses'
    )
    students = models.ManyToManyField(
        CustomUser,
        verbose_name='Студенты',
        related_name='students_courses'
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')
    price = models.PositiveIntegerField(default=0, verbose_name='Стоимость курса')


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)


class Content(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='contents')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='contents')
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')


class ItemBase(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='%(class)s_related')
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class File(ItemBase):
    file = models.FileField(upload_to='files')


class Image(ItemBase):
    file = models.ImageField(upload_to='images')


class Video(ItemBase):
    url = models.URLField()
