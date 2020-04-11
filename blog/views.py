from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse
from .models import Post, Tag
from django.views.generic import View
from .utils import ObjectDetailMixin
from .forms import TagForm





# Create your views here.
def posts_list(request):
    n = Post.objects.all()
    # return HttpResponse('<h1> Hello<h1>')
    return render(request, 'blog/index.html', context={'posts': n})
class PostDetail(View):
    def get(self,request,slug):
        # n = Post.objects.get(slug__iexact=slug)
        n = get_object_or_404(Post, slug__iexact=slug)
        return render(request, 'blog/post_detail.html', context={'post': n})
# def post_detail(request,slug):
#     # n = Post.objects.all()
#
#     n = Post.objects.get(slug__iexact=slug)
#     return render(request, 'blog/post_detail.html', context={'post': n})


def tags_list(request):
    n = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': n})
class TagCreate(View):
    def get(self,request):
        form = TagForm()
        return render(request,'blog/tag_create.html', context={'form': form})

    def post(self, request):

        print(dir(request))
        bound_form = TagForm(request.POST)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(request,'blog/tag_create.html', context={'form': bound_form})

##################### mixin can will use for class PostDataile ################################
class TagDetail(ObjectDetailMixin,View):
    model = Tag
    template = 'blog/tag_detail.html'
##################### mixin can will use for class PostDataile ################################

# def tags_detail(request, slug):
#     tag = Tag.objects.get(slug__iexact=slug)
#     return render(request, 'blog/tag_detail.html', context={'tag': tag})