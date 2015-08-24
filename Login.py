import time
def  Login_in():
	time.sleep(0.1)
	Login_1 = raw_input("Username Please  ")
	if Login_1 == "Naliste":
		passwordnaliste()

	if Login_1 == "Jaliste":
		passwordjaliste()
	else:
		print "Bad login, try again"
		time.sleep(0.2)
		Login_in()

def passwordnaliste():
	passwordnaliste_1 = raw_input("Password Please  ")
	if passwordnaliste_1 == "2147483647":
		Naliste()
	else:
		print "Bad Password , try again"
		time.sleep(0.2)
		passwordnaliste()

def passwordjaliste():
	passwordjaliste_1 = raw_input("Password Please")
	if passwordjaliste_1 == "jalistejuan":
		Jaliste()
	else:
		print "Bad Password , Try again"
		time.sleep(0.2)
		passwordjaliste()

def Naliste():
	print "Hello Naliste"


def Jaliste():
	print "Hello Jaliste"


Login_in()
