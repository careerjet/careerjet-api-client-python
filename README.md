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

cj = CareerjetAPIClient("en_GB");

result_json = cj.search({'affid':'q3123','user_ip':'192.168.0.40','url':'http://www.example.com/test_page','user_agent':'Firefox 30','locale_code':'es_ES'});
```
