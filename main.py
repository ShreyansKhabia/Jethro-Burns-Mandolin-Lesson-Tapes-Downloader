import requests
import os
from bs4 import BeautifulSoup
import string
import random

randnum=5


URL = "https://robcoleman.com/jethro/index.html"
print('')
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')


folname = []
folder = soup.find_all('td', class_="heading")
parent_dir = "D:\Music\Dada\Python"
for f in folder:
    heading = f.text.replace(' ', '').replace('\n', '')
    if 'Disc' in heading:
        mypath = os.path.join(parent_dir, heading)
        if mypath not in folname:
            folname.append(mypath)
        print(mypath)
        try:
            os.makedirs(mypath)
            print(f'{heading} folder created\n')
        except OSError as error:
            print(error)
            print("wtf man\n")
            
print(folname)

tags = soup.find_all('a')
i = 1
for tag in tags:
    name = tag.text
    if name == '?':
        res = ''.join(random.choices(string.ascii_uppercase +
                                 string.digits, k=randnum))
        name = res

    link = "https://robcoleman.com/jethro/" + tag['href']

    if 'Disc' not in name and 'CoMando' not in name and 'rob@robcoleman.com' not in name and '@robcolemanmpls' not in name and 'PDF' not in name and 'Adobe' not in name:
        if(i<=38):
            mydir=folname[0]
        if(i>38 and i<=80):
            mydir=folname[1]
        if(i>80 and i<=101):
            mydir=folname[2]
        if(i>101 and i<=141):
            mydir=folname[3]
        if(i>141 and i<=175):
            mydir=folname[4]
        if(i>175 and i<=205):
            mydir=folname[5]
        if(i>205):
            mydir=folname[6]

        finalpath= os.path.join(mydir, name+'.mp3')
        req = requests.get(link)
        mp3= open(finalpath,'wb')
        mp3.write(req.content)

        print(f"{i} {name}: {link} has been downloaded")
        i = i + 1
        print('')
