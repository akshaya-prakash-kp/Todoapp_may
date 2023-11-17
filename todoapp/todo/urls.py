from django.urls import path
from.views import TaskCreate,RegisterPage,CustomLoginView, TaskDetailView,TaskList,TaskDelete,TaskUpdate
from django.contrib.auth.views import LogoutView
urlpatterns =[
    path('taskcreate',TaskCreate.as_view(),name='createtask'),
    path('register/',RegisterPage.as_view(),name='register'),
    path('',CustomLoginView.as_view(),name='login'),
    path('lists/',TaskList.as_view(),name='task'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('task-details/<int:pk>',TaskDetailView.as_view(),name='task_details'),
    path('task-updates/<int:pk>',TaskUpdate.as_view(),name='task_updates'),
    path('task-delete/<int:pk>',TaskDelete.as_view(),name='task_delete'),


    

]