from django.urls import path

from . import views

urlpatterns = [
    path(
        "all/",
        views.ListAllPropertiesAPIView.as_view(),
        name="all-properties",
    ),
    path(
        "agents/",
        views.ListAgentsPropertiesAPIView.as_view(),
        name="agent-properties",
    ),
    path(
        "create/",
        views.create_property_api_view,
        name="property-create",
    ),
    path(
        "detail/<slug:slug>",
        views.PropertyDetailView.as_view(),
        name="property-detail",
    ),
    path(
        "update/<slug:slug>",
        views.update_property_api_view,
        name="property-update",
    ),
    path(
        "delete/<slug:slug>",
        views.delete_property_api_view,
        name="property-delete",
    ),
    path(
        "search/",
        views.PropertySearchAPIView.as_view(),
        name="property-search",
    ),
]
