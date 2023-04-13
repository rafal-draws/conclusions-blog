from django.views import generic
from .models import PlPost, EnPost

class PostListEn(generic.ListView):
    queryset = EnPost.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    context_object_name = 'post_list' 


class PostListPl(generic.ListView):
    queryset = PlPost.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    context_object_name = 'post_list' 


class PostDetailPl(generic.DetailView):
    model = PlPost
    template_name = 'post_detail_pl.html'


class PostDetailEn(generic.DetailView):
    model = EnPost
    template_name = 'post_detail_en.html'