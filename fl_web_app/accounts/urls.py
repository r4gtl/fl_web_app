from django.urls import path

from .views import registrazione_view

app_name="accounts"

urlpatterns = [
    path('registrazione/', registrazione_view, name='registration_view')
]