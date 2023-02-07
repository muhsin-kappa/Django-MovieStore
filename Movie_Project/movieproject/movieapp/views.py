from django.http import HttpResponse
from django.shortcuts import render, redirect

from movieapp.forms import MovieForm
from movieapp.models import Movie


# Create your views here.


def index(request):
    movie = Movie.objects.all()
    context = {
        'movie_list': movie
    }
    return render(request, 'index.html', context)


def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'detail.html', {'movie': movie})


def add_movie(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        year = request.POST.get('year')
        image = request.FILES['image']
        image2 = request.FILES['image2']
        movie = Movie(name=name, description=description, year=year, image=image, image2=image2)
        movie.save()
    return render(request, 'add_movie.html')

def update(request, id):
    movie = Movie.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'movie': movie, 'form': form})


def delete(request, id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')

