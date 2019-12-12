from django.urls import path

from .views import course

urlpatterns=[
    #path('', course)
     path('course/', course)

]