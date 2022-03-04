from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
# from bas].schools import schools
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from base.models import School,Student,StudentScores
from base.serializers import SchoolSerializer, UserSerializer, UserSerializerWithTokens,\
    StudentSerializer,StudentScoreSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from rest_framework import status


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserSerializerWithTokens(self.user).data

        for k,v in serializer.items():
            data[k] = v


        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def registerUser(request):
    data = request.data
    # print('DATA',data)
    try:
        user = User.objects.create(
            first_name=data['name'],
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])
        )
        serializer = UserSerializerWithTokens(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'user with this email already exist'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUserProfile(request):
    user = request.user
    serializer = UserSerializerWithTokens(user, many=False)
    data = request.data
    user.first_name = data['name']
    user.username = data['email']
    user.email = data['email']

    if data['password'] != '':
        user.password = make_password(data['password'])

    user.save()

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users,many=True)
    return Response(serializer.data)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def students(request):
    data = request.data
    try:
        student = Student.objects.create(
            username=data['username'],
            index_number=data['index_number'],
            sex=data['sex'],
            school=data['school'],
            DOB=data['DOB']

        )
        serializer = StudentSerializer(student, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'user with this index_number already exist'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def studentScores(request):
    data = request.data
    try:
        studentScores = StudentScores.objects.create(
            averageScore=data['averageScore'],
            mathes=data['mathes'],
            english=data['english'],
            kiswahili=data['kiswahili'],
            science=data['science'],
            socialStudies=data['socialStudies']
        )
        serializer = StudentScoreSerializer(studentScores, many=False)
        return Response(serializer.data)
    except:
        messsage = {'detail':'user with this scores exist'}
        return Response(messsage,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUserById(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    data = request.data

    user.first_name = data['name']
    user.username = data['email']
    user.email = data['email']
    user.is_staff = data['isAdmin']

    user.save()

    serializer = UserSerializer(user, many=False)

    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteUser(request, pk):
    userForDeletion = User.objects.get(id=pk)
    userForDeletion.delete()
    return Response("user was deleted")


