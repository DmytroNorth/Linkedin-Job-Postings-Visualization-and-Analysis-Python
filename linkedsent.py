# %% [markdown]

# # Linkedin jobs sentiment visualization and web scraping - `Python`, `JavaScript`

# ## Description
# This `Python` script scrapes up to 100 most recent Linkedin Job Postings of any Job Title and creates sentiment visualization in a form of a **word cloud**.

# ## Setting up
# First, we are importing all the necessary libraries. We are also specifying **Job Title** we wish to visualize and the number of **Job Postings** to scrape. We are then creating a link based on a Job Title.
#
# Note by default jobs' location is set to **Canada**. It can be changed to any other location simply by pasting Linkedin URL that contains desired Job Postings in the desired location.
#
# We are also setting up `Chrome Driver` locally, specifying its' path. And finally opening the link in a Chrome browser with `selenium`.

# %%
# Importing libraries and specifying URL and Chrome driver path
import time
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import advertools as adv
import matplotlib.pyplot as plt

# specifying URL and number of job postings
postings_name = 'Data Analyst'
position_num = 10  # numbers 1 to 100

# building linkedin link
posit = '%20'.join(postings_name.split())
url = f'https://www.linkedin.com/jobs/search?keywords={posit}&location=Canada&geoId=101174742&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'

# setting chrome driver path
path = '/Users/dmytrokryvonog/Documents/DAT/gda/gdasent/chromedriver'

# opening url in Chrome browser
driver = webdriver.Chrome(path)
driver.get(url)

# %% [markdown]
# Now the link is opened in **Chrome browser**. However, most job postings are **hidden** and cannot be scraped. We will have to scroll the webpage down before we can scrape.

#  ![linkedin-data-analyst-canada](/img/linkedin-dataanalyst.png)

# ## Loading webpage by scrolling down with `JavaScript`

# Since `Python` does not have a built-in function to scroll pages we are using `JavaScript` to scroll the webpage down and also to check **body height** to determine when to stop the loop.

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

# %% [markdown]
# After 100 job postings there is a "See more jobs" button. Since 100 jobs should be enough for hour purposes we don't proceed with pressing the button.

# ![linkedin-data-analyst-canada](/img/linkedin-dataanalyst-scrolldown.png)

# ## Scraping job postings' links

# Once we have all 100 job postings loaded we can **scrape the links** with `selenium`.

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

# %% [markdown]

# ## Parsing and scraping each job posting

# Now we can use `requests.get()` to parse each link, then `BeautifulSoup` module to scrape the text of **Job Description**. All text is appended to one string.

# %%
# scraping URLs' contents and combining into one string
# creating text string
time.sleep(1)
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

# %% [markdown]
# ## Plotting word cloud

# Since Canadian Job Postings can be in **English and French** we are using **stop words** from `advertools` module by combining two languages in one set.
#
# We then generate `WordCloud` class and plot it using `matplotlib`, then save as `.png` in **png** folder.


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
plt.figure(figsize=(10, 10), facecolor='Black')
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

# %%
