import scrapper


def test_getRawData():
    """unit test for the getRawData function"""
    # prepare
    companyName = "csquared"

    # test
    raw_data = scrapper.getRawData(companyName)

    # assert
    assert len(raw_data) > 100


def test_getEmailsFromFacebookAboutPage():
    """unit test"""
    # prepare
    raw = "something then an email&#064;gmail.com then more data"

    # test
    emails = scrapper.getEmailsFromFacebookAboutPage(raw)

    print(emails)

    # assert
    assert emails == "email@gmail.com"
    


def test_getTheFacebookAboutPage():
    """unit test for getTheFacebookAboutPage"""

    # prepare
    url = "/url?q=https://www.facebook.com/CafeJavas/&sa=U&ved=2ahUKEwiAy4Cuw6PoAhVHKrkGHVYjB9sQtwIwEXoECAEQAQ&usg=AOvVaw1XsBiG_tj2OQCss_f2GYiS"

    # test
    companyID = scrapper.getTheFacebookAboutPage(url)

    print(companyID)
    
    # assert
    assert companyID == "/CafeJavas/"

 
def test_composeFacebookAboutUrl():
    """unit test for composeFacebookAboutUrl"""
    print("test_composeFacebookAboutUrl started")
    # prepare
    companyId = "/CafeJavas/"
    url = "https://www.facebook.com/pg/CafeJavas/about/?ref=page_internal"

    # test
    facebookAboutUrl = scrapper.composeFacebookAboutUrl(companyId)

    # assert
    assert url == facebookAboutUrl
    print("test_composeFacebookAboutUrl ended")


def test_getFacebookAboutPageData():
    """unit test for getFacebookAboutPageData"""

    #prepare
    faceBookPageUrl = "https://www.facebook.com/pg/CafeJavas/about/?ref=page_internal"

    #test
    data = scrapper.getFacebookAboutPageData(faceBookPageUrl)

    #assert
    # look out for info&#064;cafejavas.co.ug
    assert "info&#064;cafejavas.co.ug" in data


def test_writeCompanyContact():
    """unit test for writeCompanyContact"""

    #prepare
    companyName = "Cafe Javas"
    companyEmail = "info@cafejavas.co.ug"
    expected_data = f"{companyEmail}:{companyName}"

    #test
    scrapper.writeCompanyContact(companyName, companyEmail)

    # prepare
    with open("contactinfo.txt", "r") as contactinfo:
        for companyinfo in contactinfo:
            actual_data = companyinfo

    #assert
    assert expected_data == actual_data

def test_getLinksFromRawData():

    """unit test for getLinksFromRawData"""

    #prepare
    # https://www.w3schools.com/html/html_intro.asp
    # https://www.w3schools.com/html/html_links.asp
    
    multiline_markup = """
    <!DOCTYPE html>
<html>
<body>

<h2>The target Attribute</h2>

<a href="https://www.facebook.com" target="_blank">Visit our HTML tutorial!</a> 

<p>If you set the target attribute to "_blank", the link will open in a new browser window or tab.</p>

</body>
</html>"""
    markup = "https://www.facebook.com"

    #test

    facebookhref = scrapper.getLinksFromRawData(multiline_markup)

    #assert

    assert markup in facebookhref

def test_readCompanyName():

    #test

    scrapper.readCompanyName(filename="companies.txt")