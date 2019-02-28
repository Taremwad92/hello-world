 def performOPr(*nums, opr = "+"):
	def doAdd(*nums):
		result = 0
		for num in nums:
			result += int(num)
		return result
	def doSub(*nums):
		result = 0
		for num in nums:
			result -= int(num)
		return result
	def doMult(*nums):
		result = 0
		for num in nums:
			result *= int(num)
		return result
	def doDiv(*nums):
		result = 0
		for num in nums:
			result /= int(num)
		return result
	if opr == "+":
		doAdd(*nums)
	elif opr == "-":
		doSub(*nums)
	elif opr == "*":
		doMult(*nums)
	elif opr == "/":
		doDiv(*nums)
	else:
		print("Bad choice try again")

		
>>> 
>>> while(True):
		print("Choose option;")
		print("+: Addition")
		print("-: Subtraction")
		print("*: Multipliction")
		print("/: Division")
		choice = str(input())
		if choice == "+":
			numlist = []
			print("Enter numbers or Q to quit")
			while(True):
				numlist = list(input())
				if "Q" or "q" in numlist:
					numlist.pop()
					print("The Result of Addition is "+str(performOPr(numlist)))
		elif choice == "-":
			numlist = []
			print("Enter numbers or Q to quit")
			while(True):
				numlist = list(input())
				if "Q" or "q" in numlist:
					numlist.pop()
					print("The Result of Addition is "+str(performOPr(numlist,opr = "-")))
		elif choice == "*":
			numlist = []
			print("Enter numbers or Q to quit")
			while(True):
				numlist = list(input())
				if "Q" or "q" in numlist:
					numlist.pop()
					print("The Result of Addition is "+str(performOPr(numlist,opr = "*")))
		elif choice == "/":
			numlist = []
			print("Enter numbers or Q to quit")
			while(True):
				numlist = list(input())
				if "Q" or "q" in numlist:
					numlist.pop()
					print("The Result of Addition is "+str(performOPr(numlist,opr = "/")))
		elif choice == "Q" or choice == "q":
			print("Thanks for using")
			break
		else:
			print("Bad choice")

		