def read_and_write():
	with open("ds.csv", 'r') as f:
		with open("ds.tsv", 'w') as file:
			file.write(f.read().replace('",', '"\t').replace('false,', 'false\t').replace('true,', 'true\t'))


if __name__ == '__main__':
	read_and_write()
