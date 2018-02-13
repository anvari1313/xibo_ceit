import requests
import dotenv
from .exception import CanNotAuthorize

xibo_cms_domain = 'http://xibo.ceit.aut.ac.ir'

client_id = dotenv.get('CLIENT_ID')

# client_secret = 'jaTZ09YERMvs2Ecf9WEsJtxXrW0g71WMvc' \
#                 'ISvqM4gMAkDVDPzE4NE72AzKSFZ4HoAu3p' \
#                 'Rw3NrO3k1B1aKlwyVvSmLEIpXKTKRQg1u2' \
#                 'k19dkKYfjPBLVZHZkeIV36oJQurqEJ2TEd' \
#                 'UV3yJ3mndzuK66qI4oO1qJ2MQMKgaxjJk9' \
#                 'NjEhszUvZmPhch3qGpWwOIEkf835DvwQxy' \
#                 '042ucItGf3CB19jPLjygWMwwYcAMnpGkQL' \
#                 'rhcxUZQ6PuUX1IA2'

client_secret = dotenv.get('CLIENT_SECRET')

api_routes = {
    'authenticate': '/api/authorize/access_token',
    'clock': '/api/clock',
    # 'display': {
    #     'all': '/api/display'
    # }
    'display': '/api/display'
}


def authenticate():
    url = xibo_cms_domain + api_routes['authenticate']
    payload = {'client_id': client_id, 'client_secret': client_secret, 'grant_type': 'client_credentials'}
    r = requests.post(url=url, data=payload)

    auth = r.json()
    return {'Authorization': auth['token_type'] + ' ' + auth['access_token']}


# def get_time():
#     headers = authenticate()
#     url = xibo_cms_domain + api_routes['clock']
#     r = requests.get(url=url, headers=headers)
#     print(dotenv.get('CLIENT_ID'))
#     return r.json()


class XiboRest:
    request_headers = {}

    @staticmethod
    def __authenticate():
        url = xibo_cms_domain + api_routes['authenticate']
        payload = {'client_id': client_id, 'client_secret': client_secret, 'grant_type': 'client_credentials'}
        r = requests.post(url=url, data=payload)
        print('Authenticating')
        auth = r.json()
        XiboRest.request_headers['Authorization'] = auth['token_type'] + ' ' + auth['access_token']

    @staticmethod
    def get_time():
        print('Getting time')
        url = xibo_cms_domain + api_routes['clock']
        r = requests.get(url=url, headers=XiboRest.request_headers)
        if r.status_code / 100 != 2:
            XiboRest.__authenticate()
            r = requests.get(url=url, headers=XiboRest.request_headers)
            if r.status_code == 401:
                raise CanNotAuthorize

        print(r.status_code)
        return r.json()

    @staticmethod
    def get_all_displays():
        url = xibo_cms_domain + api_routes['display']
        r = requests.get(url=url, headers=XiboRest.request_headers)
        if r.status_code / 100 != 2:
            XiboRest.__authenticate()
            r = requests.get(url=url, headers=XiboRest.request_headers)

        print(r.status_code)
        return r.json()
