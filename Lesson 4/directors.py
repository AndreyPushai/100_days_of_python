import csv
from collections import defaultdict, Counter, namedtuple
from urllib.request import urlretrieve

# Save csv to a file

url = "https://raw.githubusercontent.com/sundeepblue/movie_rating_prediction/master/movie_metadata.csv"
urlretrieve(url, 'Lesson 4/movie_metadata.csv')

# Task: Get the 20 highest rated directors based on their average movie IMDB ratings.

Movie = namedtuple("Movie", "year title score")

parsed_data = defaultdict(list)

# Parse the movie_metadata.csv, using csv.DictReader you get a bunch of OrderedDicts

with open('Lesson 4/movie_metadata.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    lines = [line for line in csv_reader]

    # print("Raw list with titles length:", len(lines))

# Take movies of year >= 1960

for line in lines:
    if line['title_year'] == '': continue
    if int(line['title_year']) >= 1960:

        # Usable Data: director_name, movie_title, title_year, imdb_score

        director = line['director_name']
        movie = Movie(year=line['title_year'], title=line['movie_title'], score=line['imdb_score'])
        parsed_data[director].append(movie)

        # Instead of this exhaustive append to parsed data we can use named tuple

# print("Length without empty years and years < 1960:", len(parsed_data))

# Only consider directors with a minimum of 4 movies

dirs_with_less_4_movies = [director for director, movie in parsed_data.items() if len(movie) < 4]

for item in dirs_with_less_4_movies:
    parsed_data.pop(item)

# print("Length of dirs with less than 4 movies:", len(parsed_data))

# Print the top 20 highest rated directors with their movies ordered desc on rating.

directors_by_score = {}

for director, movies in parsed_data.items():

    score = 0

    for movie in movies:
        score += float(movie.score)

    directors_by_score[director] = round(score / len(movies), 1)

top_directors = Counter(directors_by_score).most_common(20)

for director, score in top_directors:
    print(director, score)
    print("------------")
 
    length = len(parsed_data[director])

    for number in range(length):
        print(
            parsed_data[director][number].year,
            parsed_data[director][number].title,
            parsed_data[director][number].score
            )
    print("\n")

# Examlpe of realizaton:

# 01. Sergio Leone                                         8.5
# ------------------------------------------------------------
# 1966] The Good, the Bad and the Ugly                     8.9
# 1968] Once Upon a Time in the West                       8.6
# 1984] Once Upon a Time in America                        8.4
# 1964] A Fistful of Dollars                               8.0

# 02. Christopher Nolan                                    8.4
# ------------------------------------------------------------