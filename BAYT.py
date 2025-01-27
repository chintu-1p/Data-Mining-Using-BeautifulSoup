import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    url = f'https://www.bayt.com/en/india/jobs/?page={page}&_gl=1*78vbkv*_up*MQ..*_ga*OTgwOTYzNC4xNzM3OTA4MjUz*_ga_1NKPLGNKKD*MTczNzkwODI1Mi4xLjAuMTczNzkwODI1Mi4wLjAuMA..'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('li', class_='has-pointer-d')
    for item in divs:
        title = item.find('a').text.strip() if item.find('a') else "No Title"
        company = item.find('div', class_='t-nowrap').text.strip() if item.find('div', class_='t-nowrap') else "No Company"
        location = item.find('div', class_='t-mute t-small').text.strip() if item.find('div', class_='t-mute t-small') else "No Location"
        job_type_element = item.find('dt', class_='p0 m20r jb-label-remote')
        job_type = job_type_element.text.strip() if job_type_element else "Not Remote"
        date_posted = item.find('div', class_='jb-date col p0x p0t t-mute').text.strip() if item.find('div', class_='jb-date col p0x p0t t-mute') else "No Date Posted"
        description_element = item.find('div', class_='jb-descr m10t t-small')
        job_description = description_element.text.strip() if description_element else "No Description"
        link_element = item.find('a', class_='btn is-small')
        link = link_element['href'] if link_element else "No Link"
        job = {
            'Title': title,
            'Company': company,
            'Location': location,
            'Job Type': job_type,
            'Date Posted': date_posted,
            'Description': job_description,
            'Application Link': link
        }
        joblist.append(job)

joblist = []

for i in range(1, 11):
    c = extract(i)
    transform(c)

df = pd.DataFrame(joblist)
output_filename = 'ChintuGouda_Bayt_Output.xlsx'
df.to_excel(output_filename, index=False)

print(f"Data saved to {output_filename}")
