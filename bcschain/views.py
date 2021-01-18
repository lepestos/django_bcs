from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Block
import requests


class BlockListView(ListView):
    model = Block
    paginate_by = 50


class BlockDetailView(DetailView):
    model = Block
