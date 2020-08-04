import requests
import openpyxl
from bs4 import BeautifulSoup

wb = openpyxl.Workbook() 
sheet = wb.active
sheet.title ='find_jod'
sheet['A1'] = 'job'

test=requests.get("https://www.liepin.cn/zhaopin/?init=-1&headckid=3e635b4480bb04ac&flushckid=1&dqs=&fromSearchBtn=2&ckid=50daf356668aa0be&subIndustry=&industryType=industry_04&industries=150&siTag=1B2M2Y8AsgTpgAmY7PhCfg%7EfA9rXquZc5IkJpXC-Ycixw&d_sfrom=search_unknown&d_ckId=aedf21f076070969a9ad5b44b65768aa&d_curPage=0&d_pageSize=40&d_headId=4c3684bf118727d27b27cb82496ec84d")
testt= BeautifulSoup(test.text,'html.parser')
job_name = testt.find_all('div',class_='job-info')
company_info=testt.find_all('div',class_='company-info nohover')
for x in range(len(job_name)):
    carrer=[job_name[x].find("a").text[15:]]
    sheet.append(carrer)
wb.save('JOB.xlsx')

import requests
from bs4 import BeautifulSoup
import csv

csv_file = open('demo.csv','w',newline='',encoding='utf-8')
writer = csv.writer(csv_file)
writer.writerow(['job','link','WAGES','CITY','学历','公司'])

wb = openpyxl.Workbook() 
sheet = wb.active
sheet.title ='find_jod'
sheet['A1'] = 'job'
sheet['B1'] ='link'
sheet['C1'] ='WAGES'
sheet['D1'] ='CITY'
sheet['E1'] ='学历'
sheet['F1'] ='公司'
url ="https://www.liepin.cn/zhaopin/?"
for x in range(10):
    params = {
            "init":"-1",
            "headckid":"3e635b4480bb04ac",
            "dqs": "",
            'fromSearchBtn': '2',
            'ckid': '4ee944dac2eef8f7',
            'degradeFlag':'0',
            'subIndustry': '',
            'industryType': 'industry_04',
            'industries': '150',
            'siTag': '1B2M2Y8AsgTpgAmY7PhCfg~Al0RgotvGQ-kRA59YliAuQ',
            'd_sfrom': 'search_unknown',
            'd_ckId': 'c66767d53d4b7fa2e0b41e0d607493eb',
            'd_curPage': '6',
            'd_pageSize': '40',
            'd_headId': '4c3684bf118727d27b27cb82496ec84d',
            'curPage': str(x)
            }
    test = requests.get(url, params=params)
    testt= BeautifulSoup(test.text,'html.parser')
    job_name = testt.find_all('div',class_='job-info')
    company_info=testt.find_all('div',class_='company-info nohover')
    for x in range(len(job_name)):
        carrer=[job_name[x].find("a").text[15:],job_name[x].find('a')['href'],job_name[x].find(class_="text-warning").text,job_name[x].find(class_="area").text,job_name[x].find(class_="edu").text,company_info[x].find("a").text]
        sheet.append(carrer)
wb.save('JOB.xlsx')
