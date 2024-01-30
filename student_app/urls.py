from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views


# app_name = "student_app"


urlpatterns = [
    path('', login_required(views.Index.as_view()) ,name='index'),
    path('<int:id>', login_required(views.View_student.as_view()) , name='view_student'),
    path('add/', login_required(views.Add.as_view()) , name='add'),
    path('edit/<int:id>/',login_required(views.Edit.as_view()), name='edit'),
    path('delete/<int:pk>/',login_required(views.Delete.as_view()) , name='delete'),
    
]
