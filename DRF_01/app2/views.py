from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from app2.models import Book
from app2.serializers import BookModelSerializer


class BookAPIView(APIView):

    def get(self, request, *args, **kwargs):

        book_id = kwargs.get("id")

        if book_id:
            book = Book.objects.get(pk=book_id)

            return Response({
                "status": 200,
                "message": "查询单个图书成功",
                "results": BookModelSerializer(book).data,
            })

        else:
            books = Book.objects.all()

            return Response({
                "status": 200,
                "message": "查询单个图书成功",
                "results": BookModelSerializer(books, many=True).data,
            })

    def post(self, request, *args, **kwargs):
        """
        增加单个: 传递参数是字典
        增加多个: [{},{},{}] 列表中嵌套是一个个的图书对象
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        print(request.data)
        many = False
        if isinstance(request.data, dict):  # 代表添加的单个对象
            many = False
        elif isinstance(request.data, list):  # 代表添加的是多个对象
            many = True
        else:
            return Response({
                "status": 400,
                "message": "参数格式有误",
            })

        serializer = BookModelSerializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        book = serializer.save()

        return Response({
            "status": 200,
            "message": "添加图书成功",
            "results": BookModelSerializer(book, many=many).data,
        })

    def delete(self, request, *args, **kwargs):
        """
        删除单个  删除多个
        单个删除: 通过url传递单个删除的id
        多个删除: 有多个id {ids:[1,2,3]}
        :return:
        """
        book_id = kwargs.get("id")

        if book_id:
            # 删除单个
            ids = [book_id]
        else:
            # 删除多个
            ids = request.data.get("ids")
        # 逻辑删除
        response = Book.objects.filter(pk__in=ids, is_delete=False).update(is_delete=True)
        print(response)
        if response:
            return Response({
                "status": 200,
                "message": '删除成功'
            })
        else:
            return Response({
                "status": 400,
                "message": '删除失败或者图书存在'
            })

    def put(self, request, *args, **kwargs, ):
        """
        整体修改单个:  修改一个对象的全部字段
        修改对象时,在调用序列化器验证数据时必须指定instance关键字
        在调用serializer.save() 底层是通过ModelSerializer内部的update()方法来完成的更新
        """
        # 获取要修改的图书的id
        book_id = kwargs.get("id")
        # 论 ?? 的好用之处
        # partial = kwargs.get("partial") if kwargs.get("partial") else False
        try:
            book_obj = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return Response({
                "status": 400,
                "message": '图书不存在'
            })

        # 更新的时候需要对前端传递的数据进行安全校验
        # 更新的时候需要指定关键字参数data
        # 如果是修改  需要自定关键字参数instance  指定你要修改的实例对象是哪一个
        serializer = BookModelSerializer(data=request.data, instance=book_obj)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "status": 200,
            "message": '修改成功',
            "results": BookModelSerializer(book_obj).data
        })

    def patch(self, request, *args, **kwargs):
        # 获取要修改的图书的id
        book_id = kwargs.get("id")
        # 论 ?? 的好用之处
        # partial = kwargs.get("partial") if kwargs.get("partial") else False
        try:
            book_obj = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return Response({
                "status": 400,
                "message": '图书不存在'
            })

        # 更新的时候需要对前端传递的数据进行安全校验
        # 更新的时候需要指定关键字参数data
        serializer = BookModelSerializer(data=request.data, instance=book_obj, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "status": 200,
            "message": '修改成功',
            "results": BookModelSerializer(book_obj).data
        })


class BookGenericAPIView(GenericAPIView,
                         mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.DestroyModelMixin,
                         mixins.CreateModelMixin,
                         mixins.UpdateModelMixin):
    queryset = Book.objects.filter()
    serializer_class = BookModelSerializer
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        if "id" in kwargs:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class BookViewSetView(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    lookup_field = "id"

    def user_login(self, request, *args, **kwargs):
        # 模拟登陆
        print("登录成功")
        return Response("登录成功")

    def get_user(self, request, *args, **kwargs):
        # 模拟查询
        print("查询成功1")
        return Response("查询成功1")

