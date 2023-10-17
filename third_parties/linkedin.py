import requests
from config import settings

def scrape_linkedin(linkdin_url):
    api_key = settings.proxycurl_api
    headers = {'Authorization': 'Bearer ' + api_key}
    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    params = {'linkedin_profile_url': linkdin_url}

    response = requests.get(api_endpoint,
                        params=params,
                        headers=headers)