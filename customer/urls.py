"""customer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from customer.api.views import CustomerView

schema_view = get_schema_view(
   openapi.Info(
      title="Oowlish Customers",
      default_version='v1',
      description="List of the customers",
      contact=openapi.Contact(email="heitoranjos96@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/<int:page>', CustomerView.as_view({'get': 'list'})),
    path('customer/<int:id>', CustomerView.as_view({'get': 'retrieve'})),
    path('documentation/', schema_view.with_ui('swagger', cache_timeout=0))
]
