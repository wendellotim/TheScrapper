import scrapper


def test_getRawData():
    """unit test for the getRawData function"""
    # prepare
    companyName = "csquared"

    # test
    raw_data = scrapper.getRawData(companyName)

    # assert
    assert len(raw_data) > 100
