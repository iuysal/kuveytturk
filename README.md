

A Python wrapper for the Kuveyt Turk API!
======

[![Build Status](http://img.shields.io/travis/iuysal/kuveytturk/master.svg?style=flat)](https://travis-ci.org/iuysal/kuveytturk)
[![Version](http://img.shields.io/pypi/v/kuveytturk.svg?style=flat)](https://pypi.python.org/pypi/kuveytturk)

This library provides a Python interface for the [Kuveyt Turk API](https://developer.kuveytturk.com.tr/#/). Making a request to Kuveyt Turk API requires a valid access token and signature. OAuth procedures are eased and signature generation is automated in this library.

Installation
------------
The easiest way to install the latest version
is by using pip/easy_install to pull it from PyPI:

    $ pip install kuveytturk

or

    $ easy_install kuveytturk

You may also use Git to clone the repository from
GitHub and install it manually:

    git clone https://github.com/iuysal/kuveytturk.git
    cd kuveytturk
    python setup.py install

Python 3.6 is supported.

Quick Start
------------

First, import the API and OAuthHandler classes. 

    from kuveytturk.api import API
    from kuveytturk.auth import OAuthHandler
    
Then, 

    CLIENT_ID = '<Your OAuth Client ID>'
    CLIENT_SECRET = '<Your OAuth Client Secret>'
    REDIRECT_URI = '<Your OAuth Redirect URI>'
    PRIVATE_KEY = '<Your Private Key>'
    
Create an authentication handler with your credentials

    auth = OAuthHandler(CLIENT_ID, CLIENT_SECRET, PRIVATE_KEY, REDIRECT_URI)
    
Then create an API instance using this authentication handler

    api = API(auth)
    
Now, we're ready to make an API request!

    response = api.test_customer_list()
    
    for customerId in response.value:
        print(customerId)
        
In the examples folder, there are a variety of examples you can check out and benefit from. There is even an rsa key generator you can use to create your applications public and private keys.

Development
---
### Getting Started

Assuming that you have Python and virtualenv installed, set up your environment and install the required dependencies like this instead of the `pip install kuveytturk` defined above:

    $ git clone https://github.com/iuysal/kuveytturk.git
    $ cd kuveytturk
    $ virtualenv venv
    ...
    $ . venv/bin/activate
    $ pip install -r requirements.txt
    $ pip install -e .

### Running Tests

You can run tests in all supported Python versions using tox. By default, it will run all of the unit tests, but you can also specify your own nosetests options. Note that this requires that you have all supported versions of Python installed, otherwise you must pass -e or run the nosetests command directly:

    $ tox
    $ tox -- tests/test_api.py
    $ tox -e py27, py36 -- tests/
    
You can also run individual tests with your default Python version:

    $ nosetests tests/test_auth.py

Getting Help
---

Please, ask a question on [Stack Overflow](https://stackoverflow.com) and tag it with [kuveytturk](https://stackoverflow.com/questions/tagged/kuveytturk)