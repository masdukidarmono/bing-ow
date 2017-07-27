###Main###

import modulebingow

#Beginning
fillMethod = int (input ("Pilih metode pengisian kotak yang Anda inginkan (ketikkan nomor pilihan).\n1. Otomatis\n2. Manual\n"))

while (modulebingow.choiceCorrector (fillMethod) == False):
	print ("Anda tidak memasukkan keyword yang benar. Silakan coba lagi.")
	fillMethod = int (input ("Pilih salah satu:\n1. Otomatis\n2. Manual\n"))
	
if fillMethod == 1:
	p1 = modulebingow.player (1)
	print ("Permainan dimulai! Tabel Bing-ow Anda")
	modulebingow.boxMaker (p1.numbers)
else:
	p1 = modulebingow.player (2)
	print ("Permainan dimulai! Tabel Bing-ow Anda:")
	modulebingow.boxMaker (p1.numbers)
		

#The Game
#game.moderator ()
