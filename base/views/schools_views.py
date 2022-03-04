from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
# from .schools import schools
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from base.models import School
from base.serializers import SchoolSerializer, UserSerializer, UserSerializerWithTokens
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from rest_framework import status

@api_view(['GET'])
def getSchools(request):
    schools = School.objects.all()
    serializer = SchoolSerializer(schools,many=True)
    return Response(serializer.data)




@api_view(['GET'])
def getSchool(request, pk):
    school = School.objects.get(_id=pk)
    serializer = SchoolSerializer(school,many=False)

    return Response(serializer.data)

@api_view(['GET'])
def getChoiceSchools(request):
    schools = School.objects.all()
    serializer = SchoolSerializer(schools,many=True)
    return Response(serializer.data)




@api_view(['GET'])
def getChoiceSchool(request, pk):
    school = School.objects.get(_id=pk)
    serializer = SchoolSerializer(school,many=False)

    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteSchool(request, pk):
    school = School.objects.get(_id=pk)
    school.delete()

    return Response('school deleted')

@api_view(['POST'])
@permission_classes([IsAdminUser])
def createSchool(request):
    user = request.user

    school = School.objects.create(
        user=user,
        name='school Name',
        cutoff=0,
        # numberOfChoice=0,
        numberOfstudents=0,
        motto='Sample motto',
        level='Sample level',
        location='Sample location',
        status='Sample status',

    )

    serializer = SchoolSerializer(school, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateSchool(request, pk):
    data = request.data
    school = School.objects.get(_id=pk)
    school.name = data['name']
    school.cutoff = data['cutoff']
    # school.numberOfChoice = data['numberOfChoice']
    school.numberOfstudents = data['numberOfstudents']
    school.motto = data['motto']
    school.level = data['level']
    school.location = data['location']
    school.status = data['status']


    school.save()
    serializer = SchoolSerializer(school, many=False)
    return Response(serializer.data)

@api_view(['POST'])
# @permission_classes([IsAdminUser])
def uploadImage(request):
    data = request.data

    school_id = data['school_id']
    school =School.objects.get(_id=school_id)

    school.image = request.FILES.get('image')
    school.save()

    return Response('Image was uploaded')
