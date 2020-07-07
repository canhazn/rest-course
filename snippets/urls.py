from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.snippets_list),
    path('<int:pk>/', views.snippets_detail)
]
