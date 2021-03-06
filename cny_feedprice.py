'''
file: cny_feedprice.py
author: CTS
description:
	cny_feedprice.py is a demo for feeding CNY's feed price. It link to one cli_wallet
by rpc port, and send all of the comand by cli_wallet.

Usage:
	Modify the script by your own information:

wallet_port:    The rpc port which cli_wallet opened for script
account_name:   Account name of yours, which must be in the cli_wallet
password:       The password of cli_wallet, not the account priv key.
'''

import client
import pdb
import market


def publish_feedprice(feed_price, wallet_port):
	bts_amount = 100
	cny_amount = bts_amount * feed_price
	ret =market.publish_cny_feed_price(account_name, bts_amount * 100000, cny_amount * 10000, wallet_port)
	print(ret)


wallet_port = '8093'
account_name = 'account_name'
password = 'passowrd'


account = client.Account(account_name, password, wallet_port)
account.unlock()


# get feed price by buy order price
order_book = market.get_order_book('CNY', 'CTS', 2, wallet_port)
buy = order_book['bids']

if buy == []:
	feed_price = 0.555
	print("No buy order found, feed_price is ", feed_price)
else:
	feed_price = float(buy[0]['price']) * 1.1
	print("found buy order, new feed_price is ", feed_price)

try:

	old_feed_price = market.get_cny_settlement_price(wallet_port)
except :
	old_feed_price = feed_price


if feed_price < old_feed_price:
	feed_price = old_feed_price
	print("feed price fix to old feed price:", old_feed_price)

publish_feedprice(feed_price, wallet_port)
