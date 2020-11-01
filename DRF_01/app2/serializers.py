from rest_framework import serializers, exceptions

from app2.models import Book, Press


class PressModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Press
        fields = ("name", "pic", "address",)


class BookListSerializer(serializers.ListSerializer):
    """
    使用此序列化器完成更新多个对象
    """

    # 重写update方法完成更新
    def update(self, instance, validated_data):
        print(self.child)  # 调用逻辑的序列化器类-->BookModelSerializer
        for i, v in zip(instance, validated_data):
            self.child.update(i, v)

        return instance


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("name", "price", "publish", "authors", "pic", "author_list")

        list_serializer_class = BookListSerializer

        extra_kwargs = {
            "name": {
                "required": True,  # 必填字段
                "min_length": 1,  # 最小长度
            },
            # 指定某个字段只参与序列化
            "pic": {
                "read_only": True
            },
            "author_list": {
                "read_only": True
            },
            # 指定某个字段只参与反序列化
            "publish": {
                "write_only": True
            },
            "authors": {
                "write_only": True
            },
        }

    def validate(self, attrs):
        # if Book.objects.filter(name=attrs.get("name"), publish=attrs.get("publish"),
        #                        authors__in=[i.id for i in attrs.get("authors")]).first():
        #     raise exceptions.ValidationError("书籍已存在")
        return attrs

    def validate_name(self, obj):
        print(obj)
        return obj
