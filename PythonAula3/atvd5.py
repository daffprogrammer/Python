BandaLista = ["banda", "musica"]
Banda = dict.fromkeys(BandaLista)

Banda["banda"] = "iron maiden"
Banda["musica"] = "powerslave"
print (Banda.get("banda"))
print (Banda.get("integrantes", "sem infomação dos integrantes"))
print (Banda)