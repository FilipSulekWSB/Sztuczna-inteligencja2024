from django.conf import settings
from django.conf.urls.static import static

+ static(settings.MEDIA.URL, document_root=settings.MEDIA_ROOT)