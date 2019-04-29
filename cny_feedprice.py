import client
import util
import pdb

def publish_feedprice(feed_price, wallet_port):
	bts_amount = 100
	cny_amount = bts_amount * feed_price
	util.publish_cny_feed_price(account_name, bts_amount * 100000, cny_amount * 10000, wallet_port)






wallet_port = '8093'

#unlock account
account_name = 'account_name'
account = client.Account(account_name, 'password', wallet_port)
account.unlock()


# get feed price by buy order price
order_book = util.get_order_book('CNY', 'CTS', 2, wallet_port)
buy = order_book['bids']

if buy == []:
	print("No buy order found, feed_price is 0.1")
	feed_price = 0.1
else:
	feed_price = float(buy[0]['price']) * 1.1
	print("found buy order, new feed_price is ", feed_price)

try:

	old_feed_price = util.get_cny_settlement_price(wallet_port)
except :
	old_feed_price = feed_price


if feed_price < old_feed_price:
	feed_price = old_feed_price
	print("feed price fix to old feed price:", old_feed_price)

publish_feedprice(feed_price, wallet_port)
