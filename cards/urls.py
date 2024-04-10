# cards/urls.py
from typing import List, Any

from django.urls import path
# Removed: from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", views.welcome_page_view, name="welcome'"),
    path('existing-cards/', views.existing_cards_view, name='existing_cards'),
    path('create-cards/', views.create_cards_view, name='create_cards'),
]
