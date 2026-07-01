import requests
from bs4 import BeautifulSoup
import re

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
URL = "https://habr.com/ru/articles/"

response = requests.get(URL)
soup = BeautifulSoup(response.content, "lxml")
print(f"📊 Статус ответа: {response.status_code}")

articles = soup.find_all("div", class_="article-snippet" )
print(f"📝 Найдено статей на странице: {len(articles)}")

for article in articles:
    title_tag = article.find("h2", class_="tm-title tm-title_h2")
    title = title_tag.text.strip()

    link_tag = title_tag.find("a", class_="tm-title__link")
    link = 'https://habr.com' + link_tag.get('href')

    date_tag = article.find('time')
    date = date_tag.get('title')

    preview_tag = article.find('div', class_='article-formatted-body article-formatted-body article-formatted-body_version-2')
    preview_text = preview_tag.text.strip() if preview_tag else ""

    full_text = (preview_text + ' ' + title).lower()
    for keyword in KEYWORDS:
        pattern = re.compile(keyword, re.IGNORECASE)
        if pattern.search(full_text):
            print(f"{date}-{title}-{full_text}")