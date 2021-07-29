# %%
# Importing libraries and specifying URL and Chrome driver path
import time
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import advertools as adv
import matplotlib.pyplot as plt

# specifying URL and nuber of job postings
postings_name = 'Data Analyst'
position_num = 100  # numbers 1 to 100

# building linkedin link
posit = '%20'.join(postings_name.split())
url = f'https://www.linkedin.com/jobs/search?keywords={posit}&location=Canada&geoId=101174742&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'

# setting chrome driver path
path = '/Users/dmytrokryvonog/Documents/DAT/gda/gdasent/chromedriver'
# %%
# opening url in Chrome browser
driver = webdriver.Chrome(path)
driver.get(url)

# %%
# scrolling down the webpage with javascript
# assigning webpage's body height in pixels
previous_height = driver.execute_script('return document.body.scrollHeight')

# scrolling to the end of body tag continuosly until the body height stops increasing
while True:
    # scrolling to the bottom of body height (y coordinate)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    # pausing for 1 sec to load
    time.sleep(1)
    # assigning webpage's increased body height in pixels
    new_height = driver.execute_script('return document.body.scrollHeight')
    # breaking the loop once the body stops growing
    if new_height == previous_height:
        break
    # updating previous height for the next loop
    previous_height = new_height

# %%
# extracting hrefs
# specifying a class where hrefs are located
lnks = driver.find_elements_by_class_name('base-card__full-link')

# looping through classes and extracting hrefs into a list
links_list = []
for lnk in lnks[:position_num]:
    link_str = (lnk.get_attribute('href'))
    links_list += [link_str]
# driver.quit()

# previewing list's contents
for y in range(3):
    print(links_list[y])

# %%
# scraping URLs' contents and combining into one string
# creating text string
words_str = ''

# try/except to avoid mistakes
try:
    for link in links_list:
        # looping through the links
        req = requests.get(link)
        print(req)
        req = req.text
        # converting to BeautifulSoup
        soup = BeautifulSoup(req, 'lxml')
        # extracting text based in class
        markup = soup.find('div', class_="show-more-less-html__markup").text
        # appending to a string and converting to lowercase
        words_str = f'{words_str} {markup}'.lower()
        # pausing for 1 sec to avoid error 429
        time.sleep(1)
except Exception as e:
    pass

# previewing strings contents
print(words_str[:500])

# %%
# plotting word cloud
# joining the sets of stopwords: English and French
sw_en_fr = adv.stopwords['english'].union(adv.stopwords['french'])

# generating word cloud with WordCloud module
wordcloud = WordCloud(width=800, height=800,
                      background_color='black',
                      stopwords=sw_en_fr,
                      min_font_size=10
                      ).generate(words_str)

# plotting the WordCloud image with matplotlib
plt.figure(figsize=(25, 25), facecolor='black')
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

# assigning file path
p_name = '_'.join(postings_name.split())
f_path = f'pngs/{p_name}-{position_num}.png'
# saving png
plt.savefig(f_path)
# printing the plot
plt.show()

# Linkedin Canada jobs sentiment web scraping and visualization - Python

# This Python script scrapes up to 100 most recent Linkedin job postings of any job title and creates sentiment visualization in a form of a word cloud.
