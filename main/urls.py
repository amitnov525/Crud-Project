from django.urls import path
from main import views

urlpatterns = [
    path('',views.base),
    path('add',views.add,name="add"),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('update/<int:id>',views.update,name="update")
]
