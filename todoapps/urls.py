from django.urls import path
from . import views
urlpatterns = [
    path('create-todo/',views.CreateRetrieveView.as_view()),
    path('get-all-todo/',views.CreateRetrieveView.as_view()),
    path('get-todo/<str:id>/',views.GetUpdateDeleteView.as_view()),
    path('update-todo/<str:id>/',views.GetUpdateDeleteView.as_view()),
    path('delete-todo/<str:id>/',views.GetUpdateDeleteView.as_view()),
]
