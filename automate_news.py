from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import pandas as pd

website = "https://www.thesun.co.uk/sport/football/"
path = "C:/Users/maazr/Downloads/geckodriver-v0.33.0-win64/geckodriver.exe"

service = Service(executable_path=path)
driver = webdriver.Firefox(service=service)
driver.get(website)

# finds all of the elements on the xpath
containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]') 


titles = []
subtitles = []
links = []

#itetaring over all the items in the xpatch in containers
for container in containers:
    title = container.find_element(by="xpath", value='./a/span').text
    subtitle = container.find_element(by="xpath", value='./a/h3').text
    link = container.find_element(by="xpath", value='./a').get_attribute("href")
    
    # appending all the info extracted to the list
    titles.append(title)
    subtitles.append(subtitle)
    links.append(links)

#creating a Dictionary of all the info
my_dict = {'TITLES' : titles, 'SUBTITLES' : subtitles, 'LINKS' : link}

#making a data frame and assigning it a variable df_headlines
df_headlines = pd.DataFrame(my_dict)

#turing that data frame into a csv file
df_headlines.to_csv('headline_new.csv')

driver.quit()
