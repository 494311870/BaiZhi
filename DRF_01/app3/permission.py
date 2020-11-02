from rest_framework.permissions import BasePermission

from app3.models import User


class MyPermission(BasePermission):
    """
    登陆 可写
    游客 只读
    有权限返回True
    无权限返回False
    """

    def has_permission(self, request, view):
        # 如果是只读 则所有人都可以访问
        if request.method in ("GET", "HEAD", "OPTIONS"):
            return True
        username = request.data.get("username")
        print(username)

        # 如果用户访问的是写操作 判断用户是否有登陆信息
        user = User.objects.filter(username=username).first()
        print(user)
        if user:
            return True

        return False
