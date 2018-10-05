import operator

saved_string = ''

def remove_letter(): #Remove a selected letter from a string
	#print "Remove letter"
	base_string = str(raw_input("Enter string: "))
	letter_remove = str(raw_input("Enter letter to remove: "))
	letter_remove = letter_remove[0]
	string_length = len(base_string)
	location = 0

	while location < string_length:
		if base_string[location] == letter_remove:
			base_string = base_string[:location] + base_string[location + 1::]
			string_length -= 1

		location += 1

	print base_string

	return

def num_compare(): #Compar 2 numbers to determine the larger
	#print "Num compare"
	num1 = int(raw_input("Input first number: "))
	num2 = int(raw_input("Input second number: "))

	if (num1 > num2):
		print(num1)
	elif (num2 > num1):
		print(num2)
	else:
		print "Equal"

	return

def print_string(): #Print the previous stored string
	print saved_string
	return

def calculator(): #basic calculator (addition, subtraction, multiplication, division)
	#print "Calculator"
	sign_dict = {'+' : operator.add , '-' : operator.sub}
	num1 = int(raw_input("Input first number: "))
	sign = str(raw_input("Action: "))
	num2 = int(raw_input("Input second number: "))

	'''
	if sign == '+':
		print num1 + num2
	if sign == '-':
		print num1 - num2
	if sign == '*':
		print num1 * num2
	if sign == '%':
		print num1 % num2
	'''

	print sign_dict[sign](num1, num2)

	return

def accept_and_store(): # Accept and store a string
	#print "Accept and store"
	global saved_string
	saved_string = str(raw_input("Input string: "))

	return

def main(): #menu goes here
	opt_list = [accept_and_store,
				calculator,
				print_string,
				num_compare,
				remove_letter]

	print "SELECT OPTION: "
	print "1\tAccept and store"
	print "2\tCalculator"
	print "3\tPrint stored string"
	print "4\tNumber comparison"
	print "5\tLetter Remover"

	opt_choice = int(raw_input("SELECTION: "))
	opt_choice -= 1
	opt_list[opt_choice]()

	return

while(True):
	main()
