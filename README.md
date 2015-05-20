# Careerjet API Client Python
Official Python interface to Careerjet's public search API

This is the python client for [Careerjet](http://www.careerjet.com)'s public search API.

## Installation

Install using pip:

    pip install careerjet_api_client

and then to see docs:

    pydoc careerjet_api_client

## Usage

```python
from careerjet_api_client import CareerjetAPIClient

cj  =  CareerjetAPIClient("en_GB");

result_json = cj.search({
                        'location'    : 'london',
                        'keywords'    : 'python',
                        'affid'       : '213e213hd12344552',
                        'user_ip'     : '11.22.33.44',
                        'url'         : 'http://www.example.com/jobsearch?q=python&l=london',
                        'user_agent'  : 'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0'
                      });

```
