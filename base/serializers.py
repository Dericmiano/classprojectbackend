from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import School,Student,StudentScores,ApplicationItem,Application


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin']

    def get__id(self, obj):
        return obj.id

    def get_isAdmin(self, obj):
        return obj.is_staff

    def get_name(self, obj):
        name = obj.first_name
        if name == '':
            name = obj.email
        return name

class UserSerializerWithTokens(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class StudentScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentScores
        fields = '__all__'


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class ApplicationItemSerializer(serializers.ModelSerializer):


    class Meta:
        model = ApplicationItem
        fields = '__all__'




class ApplicationSerializer(serializers.ModelSerializer):
    applicationItems = serializers.SerializerMethodField(read_only=True)
    studentPriScores = serializers.SerializerMethodField(read_only=True)
    studentPriDetails = serializers.SerializerMethodField(read_only=True)
    user = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = Application
        fields = '__all__'
    def get_applicationItems(self, obj):
        items = obj.applicationitem_set.all()
        serializer = ApplicationItemSerializer(items,many=True)
        return serializer.data

    def get_studentPriDetails(self, obj):
        try:
            details = StudentSerializer(obj.student, many=False).data
        except:
            details = False
        return details
    # def get_applicationItems(self, obj):

    def get_studentPriScores(self, obj):
        try:
            score = StudentScoreSerializer(obj.studentscores, many=False).data
        except:
            score = False
        return score

    def get_user(self, obj):
        user = obj.user
        serializer = UserSerializer(user,many=False)
        return serializer.data


