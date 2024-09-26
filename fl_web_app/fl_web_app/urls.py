
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from core.views import SchedaLavorazioneListView



urlpatterns = [    
    path('core/', include('core.urls')),    
    path("admin/", admin.site.urls),
    path("accounts/", include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', SchedaLavorazioneListView.as_view(), name='home'),  # Homepage
    #path("__debug__/", include("debug_toolbar.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)