from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.main, name = 'mainpage'),
    path(r'index/', views.index, name = 'indexpage'),
    path('createpost/',views.createpost, name='createpost'),
    path('update/<int:post_id>',views.update_post, name='updatepost'),
    path('delete/<int:post_id>',views.delete_post, name='deletepost'),
    # path('profile/', views.profile, name='profile')
    path('accounts/profile/',views.profile,name = 'profile'),
    path(r'update_profile', views.update_profile, name='update'),
]