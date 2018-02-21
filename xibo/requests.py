import requests
import dotenv
from .exception import CanNotAuthorize

xibo_cms_domain = dotenv.get('XIBO_CMS_SERVER_PROTOCOL') + '://' + dotenv.get('XIBO_CMS_DOMAIN') + ':' + str(dotenv.get('XIBO_CMS_SERVER_PORT')) + dotenv.get('XIBO_CMS_ROOT_ROUTE', '')

client_id = dotenv.get('XIBO_CLIENT_ID')

client_secret = dotenv.get('XIBO_CLIENT_SECRET')

api_routes = {
    'authenticate': '/api/authorize/access_token',
    'clock': '/api/clock',
    'display': {
        'all': '/api/display'
    },
    'layout': {
        'all': '/api/layout'
    },
    'widget': {
        'all': '/api/playlist/widget',
        'update': '/api/playlist/widget/%d'
    }
}


def authenticate():
    url = xibo_cms_domain + api_routes['authenticate']
    payload = {'client_id': client_id, 'client_secret': client_secret, 'grant_type': 'client_credentials'}
    r = requests.post(url=url, data=payload)

    auth = r.json()
    return {'Authorization': auth['token_type'] + ' ' + auth['access_token']}


class XiboRest:
    request_headers = {}

    @staticmethod
    def __authenticate():
        url = xibo_cms_domain + api_routes['authenticate']
        print('Url is : ' + url)
        payload = {'client_id': client_id, 'client_secret': client_secret, 'grant_type': 'client_credentials'}
        r = requests.post(url=url, data=payload)
        print('Authenticating')
        auth = r.json()
        print(auth)
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
        url = xibo_cms_domain + api_routes['display']['all']
        r = requests.get(url=url, headers=XiboRest.request_headers)
        if r.status_code / 100 != 2:
            XiboRest.__authenticate()
            r = requests.get(url=url, headers=XiboRest.request_headers)

        print(r.status_code)
        return r.json()

    @staticmethod
    def get_all_layouts():
        url = xibo_cms_domain + api_routes['layout']['all']
        r = requests.get(url=url, headers=XiboRest.request_headers)
        if r.status_code / 100 != 2:
            XiboRest.__authenticate()
            r = requests.get(url=url, headers=XiboRest.request_headers)

        return r.json()

    @staticmethod
    def get_all_widgets():
        url = xibo_cms_domain + api_routes['widget']['all']
        r = requests.get(url=url, headers=XiboRest.request_headers)
        if r.status_code / 100 != 2:
            XiboRest.__authenticate()
            r = requests.get(url=url, headers=XiboRest.request_headers)

        return r.json()

    @staticmethod
    def update_widget(widget_id, text):
        url = (xibo_cms_domain + api_routes['widget']['update']) % widget_id
        print('Update url is : ' + url)
        payload = {'text': text}
        r = requests.put(url=url, data=payload, headers=XiboRest.request_headers)
        if r.status_code / 100 != 2:
            XiboRest.__authenticate()
            r = requests.put(url=url, data=payload, headers=XiboRest.request_headers)

        print(r.status_code)
        return r.json()
