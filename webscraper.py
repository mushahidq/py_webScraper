import requests
from bs4 import BeautifulSoup
url = ""
web_r = requests.get(url) # Sends the request to the URL
web_r #Displays the reponse code
web_r.status_code #Displays the status code
web_r.text #Displays the result
web_soup = BeautifulSoup(web_r.text, 'html.parser')
print(web_soup.prettify()) #Prettifies the HTML

#print(web_soup.finAll('a'))
"""
Looks for all instances of 'a'.
Here a can be changed to whatever tag we want to look of;
for example some websites use list/li tag to classify links.
"""

#Also look for a class named 'class-name' using the dictionary
for link in web_soup.findAll('a', {'class' : 'class-name'}) :
    print(link.text) # Gives the text between the filtered HTML