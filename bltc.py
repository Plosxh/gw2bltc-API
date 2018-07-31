import json
import requests
from urllib.parse import urljoin


def format_price(value, suffixes=("c", "s", "g")):
    parts = []
    for suffix in suffixes[:-1]:
        parts.append("{}{}".format(value % 100, suffix))
        value //= 100
        if not value:
            break
    else:
        parts.append("{}{}".format(value, suffixes[-1]))
    return " ".join(reversed(parts))


class Bltc(object):

    BASE_URL = "https://api.guildwars2.com/v2/"
    ECTO_ID = 19721

    def __init__(self, api_key):
        self.api_key = api_key

    def _request(self, url, params=None, authenticated=False):
        if params is None:
            params = {}
        if authenticated:
            params["access_token"] = self.api_key
        return requests.get(urljoin(self.BASE_URL, url), params=params).json()

    def get_gem_exchange(self, quantity=100):
        """Get the number of coins you get for the specified quantity of gems."""
        return self._request("commerce/exchange/gems", params=dict(quantity=quantity))

    def get_coin_exchange(self, quantity=10000):
        """Get the number of gems you get for the specified quantity of coins."""
        return self._request("commerce/exchange/coins", params=dict(quantity=quantity))

    def get_delivery(self):
        """" Return coins and items waiting at the BLTC """
        return self._request("commerce/delivery", authenticated=True)

    def get_current_buy_transaction(self):
        """" Return open buy orders """
        return self._request("commerce/transaction/current/buys", authenticated=True)

    def get_history_buy_transaction(self):
        """" Return closed buy orders """
        return self._request("commerce/transaction/history/buys", authenticated=True)

    def get_current_sell_transaction(self):
        """" Return open sell orders """
        return self._request("commerce/transaction/current/sells", authenticated=True)

    def get_history_sell_transaction(self):
        """" Return return closed sell orders """
        return self._request("commerce/transaction/history/sells", authenticated=True)

    def get_exchange(self):
        """ Return available exchange"""
        return self._request("commerce/exchange")

    def get_items(self, item_ids):
        """Get Items infos."""
        ids = ','.join(str(item_id) for item_id in item_ids)
        return self._request("items", params=dict(ids=ids))

    def get_prices(self, item_ids):
        """Get Items Price"""
        ids = ','.join(str(item_id) for item_id in item_ids)
        return self._request("commerce/prices", params=dict(ids=ids))

    def get_item_listing(self, item_id):
        """Get Items Price Listing"""
        return self._request("commerce/listings?ids={}".format(item_id))

    def get_price(self, item_id):
        """Get Item's Price"""
        return self.get_prices([item_id])[0]

    def get_ecto_price(self):
        """Get Ecto Price"""
        prices = self.get_price(self.ECTO_ID)
        return prices["sells"]["unit_price"]
