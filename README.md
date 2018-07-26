
Usage:
=======
see example.py

Covered API Endpoints:
=======================
/v2/commerce/delivery
---------------------
/v2/commerce/exchange
----------------------
/v2/commerce/exchange/coins
----------------------------
`get_gem_price()`

`{
  "coins_per_gem": 5000, => number of copper requiered for One gem
  "quantity": 2 => number of gem get for 10000 gems
}`

/v2/commerce/exchange/gems
---------------------------
`get_gem_price()`

returns :
`{
  "coins_per_gem": 1852, => number of copper recieved for a single gem
  "quantity": 18524866 => number of copper recieved for 10000 gems
}`

 /v2/commerce/listings
 ----------------------
  `get_item_listing(item)` where item is an Item ID

/v2/commerce/prices
-------------------

/v2/commerce/transactions
--------------------------
