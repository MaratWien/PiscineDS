def dict_sorter():
	list_of_tuples = [
						('Russia', '25'),
						('France', '132'),
						('Germany', '132'),
						('Spain', '178'),
						('Italy', '162'),
						('Portugal', '17'),
						('Finland', '3'),
						('Hungary', '2'),
						('The Netherlands', '28'),
						('The USA', '610'),
						('The United Kingdom', '95'),
						('China', '83'),
						('Iran', '76'),
						('Turkey', '65'),
						('Belgium', '34'),
						('Canada', '28'),
						('Switzerland', '26'),
						('Brazil', '25'),
						('Austria', '14'),
						('Israel', '12')
	]

	new_dict = {}
	for element in list_of_tuples:
		if int(element[1]) not in new_dict:
			new_dict[int(element[1])] = [element[0]]
		else:
			new_dict[int(element[1])].append(element[0])
	for number in sorted(new_dict, reverse=True):
		for country in sorted(new_dict[number]):
			print(country)


if __name__ == '__main__':
	dict_sorter()
