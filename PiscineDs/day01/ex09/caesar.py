import sys


def caesar():
	if len(sys.argv) != 4:
		raise Exception('Incorrect number of arguments is given')
	text = sys.argv[2]
	try:
		text.encode('ascii')
	except UnicodeEncodeError:
		raise Exception('The script does not support your language yet')
	shift = int(sys.argv[3])
	if sys.argv[1] == 'decode':
		shift *= -1
	elif sys.argv[1] != 'encode':
		raise Exception('Incorrect command')
	lower = list('abcdefghijklmnopqrstuvwxyz')
	capital = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
	res = ''
	for s in text:
		if s in lower:
			res += lower[(lower.index(s) + shift) % 26]
		elif s in capital:
			res += capital[(capital.index(s) + shift) % 26]
		else:
			res += s
	print(res)


if __name__ == '__main__':
	caesar()
