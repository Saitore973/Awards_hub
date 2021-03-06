from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('search', views.search_results, name='search_results'),
    re_path(r'^project/(\d+)',views.project,name ='project'),
    path('create/', views.create, name='create'),
    path('rate/', views.rate, name='rate'),
    path('profile/<int:id>/', views.profile, name="profile"),
    path('edit/<int:id>/', views.edit, name="edit"),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
