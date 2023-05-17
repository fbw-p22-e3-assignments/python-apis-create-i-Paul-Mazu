from django.contrib import admin
from django.urls import path, include  # new
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("customer/", include("customer.urls")),  # new
    path("product/", include("product.urls")),  # new
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
