from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list),
    path('view/<int:pk>', views.post_view,name='post_view'),
    path('edit/<int:pk>', views.post_update,name='post_edit'),
    path('delete/<int:pk>', views.post_delete,name='post_delete'),
    path('create/', views.post_create,name='post_create'),
]
