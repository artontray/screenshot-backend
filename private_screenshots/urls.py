from django.urls import path
from private_screenshots import views

urlpatterns = [
    path('private-scrshot/', views.PrivateScreenshotList.as_view()),
    path('private-scrshot/<int:pk>/', views.PrivateScreenshotDetail.as_view()),
]