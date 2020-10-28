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


class Teacher(models.Model):
    gender_choices = (
        (0, "保密"),
        (1, "男"),
        (2, "女"),
    )
    level_choices = (
        (0, "暂未评级"),
        (1, "初级"),
        (2, "中级"),
        (3, "高级"),
        (4, "特级"),
    )

    name = models.CharField(max_length=10, null=False, verbose_name='姓名')
    gender = models.SmallIntegerField(choices=gender_choices, default=0, verbose_name='性别')
    level = models.SmallIntegerField(choices=level_choices, default=0, verbose_name='级别')
    image = models.ImageField(upload_to='teacher/%Y/%m', verbose_name='头像', null=True)

    class Meta:
        verbose_name = "教师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.name}[{self.level}]'
