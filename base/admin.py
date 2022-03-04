from django.contrib import admin
from .models import School,Application,ApplicationItem,StudentScores,Student




admin.site.register(School)
admin.site.register(StudentScores)
admin.site.register(Application)
admin.site.register(ApplicationItem)
admin.site.register(Student)
