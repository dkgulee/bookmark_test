from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . models import Bookmark
# Create your views here.

class BookmarkLsit(ListView):
    model = Bookmark   #Bookmark 객체를 넘긴다
    context_object_name = "list" # 모댈만 줘도 object_list 로 view에 보낸다
    paginate_by = 2

class BookmarkCreateView(CreateView):
    model = Bookmark     # 모댈로 북마크를 받아오기
    fields = ['site_name', 'url']  # model 의 속성들을 추가
    success_url = reverse_lazy('list')  #  성골하면

class BookmarkDetailView(DetailView):
    model = Bookmark


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'  # tamplate_name 을 변경해주는 역할
    success_url = reverse_lazy('list')  # HttpresphonseRedirect 역할을 함

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    # fields = ['site_name', 'url']
    success_url = reverse_lazy('list')