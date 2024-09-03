import requests
from bs4 import BeautifulSoup
import sqlite3

# Send an HTTP request to the target webpage
url = "https://medium.com/"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Extracting all the links using CSS path
links = soup.select('a')

# Extracting all the images using CSS path
images = soup.find_all('img')

# Extracting all the paragraphs using CSS path
paragraphs = soup.find_all('p')

# Creating a database
conn = sqlite3.connect('web_data.db')
c = conn.cursor()

# Creating tables if they don't exist
c.execute('''CREATE TABLE IF NOT EXISTS links (url TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS images (src TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS paragraphs (content TEXT)''')

# Inserting data into the respective tables
for link in links:
    # print(link)
    c.execute("INSERT INTO links (url) VALUES (?)", (link['href'],))

for image in images:
    # print(image)
    c.execute("INSERT INTO images (src) VALUES (?)", (image['src'],))

for paragraph in paragraphs:
    # print(paragraph)
    content = paragraph.text.strip()
    c.execute("INSERT INTO paragraphs (content) VALUES (?)", (content,))



# Committing the changes and closing the connection
conn.commit()
conn.close()
