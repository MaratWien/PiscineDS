class Research:
	@staticmethod
	def file_reader():
		with open("data.csv", "r") as file:
			tmp = file.read()
			file.close()
			return tmp


if __name__ == '__main__':
	print(Research.file_reader())
