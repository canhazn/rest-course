from django.urls import path
from . import views

urlpatterns = [
    path('snippets/list/', views.SnippetsList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('users/list/', views.UserList.as_view()),
    path('users/<int:pk>/', views.USerDetail.as_view())
]
