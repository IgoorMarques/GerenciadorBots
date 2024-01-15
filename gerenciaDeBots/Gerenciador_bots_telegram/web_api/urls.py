from django.urls import path
from .views import GenericMessageApiView

urlpatterns = [
    path('hello/', GenericMessageApiView.as_view()),
]
