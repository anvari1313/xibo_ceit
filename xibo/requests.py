import requests


xibo_cms_domain = 'http://sinage.ceit.aut.ac.ir'

client_id = 'T6qH5Kth9pXasnlAg9WOYCeYH9w7lUpqc5EM3cIx'

client_secret = 'jaTZ09YERMvs2Ecf9WEsJtxXrW0g71WMvc' \
                'ISvqM4gMAkDVDPzE4NE72AzKSFZ4HoAu3p' \
                'Rw3NrO3k1B1aKlwyVvSmLEIpXKTKRQg1u2' \
                'k19dkKYfjPBLVZHZkeIV36oJQurqEJ2TEd' \
                'UV3yJ3mndzuK66qI4oO1qJ2MQMKgaxjJk9' \
                'NjEhszUvZmPhch3qGpWwOIEkf835DvwQxy' \
                '042ucItGf3CB19jPLjygWMwwYcAMnpGkQL' \
                'rhcxUZQ6PuUX1IA2'

api_routes = {
    'authenticate': '/api/authorize/access_token',
    'clock': '/api/clock'
}


def authenticate():
    url = xibo_cms_domain + api_routes['authenticate']
    payload = {'client_id': client_id, 'client_secret': client_secret, 'grant_type': 'client_credentials'}
    r = requests.post(url=url, data=payload)

    auth = r.json()
    return {'Authorization': auth['token_type'] + ' ' + auth['access_token']}


def get_time():
    headers = authenticate()
    url = xibo_cms_domain + api_routes['clock']
    r = requests.get(url=url, headers=headers)

    return r.json()
