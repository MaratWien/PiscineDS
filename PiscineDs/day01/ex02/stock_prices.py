import sys


def stock_prices():
	companies = {
					'Apple': 'AAPL',
					'Microsoft': 'MSFT',
					'Netflix': 'NFLX',
					'Tesla': 'TSLA',
					'Nokia': 'NOK'
	}
	stocks = {
					'AAPL': 287.73,
					'MSFT': 173.79,
					'NFLX': 416.90,
					'TSLA': 724.88,
					'NOK': 3.37
	}

	instance_name = sys.argv[1].lower().capitalize()
	if instance_name in companies:
		print(stocks[companies[instance_name]])
	else:
		print("Unknown company")
		return


if __name__ == '__main__':
	if len(sys.argv) != 2:
		exit(1)
	stock_prices()
