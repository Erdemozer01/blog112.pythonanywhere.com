from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path("", include("apps.authentication.urls")),

                  # ADD NEW Routes HERE
                  path('ckeditor/', include('ckeditor_uploader.urls')),
                  # Leave `Home.Urls` as last the last line
                  path("", include("apps.home.urls"))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
