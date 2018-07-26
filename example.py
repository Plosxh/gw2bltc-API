import bltc


clientBltc = bltc.Bltc("apiKey") # You'll need an API Key for some reqests, espacially to see your actual an historical buys and sell orders

listings = clientBltc.get_item_listing("19700") #Get all the listing for the item 19700 wich is Mithril Ore
print(listings)
