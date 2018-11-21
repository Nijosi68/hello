age = 70

if age < 5:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
#Note an else block is not required. If all conditions can be set, consider using a final elif block to avoid malicious code, not meeting the earlier if or elif tests, passing the else test
#else:
elif age >= 65:
	price = 5
print('Welcome! The price of admission is £' + str(price) + '.00.')
