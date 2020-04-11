from django.shortcuts import render, get_object_or_404

from .models import Post, Tag
from django.views.generic import View

class ObjectDetailMixin:
    model = None
    template = None
    def get(self,request,slug):

        n = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): n})