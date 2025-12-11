from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.core.urls')),
    
    # Esta linha carrega o seu arquivo HTML na página inicial
    path('', TemplateView.as_view(template_name='interface_kanban.html')),
]