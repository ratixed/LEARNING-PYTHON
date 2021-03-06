from bs4 import BeautifulSoup
import requests

# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# # all_anchor_tags = soup.find_all(name="a")
# #
# # # for tag in all_anchor_tags:
# # #     print(tag.get("href"))
# #
# # heading = soup.find(name="h1", id="name")
# # print(heading)
# #
# # section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading.get("class"))
#
# company_url = soup.select_one(selector="p a")
# print(company_url)

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []

for article_tag in articles:
    article_texts.append(article_tag.getText())
    article_links.append(article_tag.get("href"))


article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
largest_number = max(article_upvotes)
article_upvotes.index(largest_number)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])
print(article_upvotes[largest_index])



