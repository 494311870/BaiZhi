import requests
from django_redis import get_redis_connection


class Message(object):

    def __init__(self, api_key):
        # 账号的唯一标识
        self.api_key = api_key
        # 单条发送短信的接口
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_message(self, phone, code):
        """
        短信发送的实现
        手机号
        验证码
        """
        params = {
            "apikey": self.api_key,
            "mobile": phone,
            "text": f"【毛信宇test】您的验证码是{code}。如非本人操作，请忽略本短信"
        }

        req = requests.post(self.single_send_url, data=params)
        print(req)

    @staticmethod
    def validate_code(phone, sms_code):
        with get_redis_connection("sms_code") as redis_connection:
            mobile_code = redis_connection.get(f"mobile_{phone}")
            if mobile_code.decode() != sms_code:
                # 代表验证码有误
                # 为了防止暴力破解  可以设置一个手机号只能验证n次  累加
                return False

            # 验证通过后将redis的验证码的删除
            redis_connection.delete(f"mobile_{phone}")
            return True
