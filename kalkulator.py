def dodawanie(a, b):
	return a+b
def get_info():
	return "To jest program kalkulator stworzony przez Natalie"
try:
	a = int(input('podaj pierwsza liczbe'))	
	b = int(input('podaj druga liczbe'))
	print(dodawanie(a,b))
except ValueError as ve:
	print("WPROWADZONO BLEDNE DANE, KONCZE DZIALANIE...")
print(get_info())
input()