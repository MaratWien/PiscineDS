import sys


def call_center(clients, recipients):
	return list(set(clients) - set(recipients))


def potential_clients(participants, clients):
	return list(set(participants) - set(clients))


def loyalty_program(clients, participants):
	return list(set(clients) - set(participants))


def marketing():
	clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is',
				'bill_gates@live.com', 'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
	participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 'jessica@gmail.com',
					'elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
	recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
	if len(sys.argv) != 2:
		raise Exception('Invalid number of arguments')
	email_accounts = ['call_center', 'potential_clients', 'loyalty_program']
	if sys.argv[1] == email_accounts[0]:
		print(call_center(clients, recipients))
	elif sys.argv[1] == email_accounts[1]:
		print(potential_clients(participants, clients))
	elif sys.argv[1] == email_accounts[2]:
		print(loyalty_program(clients, participants))
	else:
		raise Exception('Invalid email account')


if __name__ == '__main__':
	marketing()
