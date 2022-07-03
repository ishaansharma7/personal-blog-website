from django.shortcuts import render
from .models import PostDetail
from django.views.generic import TemplateView, ListView, DetailView


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = PostDetail.objects.get(post_id=8)
        return context

class FeedView(ListView):
    context_object_name = 'posts'
    model = PostDetail
    template_name = 'feed.html'

    paginate_by = 3

    def get_queryset(self):
        return PostDetail.objects.filter(post_id__gte=1).order_by('-post_id')


class PostDetailView(DetailView):
    context_object_name = 'post'
    model = PostDetail
    template_name = 'detail_post.html'

def search(request):
    query = request.GET['query']
    allpost = PostDetail.objects.filter(post_title__icontains=query)
    return render(request, 'searched.html', {'allpost':allpost})