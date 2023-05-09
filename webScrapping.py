# import requests
# from bs4 import BeautifulSoup

# """Scrapping du site Jumia"""

# from pprint import pprint
# lien = requests.get("https://www.jumia.ci/telephone-tablette/")
# soup = BeautifulSoup(lien.text, "html.parser")

# data = []
# articles = soup.select("article.prd._box.col._hvr")
# for article in articles:

#     dico = {
#         "image": article.select("img.img")[0].attrs["data-src"],
#         "titre": article.select("div.name")[0].text,
#         "prix": article.select("div.prc")[0].text
#         }
    
#     link = "https://www.jumia.ci" + article.select("a.core")[0].attrs["href"]
#     r = requests.get(link)
#     soup1 = BeautifulSoup(r.text, "html.parser")





#     print(link)