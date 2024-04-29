import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       # Retrieve the following stock, bid price, ask price,
       # and final price information by calling the
       # getDataPoint() function.
       stock, bid_price, ask_price, price = getDataPoint(quote)
       
       # Check that the correct information is printed
       # such as the stock ticker name, top bid price,
       # top ask price, and the price itself.
       self.assertEqual((stock, bid_price, ask_price, price), (quote["stock"], quote["top_bid"]["price"], quote["top_ask"]["price"], (quote["top_bid"]["price"] + quote["top_ask"]["price"]) / 2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       # Just like the previous unit test, retrieve
       # the stock, bid price, ask price, and final
       # price from the getDataPoint() function.
       stock, bid_price, ask_price, price = getDataPoint(quote)

       # Check that the correct information is printed.
       self.assertEqual((stock, bid_price, ask_price, price), (quote["stock"], quote["top_bid"]["price"], quote["top_ask"]["price"], (quote["top_bid"]["price"] + quote["top_ask"]["price"]) / 2))

  """ ------------ Add more unit tests ------------ """
  def test_getRatio_enterZeroes(self):
     # Let's pretend that one of the quotes, whose ticker name is "DEF", has an ask and bid price
     # of 0. This way, we can test whether the getRatio() function returns an error when this
     # happens.
     quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 0, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
     ]

     """------------- Add the assertions -------------"""
     # Dictionary that will store the stock ticker name as 
     # the key and its final price as the value.
     stock_price = {}

     for quote in quotes:
        # Get the necessary information as covered in the
        # previous two tests.
        stock, bid_price, ask_price, price = getDataPoint(quote)

        # Include the stock ticker name with its associated final
        # price in the dictionary.
        stock_price[stock] = price

     # Since we are only checking two quotes, we can now check that the
     # function that calculates the ratio between the prices of two
     # quotes, in this case, returns 0 if one or both prices are 0.
     self.assertEqual(getRatio(stock_price["ABC"], stock_price["DEF"]), 0)

  def test_getRatio_noZeroes(self):
     # Unlike the previous test that returns a 0 if one or both final quote
     # prices are 0, include quotes that have top ask and bid prices that
     # are greater than 0.
     quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
     ]

     """------------- Add the assertions -------------"""
     # Dictionary that will store the stock ticker name as 
     # the key and its final price as the value.
     stock_price = {}

     for quote in quotes:
        # Get the necessary information as covered in the
        # previous two tests.
        stock, bid_price, ask_price, price = getDataPoint(quote)

        # Include the stock ticker name with its associated final
        # price in the dictionary.
        stock_price[stock] = price

     # Since there are only two quotes provided, we are going to check the ratio
     # between stocks "ABC" and "DEF", and assert that they return the correct
     # result.
     self.assertEqual(getRatio(stock_price["ABC"], stock_price["DEF"]), 1.0005426841995408)

if __name__ == '__main__':
    unittest.main()
