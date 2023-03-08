from django.urls import path
from public_screenshots import views

urlpatterns = [
    path('public-scrshot/', views.PublicScreenshotList.as_view()),
]