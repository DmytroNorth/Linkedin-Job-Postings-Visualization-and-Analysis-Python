# Linkedin jobs sentiment visualization and scraping - Python, JavaScript
This Python script **scrapes** up to 100 most recent **Linkedin Job Postings** of any job title and creates **sentiment visualization** in a form of a **word cloud**. It is currently limited to **Canada only**, but the code can be easily changed for any other location.

See **Jupiter notebook** [linkedsent.ipynb](/linkedsent.ipynb) for detailed presentation.

![Text to video edits - FinalCut Pro](/img/data-analyst-social.png)


## 1. Table of Contents

- [Linkedin jobs sentiment visualization and scraping - Python, JavaScript](#linkedin-jobs-sentiment-visualization-and-scraping---python-javascript)
  - [1. Table of Contents](#1-table-of-contents)
  - [2. Description](#2-description)
    - [2.1 Problem](#21-problem)
    - [2.2 Solution](#22-solution)
    - [2.3 Motivation behind the project](#23-motivation-behind-the-project)
    - [2.4 Development history](#24-development-history)
    - [2.5 Challenges encountered and overcome](#25-challenges-encountered-and-overcome)
  - [3. Technologies Used](#3-technologies-used)
    - [Coding](#coding)
    - [Parsing and Scraping](#parsing-and-scraping)
    - [Plotting](#plotting)
  - [4. Installation](#4-installation)
  - [5. Usage](#5-usage)
  - [6. Project Status](#6-project-status)
  - [7. Known Limitations](#7-known-limitations)
  - [8. Room for Improvement](#8-room-for-improvement)
  - [9. License](#9-license)
  - [10. Contact](#10-contact)

<!-- * [License](#license) -->

## 2. Description

### 2.1 Problem

It is crucial for **job seekers** to write resumes, cover letters, and Linkedin profiles using the language of their **potential employers**. The task is even more difficult for recent graduates and those who **switch fields**. Job seekers there must read through dozens of Job Positions to **pick up the lingo** before even start drafting a resume or a cover letter.

### 2.2 Solution

Instead of **manually** reading through Job Postings this script **scrapes** up to **100 recent Job Postings** in Canada and creates **Word Cloud Visualization** where the size of the word represents the frequency of its total use.

This script can also be useful for **career exploration**, **comparison** of different positions, or even for monitoring how **employers' sentiment** changes over time.

### 2.3 Motivation behind the project

When starting as a **Data Analyst** I was told by a **Career Strategist**, that I should use '**employers' language**' in my application documents... The challenge was accepted with the mindset of a Data Analyst :).

### 2.4 Development history

Throughout the project, multiple **web parsing and scraping tools** were explored, such as `requests`, `selenium`, and `bs4`. `ChromeDriver` which is a tool designed for automated testing of web apps across many browsers was adapted to navigate and **load hidden content** of a webpage.

Also, a few **custom libraries** were discovered and utilized such as `wordcloud` to generate word cloud and `advertools` to filter out stop words in **multiple languages**.

### 2.5 Challenges encountered and overcome
* #### **Hidden webpage content**
  * Problem: The original Linkedin web page only displays around 13 Job postings by default. Up to 100 Job Postings are loaded as the user scrolls down the web page.
  * **Solution:** Using `selenium` and `ChromeDriver` to open the webpage and scroll down to the bottom of the page.
* #### **Run-time error 429**
  * Problem: When scraping data from 100 links using `for loop` only about 20 will be successfully scraped. The rest would be blocked by Run-time error 429 due to frequent requests.
  * **Solution:** Using `time` module to pause the execution for 1 second at the end of each loop. And printing out response code to ensure that all 100 links give `resonse 200`.
* #### **AttributeError of NoneType object**
  * Problem: When scraping Job Postings with `bs4` and converting to text this error would be printed. 
    ```
    Error: 'NoneType' object has no attribute 'text'
    ```
  * **Solution**: putting the `for loop` inside `try except` solved the issue.

## 3. Technologies Used

### Coding
* `Python 3.8.8` as a main language.
* `JavaScript` to scroll down and load the full length of web pages.

### Parsing and Scraping
* `chromedriver` standalone server to automate opening and navigating webpages.
* `Google Chrome` web browser to run **ChromeDriver**.
* `time` module to pause between web queries to avoid run-time `error 429`.
* `requests` module to parse web content.
* `selenium` module to open and navigate through a webpage.
* `bs4` **Beautiful Soup** module to scrape content from web pages.
* `advertools` module to filter out English and French stop words.

### Plotting
* `wordcloud` module to generate a word cloud.
* `matplotlib` module to plot word cloud.


## 4. Installation

1. Install Python 3 on your system.
2. Install all libraries/modules listed in [Technologies Used](#3.-technologies-used).
   * On **Mac OS** open `Terminal.app`
   * type `pip install` and the name of the module you want to be installed, then press Enter
3. Download and install [Google Chrome web browser](https://www.google.com/chrome/index.html).
4. Download [ChromeDriver](https://chromedriver.chromium.org/downloads), unzip it, and move to `/usr/local/bin` location on **Mac OS**.
5. Download [linkedsent.py](/linkedsent.py) file from this GitHub repository.
## 5. Usage
1. Open linkedsent.py with any text editor like `TexEdit.app` or `Atom.app`.
2. Look for this code approximately in the first 30 lines.

```
# specifying URL and number of job postings
postings_name = 'Data Analyst'
position_num = 10  # numbers 1 to 100
```
3. Replace `Data Analyst` with a **Job Position** of your choice.
4. Replace number `10` with the number of **jobs you want to scrape**. Teh maximum number is 100.
5. Open **Terminal.app**. Type `python`, add `space`, then drag and drop `linkedsent.py` and press `Return`. This will run the script, open and scroll down Linkedin webpage in Google Chrome browser, then you should see multiple `<Response [200]>` each representing parsing a single Job Posting. Eventually, it will open a separate window with wordcloud image.
6. Click **save** button to save the image locally.

## 6. Project Status

The project is: **_complete_**

I am no longer working on it since I received the result I was looking for. But if you have some ideas or want me to modify something [contact me](#contact) and we should be able to collaborate.

## 7. Known Limitations

* Tested on **Mac OS** only.
* The script only runs with `ChromeDriver` and all the modules listed in [Technologies Used](#3-technologies-used).
* The script only scrapes Job Postings in **Canada** (which can be easily changed **inside the script**).
* The maximum amount of Job Postings to scrape is **100**.

## 8. Room for Improvement

* **Testing** and logging the issues.
* Designing solution to avoid using ChromeDriver and Chrome Browser.
* Making an **executable file** without the need to install additional modules.
* **Developing GUI** to be able to specify:
  * Job Title
  * location
  * number of Job Postings to scrape
  * Image aspect ratio and quality
  * the path where to save the image
* Building a **web app**.
## 9. License

This project is open-source and available under the [GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/#)

## 10. Contact

Created by [@DmytroNorth](https://github.com/DmytroNorth) - feel free to contact me at dmytronorth@gmail.com!
