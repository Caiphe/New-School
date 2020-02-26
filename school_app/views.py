from django.shortcuts import render, redirect, get_list_or_404
from . models import NewsModel
from django.conf import settings
from django.contrib import messages
from django.views.generic import DeleteView, CreateView, UpdateView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist


# Home View
def homeView(request):
  # Getting 5 News Artile
  newsArticle = NewsModel.objects.all().order_by('id')[:5]
  
  context ={
    "newsArticle" : newsArticle,
  }
  return render(request, 'school_app/index.html', context )