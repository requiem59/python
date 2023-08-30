import random

def generator(l):
	c = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!#$%&\()*+,-./:;<=>?@[]^_`{|}~"
	passwd = ""
	for i in range(l):
		passwd = passwd + random.choice(c)
	print(passwd)

length = input("Password length: ")

generator(int(length))	