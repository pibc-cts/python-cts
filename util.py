import requests
import json


def post(method, params, port):
	url = "http://127.0.0.1:" + port + "/rpc"
	headers = {'content-type': 'application/x-www-form-urlencoded'}

	payload = {
	"method": method,
	"params": params,
	"jsonrpc": "2.0",
	"id": 1,
	}
	return requests.post(url, data=json.dumps(payload), headers=headers).json()



def get_order_book(base, quote, depth, port):
	return post("get_order_book", [base,quote,depth], port)['result']


def get_cny_settlement_price(port):
	result = get_object(["2.4.0"], port)["result"]
	cny = result[0]["current_feed"]['settlement_price']['base']['amount']
	bts = result[0]["current_feed"]['settlement_price']['quote']['amount']
	return float(cny) * 10 / float(bts)

def publish_cny_feed_price(account, cts_amount, cny_amount, port):
	feed = {"settlement_price" : {
	            "base": {
	                 "amount":int(cny_amount),
	                 "asset_id":"1.3.1"
	                 },
	            "quote":{
	                 "amount":int(cts_amount),
	                 "asset_id":"1.3.0"
	                 }
	            },
	            "maintenance_collateral_ratio" : 1750,
	            "maximum_short_squeeze_ratio" : 1100,
	            "core_exchange_rate": {
	                 "base":{
	                      "amount":int(cny_amount),
	                      "asset_id":"1.3.1"
	                  },
	                  "quote":{
	                      "amount":int(cts_amount * 1.05),
	                      "asset_id":"1.3.0"
	                  }
	            }
	       } 
	print(feed)
	print(account)
	return post('publish_asset_feed', [account, 'CNY', feed, True], port)
	
