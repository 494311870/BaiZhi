from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt, csrf_protect
#
from rest_framework.response import Response
from rest_framework.views import APIView
#
from app.models import User, Teacher
from app.serializers import TeacherSerializer, TeacherDeSerializer

@method_decorator(csrf_exempt, name="dispatch")  # 为类视图免除csrf认证
class UserView(View):

    def get(self, request, *args, **kwargs):
        """
        提供查询单个用户以及  多个用户的接口
        :param request:  请求对象
        :param args:
        :param kwargs:
        :return: 返回查询结果
        """
        print("get")
        user_id = kwargs.get("id")
        print(user_id)
        if user_id:
            user = User.objects.filter(id=user_id).values("username", "password", "gender").first()
            print(type(user))
            print(user)
            if user:
                # 如果查询出用户的信息, 则返回到前端
                return JsonResponse({
                    "status": 200,
                    "message": "查询单个用户成功",
                    "results": user
                })

        else:
            # 不输入id 则代表查询所有用户信息
            user_objects_all = User.objects.all().values("username", "password", "gender")
            if user_objects_all:
                return JsonResponse({
                    "status": 200,
                    "message:": "查询所有用户成功",
                    "results": list(user_objects_all)
                })

        return JsonResponse({
            "status": 400,
            "message": "查询用户失败",
        })

    def post(self, request, *args, **kwargs):
        """
        新增单个用户
        """
        print("post")

        username = request.POST.get("username")
        password = request.POST.get("password")
        gender = request.POST.get("gender")
        print(username)
        print(password)
        print(gender)

        try:
            user_obj = User.objects.create(username=username, password=password, gender=gender)
            print(user_obj.get_gender_display())
            return JsonResponse({
                "status": 200,
                "message": "新增单个用户成功",
                "results": {"username": user_obj.username, "gender": user_obj.gender}
            })
        except:
            return JsonResponse({
                "status": 400,
                "message": "新增失败",
            })

    def put(self, request, *args, **kwargs):
        print("put")
        return HttpResponse("put OK")

    def delete(self, request, *args, **kwargs):
        print("delete")
        return HttpResponse("delete OK")


class StudentAPIView(APIView):

    def get(self, request, *args, **kwargs):
        print("DRF GET VIEW")
        return Response("DRF GET OK")

    def post(self, request, *args, **kwargs):
        print("POST GET VIEW")
        return Response("DRF POST OK")


class TeacherAPIView(APIView):

    def get(self, request, *args, **kwargs):
        print("DRF GET VIEW")
        id = kwargs.get("id")
        if id:
            teacher = Teacher.objects.filter(id=id).first()
            if teacher:
                teacher = TeacherSerializer(teacher).data
                return Response({
                    "status": 200,
                    "message": "查询单个教师成功",
                    "results": teacher
                })
        else:
            teachers = TeacherSerializer(Teacher.objects.all(),many=True).data
            return Response({
                "status": 200,
                "message": "查询所有教师成功",
                "results": teachers
            })

        return JsonResponse({
            "status": 400,
            "message": "查询教师失败",
        })

    def post(self, request, *args, **kwargs):
        print("POST GET VIEW")
        request_data = request.data
        if not isinstance(request_data, dict) or request_data == {}:
            return Response({
                "status": 400,
                "message": "参数有误",
            })
        teacher = TeacherDeSerializer(data=request_data)
        if teacher.is_valid():
            res = teacher.save()
            print(res)
            return Response({
                "status": 200,
                "message": "教师添加成功",
                "results": TeacherSerializer(res).data
            })

        else:
            return Response({
                "status": 400,
                "message": "教师添加失败",
                "results": teacher.errors
            })
