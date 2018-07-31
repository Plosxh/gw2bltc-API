import json
import requests


class Bltc(object):
    def __init__(self, apiKey):
        self.url = "https://api.guildwars2.com/v2/"
        self.apikey = apiKey

    def get_gem_exchange(self):
        """Get amount a coins requiered for one gem and for 100 gems"""
        url = self.url+"commerce/exchange/gems?quantity=10000&lang=en"
        req = requests.get(url)
        return json.loads(req.content)

    def get_coin_exchange(self):
        """Get the amout of coins traded for 1 gems the number of gems traded for 10000 coins"""
        url = self.url+"commerce/exchange/coins?quantity=10000&lang=en"
        req = requests.get(url)
        return json.loads(req.content)

    def get_delivery(self):
        """" Return coins and items waiting at the BLTC """
        url = self.url +"commerce/delivery?access_token="+self.apikey
        req = requests.get(url)
        return json.loads(req.content)

    def get_current_buy_transaction(self):
        """" Return open buy orders """
        url = self.url +"commerce/transaction/current/buys?access_token="+self.apikey
        req = requests.get(url)
        return json.loads(req.content)

    def get_history_buy_transaction(self):
        """" Return closed buy orders """
        url = self.url +"commerce/transaction/history/buys?access_token="+self.apikey
        req = requests.get(url)
        return json.loads(req.content)

    def get_current_sell_transaction(self):
        """" Return open sell orders """
        url = self.url +"commerce/transaction/current/sells?access_token="+self.apikey
        req = requests.get(url)
        return json.loads(req.content)

    def get_history_sell_transaction(self):
        """" Return return closed sell orders """
        url = self.url +"commerce/transaction/history/sells?access_token="+self.apikey
        req = requests.get(url)
        return json.loads(req.content)

    def get_exchange(self):
        """ Return avaible exchange"""
        url = self.url +"commerce/exchange"
        req = requests.get(url)
        return json.loads(req.content)

    def get_item(self,items):
        """Get Items infos."""
        url = self.url+"items?ids="
        for item in items:
            url += str(item["id"])+","
        req = requests.get(url)
        items = json.loads(req.content)
        return items

    def get_prices(self,items):
        """Get Items Price"""
        url= self.url+"commerce/prices?ids="
        for item, key in items.items():
            url += str(key["id"])+","
        req = requests.get(url)
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
        req = requests.get(url)
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
