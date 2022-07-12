from bs4 import BeautifulSoup
import requests
import csv
from itertools import zip_longest

#/home/rasmesxiii/Documents/forproject.csv

job_name = []
job_skills = []

# use requests to fetch URL
web = requests.get("https://wuzzuf.net/search/jobs/?q=django+developer&a=navbg")

# save page content
source = web.content

soup = BeautifulSoup(source, 'lxml') # require 2 prameter(web source, lxml module) secrch for lxml to know what does it do


job_name = soup.find_all("a", {"class":"css-o171kl"})
job_skills = soup.find_all('a',{'class':'css-o171kl'})
company = soup.find_all()
location = soup.find_all()
# print(job_name)

for i in range(len(job_name)) :
    job_name.append(job_name[i].text)
    job_skills.append(job_skills[i].text)

    print(job_name)

    # print(f'{job_name} required skills : \n {job_skills}')

# for job in job_skills :

#     print(f'{job} ')


