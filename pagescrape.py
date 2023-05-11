import requests
from bs4 import BeautifulSoup

def scrape_webpage(url, filename='scraped_content.html'):
    try:
        # Send a GET request to the webpage with a User-Agent header
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Create a BeautifulSoup object to parse the HTML content
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Get the inner HTML of the body
            content = soup.body.decode_contents()
            
            # Save the scraped content to a text file
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(content)
            
            print("Webpage content has been scraped and saved as '{}'."
                  .format(filename))
        else:
            print("Failed to retrieve the webpage. Status code:", response.status_code)
    except Exception as e:
        print("An error occurred during scraping:", str(e))

# Prompt the user to enter the URL of the webpage to scrape
url = input("Enter the URL of the webpage you want to scrape: ")

# Call the scrape_webpage function with the URL
scrape_webpage(url)
