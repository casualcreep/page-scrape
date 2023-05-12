import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os
import random

def send_get_request(url):
    headers = {'User-Agent': random_user_agent()}
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    return response

def parse_html_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.body.decode_contents()
    return content

def save_content_to_file(content, url):
    parsed_url = urlparse(url)
    netloc = parsed_url.netloc
    sanitized_netloc = ''.join(c for c in netloc if c.isalnum() or c in ('-', '_'))
    filename = sanitized_netloc + '.html'
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
    return filename

def scrape_webpage(url):
    try:
        response = send_get_request(url)
        content = parse_html_content(response.content)
        filename = save_content_to_file(content, url)
        print("Webpage content has been scraped and saved as '{}'.".format(filename))
    except requests.exceptions.HTTPError as e:
        print("Failed to retrieve the webpage. HTTP Error: {} - {}".format(e.response.status_code, e.response.reason))
    except requests.exceptions.RequestException as e:
        print("An error occurred during the request:", str(e))
    except IOError as e:
        print("An error occurred while saving the file:", str(e))
    except Exception as e:
        print("An error occurred during scraping:", str(e))

def random_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    ]
    return random.choice(user_agents)

# Prompt the user to enter the URL of the webpage to scrape
url = input("Enter the URL of the webpage you want to scrape: ")

# Call the scrape_webpage function with the URL
scrape_webpage(url)
