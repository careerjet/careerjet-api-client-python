
import platform
import pkg_resources
import requests
import json
from careerjet_api_client.constants import Constants
#Note: urlparse is renamed to urllib.parse in Python 3
from urllib.parse import urlparse

class CareerjetAPIClient(object):

	def __init__(self, locale_code="en_GB"):
		"""
		locale - POSIX locale that determines which Careerjet site to use. Each locale corresponds to an existing Careerjet site and 
		determines which language job-related information is returned as well as which default location filter is used.

		For example, if your users are primarily Dutch-speaking Belgians, you should use "nl_BE".

		First two letters : ISO 639-1 alpha-2 language code
		See http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes

		Last two letters : ISO 3166-1 alpha-2 country code
		See http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2

		For a list of all available locales see http://www.careerjet.co.uk/partners/api/locale/.

		"""
		if not locale_code:
			self.locale_code = "en_GB"
		elif locale_code in Constants.LOCALES:
			self.locale_code = locale_code
		else:
			raise Exception('Locale '+locale_code+' not supported')

	def search(self,search_params):
		"""
		search_params - Dictionary that contains the search params in key/value form.

	 	Mandatory search params:

	    	affid        	: Affiliate identifier provided by Careerjet if you have a Careerjet partner account.
	                     		You can open a careerjet partner account here http://www.careerjet.co.uk/partners/
	                      		Default: none
	     	user_ip      	: IP address of the end-user to whom the search results will be displayed

	     	user_agent   	: User agent of the end-user's browser

	     	url          	: URL of page that will display the search results


	 	Available search params: All params below have default values and are not mandatory

	     	keywords     	: Keywords to match either title, content or company name of job offer
	                      		Examples: 'perl developer', 'ibm', 'software architect'
	                      		Default : none
	 
	     	location     	: Location of requested job postings.
	                      		Examples: 'London' , 'Yorkshire', 'France' 
	                      		Default: country specified by country code
	 
	     	sort         	: Type of sort. This can be:
		                       'relevance'  - sorted by decreasing relevancy (default)
		                       'date'       - sorted by decreasing date
		                       'salary'     - sorted by decreasing salary
	 
	     	start_num    	: Position of returned job postings within the entire result space.
	                      		This should be a least 1 but not more than the total number of job offers.
	                      		Default : 1
	 
	     	pagesize     	: Number of returned results
	                      		Default : 20
                                        Maximum : 100

	     	page 		: Page number of returned job postings within the entire result space.
	                      		This can be used instead of start_num. The minimum page number is 1.
	                      		The maximum number of pages is given by $result->{'pages'}
	                      		If this value is set, it overrides start_num.
	 
	     	contracttype 	: Selected contract type. The following codes can be used: 
		                       'p'    - permanent
		                       'c'    - contract
		                       't'    - temporary
		                       'i'    - training
		                       'v'    - voluntary
		                      	Default: none (all contract types)
	     
	     	contractperiod 	: Selected contract period. The following codes can be used: 
		                       'f'     - full time
		                       'p'     - part time
		                      	Default: none (all contract periods)
		"""
		for field in search_params:
			if not field in Constants.ALLOWED_FIELDS:
				raise Exception('Unknown param key \''+ field +'\'')

		for field in Constants.MANDATORY_FIELDS:
			if not field in search_params or not search_params[field]:
				raise Exception('Mandatory param key \''+ field +'\' missing')

		if 'locale_code' not in search_params:
			search_params['locale_code'] = self.locale_code

		if search_params['locale_code'] not in Constants.LOCALES:
			raise Exception('Locale '+search_params['locale_code']+' not supported')

		referer_uri = urlparse(search_params.pop('url'))
		if referer_uri.scheme != 'http' and referer_uri.scheme != 'https':
			raise Exception('Invalid param url \''+ search_params['url'] +'\'')

		user_agent = 'careerjet-api-client-v' + pkg_resources.require("careerjet_api_client")[0].version +'-python-v'+platform.python_version()

		try:
			response  = requests.get(Constants.API_URL + '/search', headers={ 'user-agent':user_agent ,'referer' : referer_uri.geturl() } ,params=search_params)
		except Exception as e:
			raise e

		#If we made a bad request (a 4XX client error or 5XX server error response), we can raise it with 
		response.raise_for_status()

		try:
			return json.loads(response.text)
		except Exception as e:
			raise e
