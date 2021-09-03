import requests, csv
from collections import defaultdict, Counter


url = "https://raw.githubusercontent.com/sundeepblue/movie_rating_prediction/master/movie_metadata.csv"


def save_movie_metadata():

    raw_string_data_from_response = requests.get(url).text

    with open('utilization/movie_metadata.csv', 'w')  as csv_file:
        csv_file.write(raw_string_data_from_response)

# Task: Get the 20 highest rated directors based on their average movie IMDB ratings.

# Parse the movie_metadata.csv, using csv.DictReader you get a bunch of OrderedDicts from which you only need the following k,v pairs:

parsed_data = defaultdict(list)

with open('utilization/movie_metadata.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    lines = [line for line in csv_reader]

    print("Raw list with titles length:", len(lines))

# Take movies of year >= 1960

for line in lines:
    if line['title_year'] == '': continue
    if int(line['title_year']) >= 1960:

        # Usable Data: director_name, movie_title, title_year, imdb_score
        parsed_data[line['director_name']].append(dict({'title_year': line['title_year'], 'movie_title': line['movie_title'], 'imdb_score': line['imdb_score']}))

print("Length without empty years and years < 1960:", len(parsed_data))

# Only consider directors with a minimum of 4 movies

dirs_with_less_4_movies = [item[0] for item in parsed_data.items() if len(item[1]) < 4]

for item in dirs_with_less_4_movies:
    parsed_data.pop(item)

print("Length of dirs with less than 4 movies:", len(parsed_data))

# Print the top 20 highest rated directors with their movies ordered desc on rating.

directors_by_score = {}

for item in parsed_data.items():

    score = 0

    for movie in item[1]:
        score += float(movie["imdb_score"])

    directors_by_score[item[0]] = round(score / len(item[1]), 1)

top_directors = Counter(directors_by_score).most_common(20)

for director in top_directors:
    print(director[0], director[1])
    print("------------")

    length = len(parsed_data[director[0]])

    for number in range(length):
        print(parsed_data[director[0]][number]['title_year'], parsed_data[director[0]][number]['movie_title'], parsed_data[director[0]][number]['imdb_score'])

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