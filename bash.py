"""Please, when you don't know what it is, don't touch it"""

import os

tab = "------------------------------------------------"

print(f"Minari Bash\n\nEnter help for read documentation\n{tab}")



while True:
	x = input(">>")
	if x == "new":
		print("What a file name :")
		filename = input()
		print("Print a text")
		print(filename + "$")
		text = input()
		file = open(filename, mode='w')
		file.write(text)
		file.close()
	if x == "open":
		print("What file open :")
		filename = input()
		file = open(filename, mode='r')
		try:
			file_content = file.read()
		except:
			try:
				file = open(filename + '.txt', mode='r')
			except:
				print("Invalid file name")

		print(file_content)
		input("--------")
		file.close()
	if x == "cls":
		os.system('cls')


	if x == "help":
		print(f"Minari Bash\n\n\n[command] new - Create new file\n[command] open - Open file\n[command] cls - Clear consolen\n[command] help - Print this message\n{tab}")
