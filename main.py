import re
import sys


argc = len(sys.argv)
if argc < 3:
    print('Uzycie: main.py do_analizy.txt wzorce.txt')
    sys.exit()
	
argv = sys.argv
plik_z_regulami = open(argv[2])
patterns = [];
wzorce_do_przetworzenia = []
linie_wejsciowe = plik_z_regulami.readlines();
for linia_wejsciowa in linie_wejsciowe:
    linia_wejsciowa = linia_wejsciowa.replace('\n', '')
    wzorce_do_przetworzenia.append(linia_wejsciowa.split(' '))
for i in range(0, len(wzorce_do_przetworzenia)):
    toSwap = wzorce_do_przetworzenia[i][1]
    if toSwap[0] == '[' and toSwap[-1] == ']':
        toSwap = toSwap[1:-1]
    for j in range(i, len(wzorce_do_przetworzenia)):
        pat = '\{' + wzorce_do_przetworzenia[i][0] + '\}'
        p = wzorce_do_przetworzenia[j][1]
        wzorce_do_przetworzenia[j][1] = re.sub(pat, toSwap, p)
patterns = wzorce_do_przetworzenia
dopasowane = {}
plik_wejsciowy = open(argv[1])
linie_wejsciowe = plik_wejsciowy.readlines()
for linia_wejsciowa in linie_wejsciowe:
    for dopasowany_wzorzec in patterns:
        matches = re.findall(dopasowany_wzorzec[1], linia_wejsciowa, re.IGNORECASE)
        if matches != None:
            matched = [x for x in matches if x != '']
            if len(matched) != 0:
                try:
                    dopasowane[dopasowany_wzorzec[0]].append(matched)
                except:
                    dopasowane[dopasowany_wzorzec[0]] = [matched]
					
					

while True:
	print('------------------------------------------------')
	print('Wybierz wzorzec z ktorego chcesz pokazac odnalezione dopasowania: ')
	for key, value in dopasowane.iteritems():
		if value > 0:
			print('Wzorzec: "' + key + '" | dopasowania: ' + str(len(value)))
	print('------------------------------------------------')
	wpisane = sys.stdin.readline().rstrip()
	print('------------------------------------------------')
	if dopasowane.has_key(wpisane):
		for i, linia_wejsciowa in enumerate(dopasowane[wpisane]):
			print(str(i+1) + '. Wzorzec ' + wpisane + ': ' + linia_wejsciowa[0])
	else:
		print('Nie znaleziono takiego wzorca, podaj inny!')