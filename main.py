import requests
from bs4 import BeautifulSoup

url = 'https://www.engagebay.com'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

data = []

home_banner_top = soup.find('div', 'home-banner-top').text.replace("\n", "")
data.append(" ".join(home_banner_top.split()))

products = soup.find('div', 'dropdown-menu megamenu').text.replace("\n", "")
data.append(" ".join(products.split()))

home_features = soup.find_all('div', 'card')
for i in home_features:
    data.append(" ".join(i.text.replace("\n", "").split()))

award = soup.find('section', {"class": "section award-sec"})
data.append(" ".join(award.text.replace("\n", "").split()))

for i in award.find_all("img"):
    data.append("badge link: " + i.attrs["data-src"])

tab_views = soup.find('section', {"class": "section tabs-views nav-tabs-line"}).find_all('div', 'tab-pane fade')

for i in tab_views:
    data.append(" ".join(i.text.replace("\n", "").split()))

testimonials = soup.find('section', {"class": "section testimonial-sec position-relative z-index-1"}).text.replace("\n",
                                                                                                                   "")
data.append(" ".join(testimonials.split()))

features = soup.find('section', {"class": "section eb-features-widgets"}).text.replace("\n", "")
data.append(" ".join(features.split()))

with open('input.txt', 'w') as file:
    for d in data:
        file.write(d + '\n')
