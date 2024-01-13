from django.shortcuts import render
from django.urls import reverse_lazy
# Create your views here.


from django.views.generic import (
    ListView,
    CreateView,
    UpdateView
)
from .models import Card

class CardListView(ListView):
    model = Card
    queryset = Card.objects.all().order_by("box", "-date_created")


class cardCreateView(CreateView):
    model = Card
    fields = ["question", "answer", "box"]
    success_url = reverse_lazy("card-create")

class cardUpdateView(cardCreateView,UpdateView):
    success_url = reverse_lazy("card-list")