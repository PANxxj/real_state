
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('apps.users.urls')),
    path('api/',include('apps.profiles.urls')),
    path('api/',include('apps.common.urls')),
    path('api/',include('apps.ratings.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

admin.site.site_header='Real Estate Admin'
admin.site.site_title='Real Estate Admin Portal'
admin.site.index_title='welcome to real estate adminstration'
