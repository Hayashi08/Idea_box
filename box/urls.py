from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('project/create/', views.CreateProject.as_view(), name='project_create'),

    path('project/detail/<pk>/', views.DetailProject.as_view(), name='project_detail'),

    path('project/delete/<pk>/', views.DeleteProject.as_view(), name='project_delete'),

    path('project/update/<pk>/', views.UpdateProject.as_view(), name='project_update'),

    path('project/<pk>/', views.ProjectList.as_view(), name='project_list'),

    path('project/<pk>/bord/', views.CreateBoard.as_view(), name='board'),

    path('conclusion/form/<pk>', views.conclusion, name='conc_form'),

    path('conclusion/detail/<pk>', views.DetailConclusion.as_view(), name='conc_detail'),

    path('conclusion/update/<pk>', views.UpdateConclusion.as_view(), name='conc_update'),

    path('conclusion/delete/<pk>', views.DeleteConclusion.as_view(), name='conc_delete'),

    path('idea/form/<pk>/', views.post_idea, name='idea_form'),

    path('idea/detail/<pk>/', views.DetailIdea.as_view(), name='idea_detail'),

    path('idea/update/<pk>/', views.UpdateIdea.as_view(), name='idea_update'),

    path('idea/delete/confirm/<pk>/', views.delete_confirm_idea, name='idea_delete_confirm'),

    path('idea/delete/complete/<pk>/', views.delete_idea, name='idea_delete'),

]