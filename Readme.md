# Scrapper

TODO: Given a given list of company names, the Scrapper gets the google search results of the company name.
In the results, it picks the facebook links  and goes to the  face book about page of the company.
From the facebook about page it picks the comapnies email addresses and prints them.

## Running tests

Tests

```shell
pytest
```

Running tests and collecting test coverage

```shell
pytest -s -vv --cov-report term --cov=./ ./
```
