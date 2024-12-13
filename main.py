import requests
from bs4 import BeautifulSoup
import re

base = "https://www.boci-pru.com.hk/en/etf/wiseetf"
courses_url = base + "/02825"

# get website contents and parse html
response = requests.get(courses_url)
html = BeautifulSoup(response.text, 'html.parser')

categories_html = html.find('div', {"id" : "cms_table_etf_nav"})
# courses_html = categories_html.findChildren("div", id=re.compile('^Course-'))

# create markdown string of courses
# courses_markdown = "# Babyschwimmen Wise"
""" for c in courses_html:
    # parse information
    headline = c.find('h5', {"class" : "card-title"}).text
    text = c.find('p').text
    url = base + c.find('a' ,href=True)['href']
    
    # Strip whitespaces
    headline_stripped = re.sub(' +', ' ', headline).strip()
    text_stripped = re.sub(' +', ' ', text).strip()
    
    # append to markdown
"""
    courses_markdown += categories_html
"""
## {}
[{}]({})
"""#.format(headline_stripped, text_stripped, url)
      
# write markdown file
with open("courses.md", "w") as courses_file:
    courses_file.write(courses_markdown)
