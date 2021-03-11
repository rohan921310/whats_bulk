from django.urls import path
from .views import send_view

urlpatterns = [
    path("message",send_view,name="send"),
]