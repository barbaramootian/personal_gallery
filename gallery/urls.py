from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
  # adding dynamic ur
urlpatterns=[
    path('',views.index,name = 'welcome'),
    path('search',views.search_results, name='search'),
    path('location/<int:id>/',views.area_results,name='area')

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)