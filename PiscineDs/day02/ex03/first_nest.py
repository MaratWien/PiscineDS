import sys, os


class Research:
	def __init__(self, f_path):
		self.f_path = f_path
		self.calculations = self.Calculations()

	def file_reader(self, has_header = True):
		with open(self.f_path, 'r') as r_f:
			rows = r_f.readlines()
		if has_header == True:
			header = rows[0].split(',')
		if len(header) != 2:
			raise Exception('header has to have precisely 2 strings')
		rows = rows[1:]
		if len(rows) == 0:
			raise Exception('file has to have at least 2 rows')
		res = []
		for row in rows:
			row = row.strip()
			if row != '0,1' and row != '1,0':
				raise Exception('Incorrect file')
			res.append([int(n) for n in row.split(',')])
		return res

	class Calculations:
		def counts(self, data):
			return [sum([elem[0] for elem in data]), sum([elem[1] for elem in data])]

		def fractions(self, head, tail):
			return [head / (head + tail) * 100, tail / (head + tail) * 100]


if __name__ == '__main__':
	if len(sys.argv) == 2:
		research = Research(sys.argv[1])
		data = research.file_reader()
		print(data)
		counts = research.calculations.counts(data)
		print(counts[0], counts[1])
		fractions = research.calculations.fractions(counts[0], counts[1])
		print(fractions[0], fractions[1])