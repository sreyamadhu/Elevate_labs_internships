from django.urls import path
from . import views

urlpatterns = [
    path('track/<int:user_id>/', views.track),  # ✅ use 'track' not 'track_click'
    path('fake-login/', views.fake_login),
    path('capture/', views.capture_input),
    path('analytics/', views.plot_events, name='analytics'),
]
