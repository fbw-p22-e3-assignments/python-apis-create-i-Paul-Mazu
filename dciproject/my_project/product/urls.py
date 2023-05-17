from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProductApiListView.as_view(), name="api-list-view"),
    path("<int:pk>/", views.ProductApiDetailView.as_view(), name="api-detail-view"),
]
