import datetime

from django.shortcuts import render
from django.utils.dateformat import DateFormat
# Create your views here.


from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from .models import Movie


def index(request):
    movies = Movie.objects.order_by('title')
    context = {'movies': movies}
    return render(request, 'netflixapp/index.html', context)


def tabular(request):
    movies = Movie.objects.order_by('title')
    context = {'movies': movies}
    return render(request, 'netflixapp/tabular.html', context)


def add_movie(request):
    message = ""
    context = {"message": message, "message_type": None}
    # other fields omitted for the sake of neatness
    if request.method == 'POST':
        title = request.POST.get("title", None)
        type = request.POST.get("type", None)
        desc = request.POST.get("description", None)
        director = request.POST.get("director", None)
        country = request.POST.get("country", None)
        cast = request.POST.get("cast", None)
        date_added = request.POST.get("date_added", None)
        release_year = request.POST.get("release_year", None)
        rating = request.POST.get("rating", None)
        duration = request.POST.get("duration", None)
        listed_in = request.POST.get("listed_in", None)

        if date_added == '':
            date_added = None
        if release_year == '':
            release_year = None
        if not title:
            message = "An error occurred, your movie has not been added"
            context = {"message": message, "message_type": "error"}
        else:
            m = Movie(title=title, type=type, description=desc,
                      director=director, country=country, cast=cast,
                      date_added=date_added, duration=duration, rating=rating,
                      listed_in=listed_in, release_year=release_year)

            m.save()
            message = f"Congratulations: your movie <b>{m.title}</b> has been added!"
            context = {"message": message, "movie": m, "message_type": "success"}

    return render(request, 'netflixapp/add-movie.html', context)

def delete_movie(request):
    message = "No movie"
    message_type = "error"

    context = {"message": message, "message_type": message_type}

    if request.method == 'POST':
        movie_id = request.POST.get('movie-id')
        try:
            movie = Movie.objects.get(id=movie_id)
            movie.delete()
            message = f"The movie: <b>{movie.title}</b> has been deleted"
            message_type = "success"
        except ObjectDoesNotExist:
            message = f"The requested movie does not exist"
            message_type = "error"
        context = {"message": message, "message_type": message_type}

    movies = Movie.objects.order_by('title')
    context["movies"] = movies

    return render(request, 'netflixapp/tabular.html', context)


def edit_movie(request):

    # we accept only POST requests => other types are invalid
    message = "Invalid request method"
    context = {"message": message, "message_type": "error"}

    if request.method == 'POST':
        movie_id = request.POST.get("movie-id", None)
        action = request.POST.get("action", None)

        if movie_id is not None:
            #      Get the movie data
            m = Movie.objects.get(id=movie_id)
            if action is not None and action == "save":
                title = request.POST.get("title", None)
                type = request.POST.get("type", None)
                desc = request.POST.get("description", None)
                director = request.POST.get("director", None)
                country = request.POST.get("country", None)
                cast = request.POST.get("cast", None)
                date_added = request.POST.get("date_added", None)
                release_year = request.POST.get("release_year", None)
                rating = request.POST.get("rating", None)
                duration = request.POST.get("duration", None)
                listed_in = request.POST.get("listed_in", None)

                if date_added == '':
                    date_added = None
                else:
                    date_added = datetime.datetime.strptime(date_added, "%Y-%m-%d").date()
                    date_added = DateFormat(date_added).format('Y-m-d')
                if release_year == '':
                    release_year = None

                m.title = title
                m.type = type
                m.description = desc
                m.director = director
                m.country = country
                m.cast = cast
                m.date_added = date_added
                m.duration = duration
                m.rating = rating
                m.listed_in = listed_in
                m.release_year = release_year
                m.save()
                message = f"Congratulations: your movie <b>{m.title}</b> has been edited successfully!"
                context = {"message": message, "movie": m, "message_type": "success"}

            elif action is not None and action == "edit":
                if m.date_added == '':
                    m.date_added = None
                else:
                    m.date_added = DateFormat(m.date_added).format('Y-m-d')
                context = {"movie": m}

            else:
                message = "invalid action"
                print(f"action: {action}")
                context = {"message": message, "message_type": "error"}


        else:
            #     Error: Invalid movie identifier
            print()
            message = "Invalid movie identifier"
            context = {"message": message, "message_type": "error"}

    return render(request, 'netflixapp/edit-movie.html', context)