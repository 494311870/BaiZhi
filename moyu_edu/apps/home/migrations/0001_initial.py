# Generated by Django 2.1 on 2020-11-05 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='标题')),
                ('link', models.CharField(max_length=300, verbose_name='链接')),
                ('is_show', models.BooleanField(default=False, verbose_name='是否展示')),
                ('orders', models.IntegerField(default=1, verbose_name='排序')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('img', models.ImageField(max_length=255, upload_to='banner/%Y/%m', verbose_name='轮播图')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
            },
        ),
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='标题')),
                ('link', models.CharField(max_length=300, verbose_name='链接')),
                ('is_show', models.BooleanField(default=False, verbose_name='是否展示')),
                ('orders', models.IntegerField(default=1, verbose_name='排序')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('position', models.IntegerField(choices=[(1, '顶部导航'), (2, '底部导航')], default=1, verbose_name='导航位置')),
                ('is_site', models.BooleanField(default=False, verbose_name='是否是外部链接')),
            ],
            options={
                'verbose_name': '导航栏',
                'verbose_name_plural': '导航栏',
            },
        ),
    ]
