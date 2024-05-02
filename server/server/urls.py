from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from schema_graph.views import Schema

schema_view = get_schema_view(
   openapi.Info(
      title="Delivery API",
      default_version='v1',
      description="Rest API for a Delivery service",
      contact=openapi.Contact(email="auspicious54321@gmail.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('schema/', Schema.as_view()),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('student/', include('Student.urls')),
    path('TA/', include('TA.urls')),
]
