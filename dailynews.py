import requests
from bs4 import BeautifulSoup

def fetch_articles(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')
        page_name = soup.title.text.strip()
        articles = soup.find_all('article')
        for article in articles:
            link_tag = article.find('a', href=True)
            title_tag = article.find('h3')
            description_tag = article.find('p')
            link = link_tag['href'] if link_tag else 'No link found'
            title = title_tag.text.strip() if title_tag else 'No title found'
            description = description_tag.text.strip() if description_tag else 'No description found'
            print(f"Page Name: {page_name}")
            print(f"Link: {link}")
            print(f"Title: {title}")
            print(f"Description: {description}")
            print('-' * 40)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
if __name__ == "__main__":
    url = "https://devblogs.microsoft.com/dotnet/category/aspnetcore/"
    fetch_articles(url)
