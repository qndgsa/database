from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('ema/', views.ema, name='ema'),
    path('reward/', views.reward, name='reward'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)