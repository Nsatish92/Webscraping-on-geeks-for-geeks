!pip install requests
!pip install beautifulsoup4
!pip install pandas
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Send a GET request to the user profile page
username = input()
url = f"https://auth.geeksforgeeks.org/user/"+username

response = requests.get(url)

# Parse the HTML response
soup = BeautifulSoup(response.text, 'html.parser')

# Find the user rating element
rating_element = soup.find('div', class_='score_card_left')

#e=soup.find('div',class_="contest-participated-count")
# Extract the rating value
rating = rating_element.text.strip()
#s=e.text.strip()

# Print the user rating
print('User Rating:', rating)
#print(s)
