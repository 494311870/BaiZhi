from django.db import models

from home.baseModel import BaseModel


class Banner(BaseModel):
    """
    轮播图
    """
    img = models.ImageField(upload_to="banner/%Y/%m", max_length=255, verbose_name="轮播图")




    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Nav(BaseModel):
    """
    导航栏
    """
    POSITION_OPTION = (
        (1, "顶部导航"),
        (2, "底部导航"),
    )

    position = models.IntegerField(choices=POSITION_OPTION, default=1, verbose_name="导航位置")
    is_site = models.BooleanField(default=False, verbose_name="是否是外部链接")

    class Meta:
        verbose_name = "导航栏"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
