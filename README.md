
# uniwersalny generator skanerów <br>
Z kodu wyłąpuje poszczególne części i przydziela je do odpowiedniej grupy - np. for -> pętla. <br>
Wzorce, które rozpoznaje program:
funkcja {wyraz}\(.+\)
if if\(.+\)
petla_for for\(.+\)
zmienna ([a-z\d]+[\s]+=[\s]+[\d\w\.\(\)\s]+)
blok_kodu \{(.*)\}
komentarz_jednoliniowy \/\/.*
include \#include.*
return_funkcji return.* 
