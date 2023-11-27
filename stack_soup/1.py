import requests
from bs4 import BeautifulSoup

url = "https://ru.stackoverflow.com/questions?tab=Newest/"
response = requests.get(url)
print(response)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup)
# questions = soup.find_all('h3', class_='s-post-summary--content-title')
# description = soup.find_all('div', class_='s-post-summary--content-excerpt')
# # print(questions)
# # print(description)
# for i in range(len(questions)):
#     print(questions[i].text)
#     print(description[i].text)