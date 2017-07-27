#Corrector tools
def choiceCorrector (choice):
	if choice != 1 and choice != 2:
		return False
	else:
		return True
		
def twinChecker (numbers, numberIndex):
	substractor = numberIndex
	while (substractor>0):
		if numbers [numberIndex] == numbers [numberIndex - substractor]:
			return False
		substractor -= 1
	return True
	
def rangeAndTwinChecker (numbers, numberIndex):
	if numbers [numberIndex] <= 25 and numbers [numberIndex] >= 1:
		if twinChecker (numbers, numberIndex) == True:
			return True
		else:
			return False
	else:
		return False

	
class player:
	def __init__ (self, choice):
		self.choice = choice
		if self.choice == 1:
			numbers = player.autoSlot ()
		else:
			numbers = player.manualSlot()
		self.numbers = numbers
	
	def autoSlot ():
		import random
		numbers = []
		c1 = 0
		while (c1<25):
			numbers.append (random.randint (1, 25))
			if c1 >= 0:
				if twinChecker (numbers, c1) == False:
					del numbers [c1]
					c1 -=1
			c1 += 1
	
		return numbers
	
	def manualSlot ():
		display = list (range (1,26))
		numbers = []
		c1 = 1
		index = 0
		while (c1<=5):
			c2 = 1
			while (c2<=5):
				numbers.append (int (input ("Masukkan angka untuk kotak(%d,%d): " % (c1, c2))))
			
				if index == 0:
					if numbers[index] > 25 or numbers[index] < 1:
						print ("Angka yang dimasukkan tidak boleh lebih kecil dari satu dan tidak boleh lebih besar dari 25.")
						del numbers [index]
						c2 -= 1
						index -= 1
					else:
						z = 0
						while (z<25):
							if numbers [index] == display [z]:
								display [z] = 0
							z += 1
						print ("Angka tersisa: ", end="")
						for x in display:
							if x!=0:
								print ( x, end=" ")
						print ("\n")
				
				if index>0:
					if rangeAndTwinChecker (numbers, index) == False:
						print ("Angka yang dimasukkan tidak boleh lebih kecil dari satu, tidak boleh lebih besar dari 25, dan harus berbeda dari angka-angka sebelumnya.")
						del numbers [index]
						c2 -= 1
						index -= 1
					else:
						z = 0
						while (z<25):
							if self [numbers] == display [z]:
								display [z] = 0
							z += 1
						print ("Angka tersisa: ", end="")
						for x in display:
							if x!=0:
								print (x, end=" ")
						print ("\n")
					
				index += 1
				c2 += 1
			c1 += 1
	
		return numbers
	
	def strike (self, isStriked):
		for x in self:
			if x == isStriked:
				del self [x]
				break


#Table Building
def boxMaker (numbers):
	numberIndex = 0
	i = 1
	print (" ---- ---- ---- ---- ----")
	while (i <= 5):
		j = 1
		while (j <= 5):
			if numbers [numberIndex] <= 9:
				print ("|  %d " % numbers [numberIndex], end="")
			else:
				print ("| %d " % numbers [numberIndex], end="")
			numberIndex += 1
			j += 1
		i += 1
		print ("|\n", end="")
		print (" ---- ---- ---- ---- ----")
			
#class core:
	
#	def moderator (self):
#		isStriked = int (input ("Ketik angka yang ingin Anda coret:\n"))
#		
#		c = 0
#		while (c<25):
#			if isStriked == numbers [c]:
#				numbers [c] = *24*
#			c += 1
		
