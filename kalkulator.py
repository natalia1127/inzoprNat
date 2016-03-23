def dodawanie(a, b):
	return a+b
try:
	a = int(input('podaj pierwsza liczbe'))	
	b = int(input('podaj druga liczbe'))
	print(dodawanie(a,b))
except ValueError as ve:
	print("WPROWADZONO BLEDNE DANE, KONCZE DZIALANIE...")
input()