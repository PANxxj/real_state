from .views import *
from django.urls import path

urlpatterns=[
    path('me',GetProfile.as_view()),
    path("update",UpdateProfile.as_view()),
    path("agent/all",AgentListView.as_view()),
    path("top-agent/all",TopAgentListView.as_view())
]