from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('Dashboard', views.Dashboard, name='Dashboard'),
    path('product', views.product, name='product'),
    path('categories', views.categories, name='categories')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)