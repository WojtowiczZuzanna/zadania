file = open('countries.txt','r')
file_content = file.read()
print(file_content)
file.close()

#read "r" - tylko do odczytu
#write "w" - tworzy nowy plik, a jesli istnieje zostaje usuwany
#append "a" - tworzy nowy plik, to co było zostaje i mozna dopisać zawartość

#file_content -> zawartość pliku

#otwarty plik należy zamknąć, żeby nie utracić danych
#instrukcja "close" zapisuje dane na dysku

