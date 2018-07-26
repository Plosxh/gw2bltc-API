import json
import requests


class Bltc(object):
    def __init__(self, apiKey):
        self.url = "https://api.guildwars2.com/v2/"
        self.apikey = apiKey

    def get_item(self,items):
        """Get Items infos."""
        url = self.url+"items?ids="
        for item in items:
            url += str(item["id"])+","
        req = requests.get(url+"&lang=fr")
        items = json.loads(req.content)
        return items

    def get_prices(self,items):
        """Get Items Price"""
        url= self.url+"commerce/prices?ids="
        for item, key in items.items():
            url += str(key["id"])+","
        req = requests.get(url+"&lang=fr")
        prices =  json.loads(req.content)
        return prices

    def get_item_listing(self,item):
        """Get Items Price Listing"""
        url= self.url+"commerce/listings/"
        req = requests.get(url+str(item))
        prices =  json.loads(req.content)
        return prices

    def get_prices_list(self,items):
        """Get Items Price"""
        url= self.url+"commerce/prices?ids="
        for item in items:
            url += str(item)+","
        req = requests.get(url+"&lang=fr")
        prices =  json.loads(req.content)
        return prices

    def get_price(self,item):
        """Get Items Price"""
        url= self.url+"commerce/prices/"+str(item)
        req = requests.get(url)
        print(req)
        prices =  json.loads(req.content)
        return prices

    def get_ecto_price(self):
        """Get Items Price"""
        req = requests.get(self.url+"commerce/prices/19721")
        prices =  json.loads(req.content)
        # print(prices)
        return prices["sells"]["unit_price"]
