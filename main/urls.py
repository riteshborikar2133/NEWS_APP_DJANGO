from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.home,name='home'),
    path('news/',views.allnews,name='news'),
    path('new/<int:id>',views.onenews,name='new'),
    path('catnews/<int:id>',views.cnews,name='catnews')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)