from django.urls import path
from .views import SendWelcomeEmailView

urlpatterns = [
    path('send-welcome-email/', SendWelcomeEmailView.as_view(), name='send-welcome-email'),
]