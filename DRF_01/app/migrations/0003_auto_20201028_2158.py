# Generated by Django 3.1.2 on 2020-10-28 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='level',
            field=models.SmallIntegerField(choices=[(0, '暂未评级'), (1, '初级'), (2, '中级'), (3, '高级'), (4, '特级')], default=0, verbose_name='级别'),
        ),
    ]
