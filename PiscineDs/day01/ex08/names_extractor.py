import sys


def names_extractor():
	if len(sys.argv) != 2:
		return
	with open(sys.argv[1], 'r') as r_f:
		with open('employees.tsv', 'w') as w_f:
			w_f.write('Name\tSurname\tE-mail\n')
			mails = [s.strip() for s in r_f.readlines()]
			for mail in mails:
				name, surname = mail.split('@')[0].split('.')
				name, surname = name.capitalize(), surname.capitalize()
				w_f.write(f'{name}\t{surname}\t{mail.strip()}\n')


if __name__ == '__main__':
	names_extractor()
