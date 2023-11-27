movie_titles = ['movie1', 'movie2', 'movie3', 'movie4', 'movie5']

file = open('movie_titles.txt', 'w')
file_content = file.read


for title in movie_titles:
    file.write(title)


file.close()