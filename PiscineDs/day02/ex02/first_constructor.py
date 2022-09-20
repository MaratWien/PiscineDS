import sys, os


class Research:
	def __init__(self, path):
		self.path = path

	def file_reader(self):
		with open(self.path, 'r') as file:
			file_data = file.readlines()
		if len(file_data) < 2:
			raise Exception('file has to have at least 2 rows')
		head = file_data[0].split(',')
		if len(head) != 2:
			raise Exception("header has to have precisely 2 strings")
		for row in file_data[1:]:
			if row[0:3] != '0,1' and row[0:3] != '1,0':
				raise Exception('Incorrect file')
		return ''.join(file_data)


if __name__ == '__main__':
	if len(sys.argv) == 2:
		print(Research(sys.argv[1]).file_reader())
