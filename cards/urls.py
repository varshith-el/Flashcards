from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path(
        "",
        views.CardListView.as_view(),
        name="card-list"
    ),
    path(
        "new",views.cardCreateView.as_view(),
    name = 'card-create'
    ),
    path(
        "edit/<int:pk>",
        views.cardUpdateView.as_view(),
        name="card-update"
    ),
]

