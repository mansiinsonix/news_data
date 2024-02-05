import requests
from bs4 import BeautifulSoup
import csv

source_code = requests.get('https://www.ndtv.com/')
plain_text = source_code.content
soup = BeautifulSoup(plain_text, "html.parser")

#CSS selector to select a tags within divs with class "thumbnail"
css_selector = 'div.thumbnail a'

# Find all a tags within the selected divs
a_tags = soup.select(css_selector)

# Create a list to store data
data_list = []

# Extract href and title attributes
for a_tag in a_tags:
    href = a_tag.get('href', '')
    # Get the title from the img tag within the a tag
    img_tag = a_tag.find('img')
    title = img_tag.get('title', '') if img_tag else ''

    # Check if title is not empty
    if title:
        data_list.append({'Title': title, 'Link': href})

#Create and write to a CSV file
csv_file_path = 'ndtv_data.csv'
field_names = ['Title','Link']

with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=field_names)
    # Write header
    csv_writer.writeheader()
    # Write data
    csv_writer.writerows(data_list)

print(f"CSV file '{csv_file_path}' created successfully.")
