import requests

from bs4 import BeautifulSoup

import re


def readCompanyName(filename="companies.txt"):
    with open(filename, "r") as companies:
        for company in companies:
            return company


def getRawData(companyName):
    '''collects the HTML data '''

    searchUrl = f'https://www.google.com/search?q={companyName}'
    data = requests.get(searchUrl)
    response = data.text
    return response


def getLinksFromRawData(YOUR_MARKUP):
    ''' The function gets the facebook links of the company '''

    soup = BeautifulSoup(YOUR_MARKUP, "html.parser")

    for link in soup.findAll('a', attrs={'href': re.compile("a")}):
        href = link.get('href')
        if "facebook.com" in href:
            return href


def getTheFacebookAboutPage(href):
    ''' the function collects the facebook about page data '''

    rawFacebookLink = href.strip('')
    finder = rawFacebookLink.find('&')
    facebookLink = slice(31, finder)
    return rawFacebookLink[facebookLink]

def composeFacebookAboutUrl(companyFacebookId):
    faceBookAboutPageUrl = f'https://www.facebook.com/pg{companyFacebookId}about/?ref=page_internal'
    return faceBookAboutPageUrl


def getFacebookAboutPageData(faceBookAboutPageUrl):
    
    aboutPageData = requests.get(faceBookAboutPageUrl)
    return aboutPageData.text


def getEmailsFromFacebookAboutPage(facebookAboutPageData):

    
    rawEmail = re.findall(r"\w+[.|\w]\w+&#064;\w+[.]\w+[.|\w+]\w+", facebookAboutPageData)
    
    email = rawEmail[0]

    companyEmail = email.replace("&#064;","@")

    return companyEmail

def writeCompanyContact(companyEmail, companyName):

    companyName = companyName.strip()
    info = f"{companyName}:{companyEmail}"
    contact = info.strip()
    with open("contactinfo.txt", "w") as contactinfo:
        contactinfo.write(contact)