def activity01(num):
	''' Determine if an input number is Even or Odd'''
	if (num % 2 == 0):
		return 'Even'
	else:
		return 'Odd'

def activity02(iv_one, iv_two):
	'''Returns the sum of two input values'''
	return iv_one + iv_two

def activity03(num_list):
	'''Given a list of integers, count how many are even'''
	num_integers = 0

	for number in num_list:
		if (number % 2 == 0):
			num_integers += 1

	return num_integers

def activity04(input_string):
	'''Return the input string, backward'''
	return input_string[::-1]
