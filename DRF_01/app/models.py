from django.db import models


# Create your models here.
class User(models.Model):
    gender_choices = (
        (0, "男"),
        (1, "女"),
        (2, "保密"),
    )

    username = models.CharField(max_length=80)
    password = models.CharField(max_length=80)
    gender = models.SmallIntegerField(choices=gender_choices, default=0)

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
