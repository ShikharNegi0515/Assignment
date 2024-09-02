from bs4 import BeautifulSoup
import requests
import json

url="https://time.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

latest_stories_section = soup.find('div', class_='partial latest-stories')

news_list = []
if latest_stories_section:
    for item in latest_stories_section.find_all('li', class_='latest-stories__item'):
        headline = item.find('h3', class_='latest-stories__item-headline').get_text(strip=True)
        link = item.find('a', href=True)['href']

        news_list.append({
            "title": headline,
            "link": url.rstrip('/') + link
        })

    print(json.dumps(news_list, indent=4))
