from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from user.models import UserInfo
from utils.send_msg import Message


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        "token": token,
        "user": user.username,
        "user_id": user.id
    }


def get_user_by_account(account):
    """根据条件获取用户"""
    try:
        user = UserInfo.objects.filter(Q(username=account) | Q(email=account) | Q(phone=account)).first()
    except UserInfo.DoesNotExist:
        return None
    else:
        return user


class UserAuthBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        根据账号来获取用户登陆方式   手机号  邮箱  用户名
        :return:  查询出的用户
        """
        user = get_user_by_account(username)

        if user:
            if password[:6] == "phone:":
                # 短信验证
                if (Message.validate_code(username, password[6:])) and user.is_authenticated:
                    return user

            if user.check_password(password) and user.is_authenticated:
                return user

        return None
