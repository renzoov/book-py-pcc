first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

message = f"Hello, {full_name.title()}!"
print(message)

#darle tab a una palabra
print("\tPython")

#darle salto de linea a una palabra
print("Languages:\nPython\nC\nJavaScript")

#eliminar espacios en blanco al inicio y al final
favorite_language = ' Python 3 '
print(favorite_language.strip())

#eliminar espacios en a la izquierda
game1 = "zelda and mario"
game2 = " yoshi and luigi"

print(game1 + game2)           
print(game1  + game2.lstrip())

#eliminar espacios en a la derecha
game3 = "toad and koopa "
game4 = "peach and wario"

print(game3 + game4)          
print(game3.rstrip() + game4)

#eliminar prefijo
book_url = 'https://book.com'
remove_https = book_url.removeprefix("https://")

print(book_url)        
print(remove_https)    