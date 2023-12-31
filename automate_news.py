from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import pandas as pd
from datetime import datetime
import os #helps intrect with computer os
import sys

application_path = os.path.dirname(sys.executable) #getting the path of the executable

#to change the name of the csv file to include date 
now = datetime.now()
month_day_year = now.strftime("%m%d%Y") #using this the now variable is in time format MMDDYYYY


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
file_name = f'headline-{month_day_year}.csv'
final_path = os.path.join(application_path, file_name)
df_headlines.to_csv(final_path) #with this the csv file will me send to this path and having file name

driver.quit()

#command to turn py file to exe
#use pyinstaller #pyinstaller --onefile {py file name}