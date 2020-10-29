from django.db import models


# Create your models here.

class BaseModel(models.Model):
    is_delete = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        # 原元数据中声明此字段后  不会再数据库为此表创建对应的表结构
        # 其他模型在继承此模型后,可以继承表中的字段
        abstract = True


class Book(BaseModel):
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    pic = models.ImageField(upload_to="book/%Y/%m", default="book/default.jpg")
    publish = models.ForeignKey(to="Press", on_delete=models.CASCADE, db_constraint=False,
                                related_name="books")
    authors = models.ManyToManyField(to="Author", db_constraint=False, related_name="books")

    class Meta:
        verbose_name = "图书"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    # 自定义序列化属性
    @property
    def press_name(self):
        return self.publish.press_name

    @property
    def author_list(self):
        return self.authors.values("name", "age", "detail__phone")


class Press(BaseModel):
    name = models.CharField(max_length=128)
    pic = models.ImageField(upload_to="press/%Y/%m", default="press/1.jpg")
    address = models.CharField(max_length=256)

    class Meta:
        verbose_name = "出版社"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Author(BaseModel):
    name = models.CharField(max_length=128)
    age = models.IntegerField()

    class Meta:
        verbose_name = "作者"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class AuthorDetail(BaseModel):
    phone = models.CharField(max_length=11)
    author = models.OneToOneField(to="Author", on_delete=models.CASCADE, related_name="detail")

    class Meta:
        verbose_name = "作者详情"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.author.name}的详情"


