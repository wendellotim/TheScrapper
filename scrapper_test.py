import scrapper


def test_getRawData():
    """unit test for the getRawData function"""
    # prepare
    companyName = "csquared"

    # test
    raw_data = scrapper.getRawData(companyName)

    # assert
    assert len(raw_data) > 100

def test_extractEmailsFromString():
    """unit test"""
    raw = "something then an email@gmail.com then more data"
    emails = scrapper.extractEmailsFromString(raw)
    print(emails)