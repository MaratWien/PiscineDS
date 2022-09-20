def to_dictionary():
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
	# new_list = dict(([(key, value) for key, value in list_of_tuples]))
	# for key, value in new_list.items():
	# 	print(key, value)
	new_dict = {}
	for ch in list_of_tuples:
		if ch[1] not in new_dict:
			new_dict[ch[1]] = [ch[0]]
		else:
			new_dict[ch[1]].append(ch[0])
	for key, values in new_dict.items():
		for value in values:
			print(f"'{key}' : '{value}'")


if __name__ == '__main__':
	to_dictionary()
