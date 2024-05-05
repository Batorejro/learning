
print("Lista zakupów")

goods_list = {
'motoryzacyjnego': ["części", "kościoły", "błoto"],
'spozywczego': ['mąkę', 'mleko', 'ser'],
        # nie mogę 'z' z kropką zrobić
"drogerii": ["szampon", "proszek", "papugi"],
"kosmicznego": ['asteroidy', 'galaktyki', 'słońca']
}
print("teraz trochę poskładamy values")
ilosc_moto = len(goods_list['motoryzacyjnego'])
ilosc_spo = len(goods_list['spozywczego'])
ilosc_drog = len(goods_list['drogerii'])
ilosc_kosm = len(goods_list['kosmicznego'])
ilosc_towaru = ilosc_moto + ilosc_spo + ilosc_drog + ilosc_kosm
# print(ilosc_towaru)

for shop in goods_list:
    if shop in goods_list:
        print(f"Idę do {shop} i kupuję {goods_list[shop]} ")

print(f'Kupuję w sumie {ilosc_towaru} towarów.')

print("teraz będzie inaczej")
n_o_it = 0
print("Lista zakupow")
for shop, items in goods_list.items():
    print(f"Idę do {shop} i kupuje tam {', '.join(items)}.")
    n_o_it +=len(items)
print(f"Kupuję {n_o_it} towarów")
print("opopopopopoppopoppoppopo")
print("PALINDROMY ver. 1")
# cos innego

