from django.shortcuts import render
from django.http import HttpResponse
from django.http.request import HttpRequest
import  random
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, UpdateView
from .models import BlogPost
from .forms import BlogForm
# Create your views here.

def random_number(request):
    return HttpResponse(f"Random number: {random.randint(1, 100)}")

class PostListView(ListView):
    template_name = 'index.html'
    queryset: list[BlogPost] = BlogPost.objects.all()
    context_object_name = 'blogs'

class PostChangeView(UpdateView):
    model = BlogPost
    fields = {
        "image", "title", "description"
    }

    template_name = "BlogChange.html"

class PostDetailView(DetailView):
    queryset = BlogPost.objects.all()
    template_name = 'blog_detail.html'
    context_object_name = 'blog'

    # def get_context_data(self, **kwargs):
    #     contex: dict = super(PostDetailView, self).get_context_data(**kwargs)
    #     pk = self.kwargs["pk"]
    #     comments: list[Comment] = Comment.objects.filter(post_id=pk)
    #     context["comments"] = comments
    #     return contex


def create_blog_view(request: HttpResponse):
    if request.method == "POST":
        data = request.POST
        files = request.FILES
        title = data.get("title")
        description = data.get("description")
        image = files.get("image")
        BlogPost.objects.create(title=title, image=image, description=description)
        return redirect("/blog/")
    elif request.method == "GET":
        return render(request, 'blog_create.html')


