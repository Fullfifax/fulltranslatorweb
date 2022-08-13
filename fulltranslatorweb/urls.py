from django.contrib import admin
from django.urls import path

from textTranslator.views import translate_text

urlpatterns = [
    path('admin/', admin.site.urls),
    path('translate/', translate_text, name='trans'),
]
