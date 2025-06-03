from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('signup', views.signup, name='signup'),
    path('addcart', views.addcart, name='addcart'),
    path('searcht', views.searcht, name='searcht'),
    path('editadmin', views.editadmin, name='editadmin'),
    path('search', views.search, name='search'),
    path('removecart/<int:id>', views.removecart, name='removecart')
]
