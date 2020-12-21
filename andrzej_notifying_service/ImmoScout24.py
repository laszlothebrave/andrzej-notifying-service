import oauthlib
from requests_oauthlib import OAuth1Session

from andrzej_notifying_service import Advertisement
import requests


class ImmoScout24:
    def __init__(self):
        pass

    def convert_into_advertisement(self, json)->Advertisement:
        return Advertisement()

    def request(self):
        immoscout_api = OAuth1Session('myKey',
                                      client_secret='mysecret')
        url = 'https://rest.immobilienscout24.de/restapi/api/offer/v1.0/user/me/realestate?publishchannel=IS24'
        r = immoscout_api.get(url)
        print(r)

if __name__ == '__main__':
    object=ImmoScout24()
    object.request()
