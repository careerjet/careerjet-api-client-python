# Careerjet API Client Python
Official Python interface to [Careerjet](http://www.careerjet.com)'s  public search API

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
### Mandatory Search Params

* `affid`      : Affiliate ID provided by Careerjet. Requires to open a Careerjet partner account (http://www.careerjet.co.uk/partners).
* `user_ip`    : IP address of the end-user to whom the search results will be displayed.  
* `user_agent` : User agent of the end-user's browser.
* `url`        : URL of page that will display the search results

### Search Params

Please note that each parameter is optional.

* `keywords`: Keywords to match the title, content or company name of a job offer

* `location`: Location of requested jobs

* `sort`: Sort type. This can be: `relevance` (default) — sorted by decreasing relevancy, `date` — sorted by decreasing date and `salary` — sorted by decreasing salary.

* `start_num`: Position of returned job postings within the entire result space. Should be >= 1 and <= Number of hits.

* `pagesize`: Number of jobs returned in one call.

* `page`: Page number of returned jobs within the entire result space. Should be >=1. If this value is set, it overrides `start_num`.

* `contracttype`: Selected contract type.`p` — permanent job, `c` — contract, `t` — temporary, `i` — training, `v` — voluntary, none — all contract types.

* `contractperiod`: Selected contract period. `f` — full time, `p` — part time, none — all contract periods.

### Locale code

The locale code needs to be supplied in the contructor of the API client. It defines the default location as well as the language in
which the search results are returned. Each locale corresponds to a Careerjet site.

The default is 'en_GB'.

For a list of all available locales see http://www.careerjet.co.uk/partners/api/locale/.
