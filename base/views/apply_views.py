from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
# from .schools import schools
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from base.models import School,Application,ApplicationItem,StudentScores,Student
from base.serializers import SchoolSerializer,ApplicationItemSerializer,ApplicationSerializer,\
    StudentScoreSerializer,StudentScores
from rest_framework import status

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addApplicationItems(request):
    user = request.user
    data = request.data
    applicationItems = data['applicationItems']
    if applicationItems and len(applicationItems) == 0:
        return Response({'detail':'No schools selected'},status=status.HTTP_400_BAD_REQUEST)
    else:
        application = Application.objects.create(
            user = user,
            # username=data['studentPriDetails']['username'],
            studentScoreAverage = data['studentScoreAverage'],


            # studentScores = studentScores,
            # gender=data['gender'],
            # cutoff=data['cutoff']
        )
        student = Student.objects.create(
            user = user,
            application=application,
            username=data['studentPriDetails']['username'],
            index_number=data['studentPriDetails']['index_number'],
            sex=data['studentPriDetails']['sex'],
            DOB=data['studentPriDetails']['DOB'],
            school=data['studentPriDetails']['school']

        )
        studentScores = StudentScores.objects.create(
            application = application,
            # student = student,
            # studentScoreAverage = data['studentScoreAverage'],
            mathes=data['studentPriScores']['maths'],
            english=data['studentPriScores']['english'],
            kiswahili=data['studentPriScores']['kiswahili'],
            science=data['studentPriScores']['science'],
            socialStudies=data['studentPriScores']['socialStudies']


        )

        for i in applicationItems:
            school = School.objects.get(_id=i['school'])
            # student = Student.objects.get(_id=i['student'])
            item = ApplicationItem.objects.create(
                student=student.username,
                username=data['studentPriDetails']['username'],
                school=school,
                application=application,
                name=school.name,
                studentScoreAverage = data['studentScoreAverage'],
                numberOfChoice=i['numberOfChoice'],
                numberOfstudents=school.numberOfstudents,
                cutoff=school.cutoff,
                image = school.image.url,

            )
            school.numberOfstudents =item.numberOfstudents - 1
            school.save()
        serializer = ApplicationSerializer(application, many=False)
        return Response(serializer.data)






@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getApplicatioById(request,pk):
    user =request.user
    try:
        application = Application.objects.get(_id=pk)
        if user.is_staff or application.user == user:
            serializer = ApplicationSerializer(application, many=False)
            return Response(serializer.data)
        else:
            Response({'detail':'Not authorized to view this order'},status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({'detail':'application does not  exist'},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getApplicationItemById(request,pk):
    user =request.user
    try:
        application = ApplicationItem.objects.get(_id=pk)
        if user.is_staff or application.user == user:
            serializer = ApplicationItemSerializer(application, many=False)
            return Response(serializer.data)
        else:
            Response({'detail':'Not authorized to view this order'},status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({'detail':'application does not  exist'},status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAdminUser])
def successApplication(request):
    # user = request.user
    # applications = ApplicationItem.objects.all()
    # for application in application:application.numberOfChoice ==1
    if ApplicationItem.numberOfChoice == 1 and ApplicationItem.cutoff <= ApplicationItem.studentScoreAverage and ApplicationItem.numberOfstudents >=1:
        applications = ApplicationItem.objects.all()
        serializer = ApplicationItemSerializer(applications, many=True)
        return Response(serializer.data)
    elif ApplicationItem.numberOfChoice ==2 and ApplicationItem.cutoff <= ApplicationItem.studentScoreAverage and ApplicationItem.numberOfstudents >=1:
        applications = ApplicationItem.objects.all()
        serializer = ApplicationItemSerializer(applications, many=True)
        return Response(serializer.data)
    elif ApplicationItem.numberOfChoice ==3 and ApplicationItem.cutoff <= ApplicationItem.studentScoreAverage and ApplicationItem.numberOfstudents >=1:
        applications = ApplicationItem.objects.all()
        serializer = ApplicationItemSerializer(applications, many=True)
        return Response(serializer.data)
    else:
        return Response({'detail':' no school found for you'},status=status.HTTP_400_BAD_REQUEST)
    # return application;


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getApplications(request):
    # user =request.user
    applications= ApplicationItem.objects.filter(numberOfChoice=2)
    serializer = ApplicationItemSerializer(applications, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getTest(request):
    # user =request.user
    applications= ApplicationItem.objects.filter(numberOfChoice__g)
    serializer = ApplicationItemSerializer(applications, many=True)
    return Response(serializer.data)



