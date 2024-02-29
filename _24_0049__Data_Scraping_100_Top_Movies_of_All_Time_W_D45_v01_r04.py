from bs4 import BeautifulSoup
import requests

# CONSTANTS:
LIMIT_OF_MAXIMUM_ARTICLES_TO_DATA_SCRAPE = 100
print(f"Generating {LIMIT_OF_MAXIMUM_ARTICLES_TO_DATA_SCRAPE} Movies in the List... \n")
print("Movie:")

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
html_doc = response.text

soup = BeautifulSoup(html_doc, 'html.parser')

# USE PRETTIFY on the html doc:

# initialize an empty list to store article information
movies_list = []

title1 = ""

article_rows = soup.find_all('h3', class_='listicleItem_listicle-item__title__BfenH', limit=LIMIT_OF_MAXIMUM_ARTICLES_TO_DATA_SCRAPE)

for row in article_rows:
    movies_list.append(row.text)

# Format for the Movie Title:   <h3 class="listicleItem_listicle-item__title__BfenH">100) Reservoir Dogs</h3>


reversed_movie_list = list(reversed(movies_list))
# or you can use: slice operator [::-1]

movie_text_for_txt_file = "\n".join(reversed_movie_list)

# creates .txt file to write the full numbered list to:
with open("100_Top_Movies-1.txt", mode="w") as file:
    contents = file.write(f"The 100 Greatest Movies of All Time:\n"
                          f"{movie_text_for_txt_file}\n")


print(movie_text_for_txt_file)