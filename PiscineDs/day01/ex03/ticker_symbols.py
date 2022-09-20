import sys


def ticker_symbols():
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
	instance_name = sys.argv[1].upper()
	if instance_name in stocks:
		for key, value in companies.items():
			if instance_name == value:
				print(key, stocks[instance_name])
	else:
		print('Unknown ticker')
		return


if __name__ == '__main__':
	if len(sys.argv) != 2:
		exit(1)
	ticker_symbols()
