import scrapper

companyName = input("Enter company name: ")

page = scrapper.getsRawData(companyName)

aboutLink = scrapper.getsLinksFromRawData(page)

scrapper.getsLinksFromRawData(page)

scrapper.getsTheFacebookAboutPage(aboutLink, companyName)

facebookHtml = scrapper.getsTheFacebookAboutPage(aboutLink, companyName)

scrapper.getsEmailsFromFacebookAboutPage(facebookHtml)

