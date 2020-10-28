from rest_framework import serializers
from app.models import Teacher


class TeacherSerializer(serializers.Serializer):
    name = serializers.CharField()
    gender = serializers.SerializerMethodField()
    level = serializers.SerializerMethodField()
    image = serializers.ImageField()

    # 自定义字段
    def get_gender(self, obj):
        return obj.get_gender_display()

    def get_level(self, obj):
        return obj.get_level_display()


class TeacherDeSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=1)
    gender = serializers.IntegerField(min_value=0, max_value=2)
    level = serializers.IntegerField(min_value=0, max_value=4)
    image = serializers.ImageField(allow_empty_file=False)

    # 如果想要完成对象的新增 必须重写create方法
    # self是序列化器对象  validated_data需要保存的数据
    def create(self, validated_data):
        print(validated_data)
        return Teacher.objects.create(**validated_data)
