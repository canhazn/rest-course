from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.SnippetsList.as_view()),
    path('<int:pk>/', views.SnippetDetail.as_view())
]
