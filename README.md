
Usage:
=======
see example.py

Requirement:
============

- Python 3.6
- requests lib `pip install requests`

Covered API Endpoints:
=======================

/v2/commerce/delivery
---------------------
*Authentication REQUIERED*
`get_delivery()`

Make sure to create the client with a valid API Key

```
{

  "coins": 0, => coins waiting at BLTC

  "items": [] => list of items Waiting to withdraw

}
```


/v2/commerce/exchange
----------------------

`get_echange()`

Return a list of exchangeable currencies

```
[

  "coins",

  "gems"

]
```


/v2/commerce/exchange/coins
----------------------------

`get_gem_price()`

```
{

  "coins_per_gem": 5000, => number of copper requiered for One gem

  "quantity": 2 => number of gem get for 10000 gems

}
```

/v2/commerce/exchange/gems
---------------------------
`get_gem_price()`

returns :
```
{

  "coins_per_gem": 1852, => number of copper recieved for a single gem

  "quantity": 18524866 => number of copper recieved for 10000 gems

}
```

 /v2/commerce/listings
 ----------------------

  `get_item_listing(item)` where item is an Item ID


/v2/commerce/prices
-------------------
`get_prices(items)` => use when items is like : [{"id":9999,...},{"id":8888,...}]

`get_prices_list(items)` => use when items is like : [9999,8888,7777]

/v2/commerce/transactions/current/sells
--------------------------------------

*Authentication REQUIERED*
`get_current_sell_transaction()`

Return open sell orders


/v2/commerce/transactions/history/sells
--------------------------------------

*Authentication REQUIERED*

`get_history_sell_transaction()`

Return closed sell order

/v2/commerce/transactions/current/buys
--------------------------------------

*Authentication REQUIERED*
`get_current_buy_transaction()`

Return open buy orders

/v2/commerce/transactions/history/buys
--------------------------------------

*Authentication REQUIERED*
`get_history_buy_transaction()`

Return closed buy orders

Extras API Endpoints:
=======================

Ectos Price
------------

`get_ecto_price()`

Return Glob of Ectoplasm price
