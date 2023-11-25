from django.db import models

from accounts.models import CustomUser


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Категория')

    def __str__(self):
        return f'{self.title}'


class Course(models.Model):
    lang = (
        ('en', 'Английский'),
        ('ru', 'Русский'),
    )
    title = models.CharField(max_length=150)
    tutor = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Преподаватель',
        related_name='tutor_courses'
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')
    price = models.PositiveIntegerField(default=0, verbose_name='Стоимость курса')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    requirements = models.TextField(blank=True, null=True, verbose_name='Требования')
    is_active = models.BooleanField(default=False, verbose_name='Открыть курс')
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0, verbose_name='Рейтинг')
    language = models.CharField(max_length=2, choices=lang, verbose_name='Язык обучения')

    def __str__(self):
        return f'Курс {self.title}. Преподаватель {self.tutor}'

    def get_students_count(self):
        return self.students.count()

    def update_rating(self):
        # Обновление рейтинга курса на основе отзывов
        reviews = Review.objects.filter(course=self)
        if reviews.exists():
            sum_rating = sum([reviews.rating for review in reviews])
            avg_rating = sum_rating / len(reviews)
            self.rating = avg_rating
            self.save()


class StudentsCourses(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='Студент')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='Курс')

    def __str__(self):
        return f'Пользователь {self.student.username} записан на {self.course.title}'


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)


class Lesson(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=150)


class TextContent(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='text_contents')
    text = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Текстовый контент'
        verbose_name_plural = 'Текстовый контент'


class VideoContent(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='video_contents')
    video_url = models.URLField(blank=True, null=True, verbose_name='Ссылка на видео')

    class Meta:
        verbose_name = 'Видеоконтент'
        verbose_name_plural = 'Видеоконтент'


class ImageContent(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='image_contents')
    image = models.ImageField(upload_to='media/lessons_images/')


class Review(models.Model):
    """Модель отзыва о курсе"""
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='review')
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='student')
    text = models.TextField(blank=True, null=True, verbose_name='Текст отзыва')
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)], verbose_name='Оценка')


    def __str__(self):
        return f'Отзыв на курс {self.course.title} пользователя {self.student.username}'