from nltk.ccg import chart, lexicon

lex = lexicon.parseLexicon('''
    :- S, NP, N, VP

    Det :: NP/N
    	 
    Pablo => NP
    lee => (S\\NP)/NP
    un => Det
    libro => N
    interesante => N\N
    Ana => NP
    y => var\\.,var/.,var
    fueron => (S\\NP)/NP
    al => NP/N
    cine => N
    ayer => (S\NP)\(S\NP)
    Ayer => (S/NP)/(S/NP)
    auto => NP
    en => (NP\NP)/NP
    que => S/S	
    que => (N\\N)/(S/NP)
    es => (S\\NP)/(N\N)
    El => Det
    el => Det
    cree => (S\\NP)/S
    ministro => N
    anuncio => (S\\NP)/NP
    presidente => N
    desmintio => (S\\NP)/NP
    la => Det
    nueva => N/N
    ley => N
    compro => (S\\NP)/NP
    las => Det
    bebidas => N
    panaderia => N
    super => N
	pero => var\\.,var/.,var
''')

parser = chart.CCGChartParser(lex, chart.DefaultRuleSet)

print "\n################Bienvenido################\n"

entry = ""

while (entry != "fin"):
    entry = raw_input("\nIngrese la oracion para realizar el analisis o fin para salir:\n> ")
    
    if (entry != "fin"):
        cont = 0
        for parse in parser.parse(entry.split()):
            cont = cont + 1
            print "\n"
            chart.printCCGDerivation(parse)
            break
        
        if (cont == 0):
		    print "Error! La oracion ingresada es incorrecta.\n"

