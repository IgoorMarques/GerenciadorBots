from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# Configuração do Swagger
schema_view = get_schema_view(
   openapi.Info(
      title="Minha API",
      default_version='v1',
      description="Descrição da API",
      terms_of_service="https://www.meusite.com/policies/terms/",
      contact=openapi.Contact(email="contato@meusite.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', admin.site.urls),
    path('api/', include('web_api.urls')),  # Substitua 'nome_do_app' pelo nome do seu app

    # URLs do Swagger
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

