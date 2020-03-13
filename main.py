import scrapper

companyName = scrapper.readCompanyName()

page = scrapper.getRawData(companyName)

aboutLink = scrapper.getLinksFromRawData(page)

scrapper.getLinksFromRawData(page)

scrapper.getTheFacebookAboutPage(aboutLink, companyName)

facebookHtml = scrapper.getTheFacebookAboutPage(aboutLink, companyName)

scrapper.getEmailsFromFacebookAboutPage(facebookHtml)
