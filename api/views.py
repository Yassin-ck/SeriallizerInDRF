from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse

# Create your views here.


def student_details(request,pk):
    stu = Student.objects.get(id=pk)
    serilizer = StudentSerializer(stu)   
    # json_data = JSONRenderer().render(serilizer.data)  
    # return HttpResponse(json_data , content_type='application/json')
    return JsonResponse(serilizer.data)


def student_list(request):
    stu = Student.objects.all()
    serilizer = StudentSerializer(stu,many=True)   
    # json_data = JSONRenderer().render(serilizer.data)  
    # return HttpResponse(json_data , content_type='application/json')
    return JsonResponse(serilizer.data,safe=False)