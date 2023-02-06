import os
import sys
import time

#COLORES
rojo = '\033[31;1m'
azul = '\033[34;1m'
verde = '\033[32;1m'
amarillo = '\033[33;1m'
morado = '\033[35;1m'
celeste = '\033[36;1m'
plomo = '\033[30;1m'
close = '\033[0m'

os.system ("toilet -f big ' 7K CC' -F gay | lolcat")
username = 'L7K-cc'      
password = 'dunbar09'

print(amarillo)
nick = str(input(' Coloca tu nick: '))

def restart():
	ngulang = sys.executable
	os.execl(ngulang, ngulang, *sys.argv)

def main():
	uname = str(input("\n\033[33;1mUSUARIO : \033[32;1m"))
	if uname == username:
		pwd = str(input("\n\033[33;1mCONTRASEÑA : \033[32;1m"))

		if pwd == password:
			os.system("clear")
			time.sleep(2)
			os.system ("toilet -f big ' 7KCC' -F gay | lolcat")
			print("\n\033[33;1m HOLA \033[31;1m†★",nick,"★†\033[33;1m BIENVENIDO AL 7K CC !!! RECUERDA EXTRAPOLAR LOS RESULTADOS !!!\n")
			time.sleep(2)
			print(rojo,'+————————————————————————————————————————————————————————————+')
			print(amarillo)
			print('  [ 01 ] TARGETA DE CREDITO ESTADOS UNIDOS')
			print('  [ 02 ] TARGETA DE CREDITO AUSTALIA')
			print('  [ 03 ] TARGETA DE CREDITO AUSTRIA')
			print('  [ 04 ] TARGETA DE CREDITO BELGIUM')
			print('  [ 05 ] TARGETA DE CREDITO BRAZIL')
			print('  [ 06 ] TARGETA DE CREDITO CANADA')
			print('  [ 07 ] TARGETA DE CREDITO DENMARK')
			print('  [ 08 ] TARGETA DE CREDITO ESTONIA')
			print('  [ 09 ] TARGETA DE CREDITO FINLANDIA')
			print('  [ 10 ] TARGETA DE CREDITO FRANCIA')
			print('  [ 11 ] TARGETA DE CREDITO GERMANYA')
			print('  [ 12 ] TARGETA DE CREDITO GREENLANDIA')
			print('  [ 13 ] TARGETA DE CREDITO HUNGARYA')
			print('  [ 14 ] TARGETA DE CREDITO ICELANDIA')
			print('  [ 15 ] TARGETA DE CREDITO NETHERLANDIA')
			print('  [ 16 ] TARGETA DE CREDITO NORWAY')
			print('  [ 17 ] TARGETA DE CREDITO POLAND')
			print('  [ 18 ] TARGETA DE CREDITO PORTUGAL')
			print('  [ 19 ] TARGETA DE CREDITO SLOVENIA')
			print('  [ 20 ] TARGETA DE CREDITO SPAÑA')
			print('  [ 21 ] TARGETA DE CREDITO SWEDEN')
			print('  [ 22 ] TARGETA DE CREDITO SWITZERLANDIA')
			print('  [ 23 ] TARGETA DE CREDITO TUNISIA')
			print('  [ 24 ] TARGETA DE CREDITO ARGENTINA(PRONTO).... \n\033[31;1m')
			sys.exit()

		else:
			os.system("clear")
			print("\n\033[1;31mLO SIENTO" , nick, " INGRESASTE UNA CONTRASEÑA INCORRECTA !!!\033[00m")
			print(azul, "SI NO SABES LA CONTRASEÑA COMUNICATE CON !L7K#0009 (DISCORD)")
			time.sleep(3.3)
			os.system("clear")
			restart()

	else:
		os.system("clear")
		print("\n\033[1;31mLO SIENTO " , nick, " INGRESASTE UN USUARIO INCORRECTO !!!\033[00m")
		print(azul, "\nSI NO SABES EL USUARIO COMUNICATE CON !L7K#0009 (DISCORD))
		time.sleep(3.3)
		os.system("clear")
		restart()

try:
	main()
except KeyboardInterrupt:
	os.system('clear')
	restart()
