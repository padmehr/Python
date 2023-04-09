from bs4 import BeautifulSoup
import requests

'''with open('home.html', 'r') as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content, 'lxml')
    #print(soup.prettify())
    html_tags = soup.find_all('h1')
    #print(html_tags)
    for tag in html_tags:
        print(tag.text)'''
###
###
###
'''      
url = 'https://www.meteo.it/meteo/roma-oggi-58091'
home_page = requests.get(url)
soup = BeautifulSoup(home_page.text, 'lxml')
img_weather = soup.find_all('img', alt = True)
alt_weather = []
for img in img_weather:
    alt = str(img['alt'])
    if alt != 'None':
        alt_weather.append(alt)
 
print('\n'.join(alt_weather))''' 
###
###
###
'''url = 'https://jobinja.ir/jobs?filters%5Bkeywords%5D%5B%5D=python&filters%5Blocations%5D%5B%5D=&filters%5Bjob_categories%5D%5B%5D=&b='
page = requests.get(url).text
soup = BeautifulSoup(page, 'lxml')
job = soup.find('div', class_ = 'o-listView__itemWrap c-jobListView__itemWrap u-clearFix')
company_name = job.find('li', class_ = 'c-jobListView__metaItem')
company = company_name.find('span').text

print(company)
'''
###
###
###
url = 'https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=python&txtLocation=&cboWorkExp1=-1'
page = requests.get(url).text
soup = BeautifulSoup(page, 'lxml')
job_list = soup.find('ul', class_ = 'ui-content search-result')
jobs = job_list.find_all('li')
for job in jobs:
    
    company_name = job.find('h4').text
    skills = job.find('div', class_ = 'srp-keyskills').text.replace(' ' and '\n', '')
    published_date = job.find('span', class_ = 'posting-time').text
    
    #print(published_date)

    print(f'''
         Company Name: {company_name}
         Required Skills: {skills}''')
    
    print('')