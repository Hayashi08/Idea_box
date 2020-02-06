from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('project/create/', views.CreateProject.as_view(), name='project_create'),

    path('project/delete/<pk>/', views.DeleteProject.as_view(), name='project_delete'),

    path('project/<pk>/', views.ProjectList.as_view(), name='project_list'),

    path('project/<pk>/bord/', views.CreateBoard.as_view(), name='board'),

    path('project/<pk>/conclusion/', views.conclusion, name='conclusion'),

    path('idea/form/<pk>/', views.post_idea, name='idea_form'),

    path('idea/detail/<pk>/', views.DetailIdea.as_view(), name='detail'),

    path('idea/update/<pk>/', views.UpdateIdea.as_view(), name='update'),

    path('idea/delete/<pk>/', views.DeleteIdea.as_view(), name='delete'),

]