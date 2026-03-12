from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from commandes import views
from commandes.serializers import MyTokenObtainPairView
from django.views.generic import TemplateView
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('commandes.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('commandes/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
