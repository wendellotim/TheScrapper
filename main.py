import scrapper

companyName = scrapper.readCompanyName()

page = scrapper.getRawData(companyName)

aboutLink = scrapper.getLinksFromRawData(page)

scrapper.getLinksFromRawData(page)

scrapper.getTheFacebookAboutPage(aboutLink)

companyFacebookId = scrapper.getTheFacebookAboutPage(aboutLink)

scrapper.composeFacebookAboutUrl(companyFacebookId)

faceBookAboutPageUrl = scrapper.composeFacebookAboutUrl(companyFacebookId)

scrapper.getFacebookAboutPageData(faceBookAboutPageUrl)

facebokAboutPageData = scrapper.getFacebookAboutPageData(faceBookAboutPageUrl)

scrapper.getEmailsFromFacebookAboutPage(facebokAboutPageData)

companyEmail = scrapper.getEmailsFromFacebookAboutPage(facebokAboutPageData)

scrapper.writeCompanyContact(companyEmail, companyName)
