from django.urls import path
from . import views

urlpatterns = [
    path("me/", views.GetProfileAPIView.as_view(), name="get_profile"),
    path(
        "me/<str:username>", views.UpdateProfileAPIView.as_view(), name="update_profile"
    ),
    path("agents/all/", views.AgentListAPIView.as_view(), name="all_agents"),
    path("agents/top/", views.TopAgentListAPIView.as_view(), name="top_agents"),
]
