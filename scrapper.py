import requests

from bs4 import BeautifulSoup

import re


def getRawData(companyName):
    '''collects the HTML data '''

    searchUrl = f'https://www.google.com/search?q={companyName}'
    data = requests.get(searchUrl)
    response = data.text
    return response


def getsLinksFromRawData(YOUR_MARKUP):
    ''' The function gets the facebook links of the company '''

    soup = BeautifulSoup(YOUR_MARKUP, "html.parser")

    for link in soup.findAll('a', attrs={'href': re.compile("a")}):
        href = link.get('href')
        if "facebook.com" in href:
            return href


def getsTheFacebookAboutPage(href, companyName):
    ''' the function collects the facebook about page data '''

    rawFacebookLink = href.strip('')
    facebookLink = slice(7, 31)
    faceBookAboutPageUrl = f'{rawFacebookLink[facebookLink]}/pg/{companyName}/about/?ref=page_internal'
    aboutPageData = requests.get(faceBookAboutPageUrl)
    return aboutPageData.text


def getsEmailsFromFacebookAboutPage(facebookHtml):

    soup = BeautifulSoup(facebookHtml, "html.parser")

    companyEmails = []
    emails = soup.findAll(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    print(emails)

    # emails = re.findall(r"\w+[.|\w]\w+@\w+[.]\w+[.|\w+]\w+", facebookHtml)
    # print(emails)

    # print(facebookHtml.index("@"))

    for email in emails:
        companyEmails.append(email)
    print(companyEmails)


def extractEmailsFromString(string):
    """extracts email addresses from a string"""
    emails = re.findall(r"\w+[.|\w]\w+@\w+[.]\w+[.|\w+]\w+", string)
    return emails
