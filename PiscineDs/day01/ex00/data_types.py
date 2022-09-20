def data_types():
	a = 5
	b = 'Hello, World!'
	c = 4.3
	d = True
	new_list = []
	new_dictionary = {}
	new_tuple = ()
	new_set = {1, 2}
	print('[', type(a).__name__, ', ', type(b).__name__, ', ', type(c).__name__, ', ', type(d).__name__,  ', ', type(new_list).__name__, ', ', type(new_dictionary).__name__, ', ', type(new_tuple).__name__, ', ', type(new_set).__name__, ']', sep='')


if __name__ == '__main__':
	data_types()
