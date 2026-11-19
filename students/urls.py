from django.urls import path
from .views import home, fatou_list, fatou_detail, fatou_by_class, teacher_list, about

urlpatterns = [
    path('', home, name='home'),
    path('student/', fatou_list, name='fatou_list'),
    path('student/<int:id>/', fatou_detail, name='fatou_detail'),
    path('student/classe/<str:classe>/', fatou_by_class, name='fatou_by_class'),
    path('teachers/', teacher_list, name='teacher_list'),
    path('about/', about, name='about'),
]