import requests
from bs4 import BeautifulSoup

def parse_website(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Example: Extract title and meta description
        title = soup.title.string if soup.title else 'No title found'
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        description = meta_desc['content'] if meta_desc else 'No description found'
        return {'title': title, 'description': description}
    except Exception as e:
        return {'error': str(e)}

def parse_google_play(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Example: Extract title and meta description
        title = soup.title.string if soup.title else 'No title found'
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        description = meta_desc['content'] if meta_desc else 'No description found'
        return {'title': title, 'description': description}
    except Exception as e:
        return {'error': str(e)}
