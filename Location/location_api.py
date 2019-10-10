import requests
from Location.constants_api import *


class LocationApi():

    def __init__(self):
        adress = input("Введите наименование лакации где будет проводиться БОЙ !!!!\n")
        self.get_coordinates_by_address(adress)

    def get_google_key(self):
        data = open(GOOGLE_API_GEOCODE_KEY, mode='r', encoding='utf8')
        return data.read()

    def get_location(self, address=None, coords=None):
        data = {
            'key': self.get_google_key()
        }
        if address:
            data['address'] = address
        if coords:
            data['latlng'] = coords
        response = requests.get(GOOGLE_API_GEOCODE_URL, data)
        return response.json()

    def get_coordinates_by_address(self, address):
        """Метод возвращает координаты локации по ЗАПРОСУ"""
        coordinates = self.get_location(address)
        print('Запрос по адрессу:  {}\nОтвет - Координаты:\n    lat = {}\n    lng = {}\n'.format
              (coordinates['results'][0]['formatted_address'],
               coordinates['results'][0]['geometry']['location']['lat'],
               coordinates['results'][0]['geometry']['location']['lng']))

    def get_address_by_coordinates(self, *args):
        """Метод возвращат данные локации по координатам"""
        if type(args[0]) == list:
            lat = args[0][0]
            lng = args[0][1]
        else:
            lat = args[0]
            lng = args[1]
        address = self.get_location('{},{}'.format(lat, lng))
        print('Запрос по координатам: lat = {} lng = {}\nОтвет - Локация: {}\n'.format
              (lat, lng, address['results'][0]['formatted_address']))


# location = LocationApi()
# location.get_coordinates_by_address('Derybasivska Street, 11')
# location.get_address_by_coordinates([46.483955, 30.737055])

