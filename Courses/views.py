from django.shortcuts import render

from .models import Courses #name of the app

def course(request): #name of the function that is in urls
    if request.method=="POST":
        c_code=request.POST['course_code']
        c_title=request.POST['course_title']
        c_credit=request.POST['course_credit']

        # this will set elective to True, only if the value of

        # 'elective' passed in the POST is on "on means the checkbox is checked"

        ele = request.POST.get('elective', '') == 'on'

        obj=Courses.objects.create(course_code=c_code,

        course_title=c_title,

        course_credit=c_credit, elective=ele)

        obj.save()

        getcor=Courses.objects.all()

        msg="this is a Post request"

        context={

        'courses':getcor,

        }

        return render(request, "courses/courses.html", context)

    else:
        #this code get all the soruese
        getcor= Courses.objects.all()
        msg="this is a Post request"
        context={
        'courses':getcor,
        }
        return render(request, "courses/courses.html", context) ###### corrected

        #goes to file couses in templates an then takes courses.html

