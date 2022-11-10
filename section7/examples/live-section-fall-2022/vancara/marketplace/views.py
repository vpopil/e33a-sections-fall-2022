from django.shortcuts import render
from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Vehicle

PAGE_SIZE=2

def render_with_pagination(request, vehicles):
    page_num = request.GET.get('page', 1)
    paginator = Paginator(vehicles, per_page=PAGE_SIZE)
    page = paginator.page(page_num) 
    return render(request, "marketplace/index.html", {'page': page})


def index(request):
    vehicles = Vehicle.objects.all()
    return render_with_pagination(request, vehicles)
    

def make(request, id):
    vehicles = Vehicle.objects.filter(make__id=id)
    return render_with_pagination(request, vehicles)


def update_post():
    content =data.

    post = Post by id
    post.content= content
    post.content.save()

    return jsonify({'content':post.content})