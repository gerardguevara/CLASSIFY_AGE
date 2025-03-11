def classify_age(num):
	while True:
		num = int(input("type your age"))
		if num >=0 and num <= 12:
			print ("You are a child")
		elif num >=13 and num <=19:
			print ("you are a teen")
		elif num >=20 and num <=64:
			print("you are an adult")
		elif num >=65:
			print("you are a senior")
		else:
			print("invalid input")
classify_age(1)