import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 11.2, 'size': 76}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 12, 'size': 89}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 221.2, 'size': 26}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 221.3, 'size': 89}, 'id': '0.109974697771', 'stock': 'DEF'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price']+quote['top_ask']['price'])/2))



  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.95, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 19.2, 'size': 64}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 19.3, 'size': 79}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 74}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 127.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price']+quote['top_ask']['price'])/2))



  def test_getDataPoint_calculatePriceAskGreaterThanBid(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 115.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 19.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 19.25, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 5.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 4.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price']+quote['top_ask']['price'])/2))



  def test_getDataPoint_calculatePriceAskZero(self):
    quotes = [
      {'top_ask': {'price': 0.0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 1.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 0.0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 0, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 1.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price']+quote['top_ask']['price'])/2))


  def test_getDataPoint_calculatePriceAlmostZero(self):
    quotes = [
      {'top_ask': {'price': 0.2, 'size': 56}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 0.120, 'size': 56}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0.20, 'size': 109}, 'id': '0.109974697771', 'stock': 'DEF'},
      {'top_ask': {'price': 1.120, 'size': 76}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0.20, 'size': 59}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 0.190, 'size': 74}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 1.170, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price']+quote['top_ask']['price'])/2))



  def test_getDataPoint_calculatePriceBidZero(self):
    quotes = [
      {'top_ask': {'price': 1.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0.0, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 2.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0.0, 'size': 109}, 'id': '0.109974697771', 'stock': 'DEF'},
      {'top_ask': {'price': 2.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0.0, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price']+quote['top_ask']['price'])/2))



  def test_getDataPoint_calculatePriceAskEqualsBid(self):
    quotes = [
      {'top_ask': {'price': 119.25, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 119.25, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 259.25, 'size': 86}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 259.25, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 7, 'size': 78}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 7, 'size': 19}, 'id': '0.109974697771', 'stock': 'DEF'},
      {'top_ask': {'price': 0.0, 'size': 58}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0.0, 'size': 69}, 'id': '0.109974697771', 'stock': 'DEF'},
      {'top_ask': {'price': 65, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 65, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price']+quote['top_ask']['price'])/2))



  def test_getDataPoint_calculatePriceBigDifference(self):
    quotes = [
      {'top_ask': {'price': 120.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 125.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 1.25, 'size': 56}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 2.48, 'size': 49}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 12.2, 'size': 15}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 18.48, 'size': 10}, 'id': '0.109974697771', 'stock': 'DEF'},
      {'top_ask': {'price': 140.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 131.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price']+quote['top_ask']['price'])/2))


  def test_getDataPoint_calculatePriceSmallDifference(self):
    quotes = [
      {'top_ask': {'price': 120.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.25, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 1.25, 'size': 56}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 1.4, 'size': 49}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 12.25, 'size': 15}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 12.20, 'size': 10}, 'id': '0.109974697771', 'stock': 'DEF'},
      {'top_ask': {'price': 140.68, 'size': 74}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 140.75, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price']+quote['top_ask']['price'])/2))
    


  def test_getRatio_(self):
    quotes = [
      {'top_ask': {'price': 120.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.25, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 12.25, 'size': 15}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 12.20, 'size': 10}, 'id': '0.109974697771', 'stock': 'DEF'},
      {'top_ask': {'price': 1.25, 'size': 56}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 1.4, 'size': 49}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 140.68, 'size': 74}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 140.75, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    prices={}
    prices['ABC']=(quotes[0]['top_ask']['price']+quotes[0]['top_bid']['price'])/2    #Initializing Opening Price of Stock ABC
    prices['DEF']=(quotes[1]['top_ask']['price']+quotes[0]['top_bid']['price'])/2    #Initializing Opening Price of Stock DEF
    
    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      prices[stock]=price    #Price being updated
      self.assertEqual(getRatio(prices['ABC'], prices['DEF']), (prices['ABC']/prices['DEF']))

  def test_getRatio_RatioOne(self):
    quotes = [
      {'top_ask': {'price': 119.25, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 119.25, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 259.25, 'size': 86}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 259.25, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 7, 'size': 78}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 7, 'size': 19}, 'id': '0.109974697771', 'stock': 'DEF'},
      {'top_ask': {'price': 0.0, 'size': 58}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0.0, 'size': 69}, 'id': '0.109974697771', 'stock': 'DEF'},
      {'top_ask': {'price': 65, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 65, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    prices={}

    prices['ABC']=(quotes[0]['top_ask']['price']+quotes[0]['top_bid']['price'])/2    #Initializing Opening Price of Stock ABC
    prices['DEF']=(quotes[2]['top_ask']['price']+quotes[0]['top_bid']['price'])/2    #Initializing Opening Price of Stock DEF
    
    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      prices[stock]=price    #Price being updated
      if(prices['DEF'] != 0.0):
        ans=(prices['ABC']/prices['DEF'])
        self.assertEqual(getRatio(prices['ABC'], prices['DEF']), ans)
      else:
        continue


  def test_getRatio_RatioGreaterThanOne(self):
    quotes = [
      {'top_ask': {'price': 119.25, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 119.25, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 259.25, 'size': 16}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 259.25, 'size': 19}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 115.25, 'size': 78}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.15, 'size': 19}, 'id': '0.109974697771', 'stock': 'DEF'},
      {'top_ask': {'price': 0.0, 'size': 58}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0.0, 'size': 69}, 'id': '0.109974697771', 'stock': 'DEF'},
      {'top_ask': {'price': 6.5, 'size': 44}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 6.65, 'size': 51}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    prices={}

    prices['ABC']=(quotes[0]['top_ask']['price']+quotes[0]['top_bid']['price'])/2     #Initializing Opening Price of Stock ABC
    prices['DEF']=(quotes[2]['top_ask']['price']+quotes[0]['top_bid']['price'])/2     #Initializing Opening Price of Stock DEF
    
    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      prices[stock]=price    #Price being updated
      if(prices['DEF'] != 0.0):
        ans=(prices['ABC']/prices['DEF'])
        self.assertEqual(getRatio(prices['ABC'], prices['DEF']), ans)
      else:
        continue


  def test_getRatio_RatioLessThanOne(self):
    quotes = [
      {'top_ask': {'price': 119.25, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 119.25, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 2.95, 'size': 16}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 3.5, 'size': 19}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 265.25, 'size': 88}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 264.15, 'size': 99}, 'id': '0.109974697771', 'stock': 'DEF'},
      {'top_ask': {'price': 10.50, 'size': 58}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 11.0, 'size': 69}, 'id': '0.109974697771', 'stock': 'DEF'},
      {'top_ask': {'price': 6.5, 'size': 44}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 6.65, 'size': 51}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    prices={}

    prices['ABC']=(quotes[0]['top_ask']['price']+quotes[0]['top_bid']['price'])/2     #Initializing Opening Price of Stock ABC
    prices['DEF']=(quotes[2]['top_ask']['price']+quotes[0]['top_bid']['price'])/2     #Initializing Opening Price of Stock DEF
    
    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      prices[stock]=price    #Price being updated
      if(prices['DEF'] != 0.0):
        ans=(prices['ABC']/prices['DEF'])
        self.assertEqual(getRatio(prices['ABC'], prices['DEF']), ans)
      else:
        continue


  def test_getRatio_RatioAtleastOnePriceZero(self):
    quotes = [
      {'top_ask': {'price': 119.25, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 119.25, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 0.0, 'size': 16}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0.0, 'size': 19}, 'id': '0.109974697771', 'stock': 'DEF'},
      {'top_ask': {'price': 0.0, 'size': 78}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0.0, 'size': 19}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 2.50, 'size': 58}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 3.0, 'size': 69}, 'id': '0.109974697771', 'stock': 'DEF'},
      {'top_ask': {'price': 0.0, 'size': 44}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0.0, 'size': 51}, 'id': '0.109974697771', 'stock': 'ABC'}
    ]
    prices={}

    prices['ABC']=(quotes[0]['top_ask']['price']+quotes[0]['top_bid']['price'])/2     #Initializing Opening Price of Stock ABC
    prices['DEF']=(quotes[1]['top_ask']['price']+quotes[0]['top_bid']['price'])/2     #Initializing Opening Price of Stock DEF
    
    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      prices[stock]=price    #Price being updated
      if(prices['DEF'] != 0.0):
        ans=(prices['ABC']/prices['DEF'])
        self.assertEqual(getRatio(prices['ABC'], prices['DEF']), ans)
      else:
        continue


  def test_getRatio_RatioBigSmallDifference(self):
    quotes = [
      {'top_ask': {'price': 119.25, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 119.25, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 2.95, 'size': 16}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 3.5, 'size': 19}, 'id': '0.109974697771', 'stock': 'DEF'},
      {'top_ask': {'price': 119.25, 'size': 88}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 119.50, 'size': 99}, 'id': '0.109974697771', 'stock': 'DEF'},
      {'top_ask': {'price': 10.50, 'size': 58}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 11.0, 'size': 69}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 6.5, 'size': 44}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 6.65, 'size': 51}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    prices={}

    prices['ABC']=(quotes[0]['top_ask']['price']+quotes[0]['top_bid']['price'])/2     #Initializing Opening Price of Stock ABC
    prices['DEF']=(quotes[1]['top_ask']['price']+quotes[0]['top_bid']['price'])/2     #Initializing Opening Price of Stock DEF
    
    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      prices[stock]=price    #Price being updated
      if(prices['DEF'] != 0.0):
        ans=(prices['ABC']/prices['DEF'])
        self.assertEqual(getRatio(prices['ABC'], prices['DEF']), ans)
      else:
        continue




if __name__ == '__main__':
  unittest.main() 
