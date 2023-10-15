from django.db import models
from django.contrib.auth.models import AbstractUser

from django.utils import timezone


class CustomUser(AbstractUser):
    """"""

    without_breaks = models.PositiveIntegerField(default=0, verbose_name='Дней без перерыва')
    max_without_breaks = models.PositiveIntegerField(default=0, verbose_name='Максимум дней без перерыва')
    problems_complete = models.PositiveIntegerField(default=0, verbose_name='Задач решено')
    last_problem_completion_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return  f'Пользователь {self.username}'

    def update_days_without_breaks(self):
        last_problem_completion_date = self.last_problem_completion_date
        today = timezone.now().date()

        if last_problem_completion_date is not None:
            if last_problem_completion_date == today - timezone.timedelta(days=1):
                self.without_breaks += 1
                if self.without_breaks > self.max_without_breaks:
                    self.max_without_breaks = self.without_breaks
            elif last_problem_completion_date < today - timezone.timedelta(days=1):
                self.without_breaks = 0

            self.save()

    def complete_problem(self):
        self.problems_complete += 1
        self.update_days_without_breaks()
        self.save()

