from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include('product.urls')),
    path('api/v1/', include('order.urls'))
]

urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }), ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
