import datetime

import django
import os
import pandas as pd

def printMovie(movie):
    """ Print movie information """
    print(f"title: {movie.title};\n"
          f"director: {movie.director};\n"
          f"type: {movie.type};\n"
          f"description: {movie.description};\n"
          f"country: {movie.country};\n"
          f"release-year: {movie.release_year};\n"
          f"cast: {movie.cast};\n"
          f"date_added: {movie.date_added};\n"
          f"rating: {movie.rating};\n"
          f"listed-in: {movie.listed_in}")

def printFirstMovie(movies=False):
    """ Print the title of the first movie in list """

    if not movies:
        movies = Movie.objects.all()
    printMovie(movies[0])

def printTitles(movies=False):
    """ Print the titles of the movies in list """

    if not movies:
        movies = Movie.objects.all()

    for m in movies:
        print(f"- {m.title}\n")


def convertDate(date_string):
    """ Convert a date string into a date object """
    map = {
        'January': 1,
        'February': 2,
        'March': 3,
        'April': 4,
        'May': 5,
        'June': 6,
        'July': 7,
        'August': 8,
        'September': 9,
        'October': 10,
        'November': 11,
        'December': 12
    }
    if ((type(date_string) != float) and (date_string is not None and date_string != "") and (date_string != "nan")):
        tokes = date_string.split()
        month_textual = tokes[0]
        # convert the textual month to the corresponding number
        month_number = map[month_textual]
        day = int(tokes[1].replace(",", ""))
        year = int(tokes[2])
        date_obj = datetime.datetime(year, month_number, day)
        return date_obj
    return None


def ingestionDB(filepath):
    """ Save the Netflix dataset into the database """
    # delete existing movies (if any) in the database
    Movie.objects.all().delete()
    # read the dataset
    df = pd.read_csv(filepath)
    # loop over the DataFrame's rows
    for row in df.itertuples():
        # create and save a new movie
        m = Movie(title=row.title, type=row.type, description=row.description,
                  director=row.director, country=row.country, cast=row.cast, date_added=convertDate(row.date_added),
                  release_year=row.release_year, rating=row.rating, duration=row.duration,
                  listed_in=row.listed_in)
        m.save()

def filteringMoviesDB(title=False, director=False, release_year=False,
                      country=False, cast=False, duration=False,
                      listed_in=False, date_added=False, type=False):
    """ Filter movies according to multiple filters (e.g. director, country, duration, etc...)"""
    movies = Movie.objects.all()

    if title:
        movies = movies.filter(title__contains=title)
    if director:
        movies = movies.filter(director=director)
    if release_year:
        movies = movies.filter(release_year=release_year)
    if country:
        movies = movies.filter(country=country)
    if cast:
        movies = movies.filter(cast__contains=cast)
    if duration:
        movies = movies.filter(duration=duration)
    if date_added:
        movies = movies.filter(date_added=date_added)
    if type:
        movies = movies.filter(type=type)
    if listed_in:
        movies = movies.filter(listed_in__contains=listed_in)
    return movies

if __name__ == '__main__':
    # Set the Django settings (necessary for using Django functionalities in external Python scripts)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproj.settings')
    django.setup()

    # import model 'Movie' from our Django models
    from netflixapp.models import Movie

    # declare settings variables
    settings_dir = os.path.dirname(__file__)
    LAB_ROOT = os.path.abspath(os.path.dirname(settings_dir))
    PROJECT_ROOT = os.path.join(LAB_ROOT, 'myproj/')
    DATASETS_FOLDER = os.path.join(PROJECT_ROOT, 'datasets/')
    NETFLIX_DATASET_PATH = os.path.join(DATASETS_FOLDER, 'netflix_titles.csv')

    movies = filteringMoviesDB(listed_in='Comedies', cast='Bill Murray')
    printTitles(movies)
    # printFirstMovie(movies)

    # ingestionDB(NETFLIX_DATASET_PATH)
