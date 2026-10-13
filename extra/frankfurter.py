

import requests
from decimal import Decimal


# Tečaji na dan 2026-10-05
# CHF: 0.9374
# GBP: 0.8712
# JPY: 172.41
# USD: 1.1683
# Skupaj valut: 4


def poklic_ga(base:str, symbols:list[str])->dict:
    url = "https://api.frankfurter.dev/v1/latest"
    parametri = {
        # iz katere valute
        "base": base,
        # v katere valute
        "symbols": ",".join(symbols)
    }
    odgovor = requests.get(url, params=parametri)
    
    # print(odgovor.url)
    return odgovor.json()

def poklic_datum(datumOd:str, datumDo:str, symbols:list[str]):
    url = f"https://api.frankfurter.dev/v1/{datumOd}..{datumDo}"
    parametri = {
        "symbols": ",".join(symbols)
    }
    odgovor = requests.get(url, params=parametri)
    
    print(odgovor.url)
    # print(odgovor.json())
    return odgovor.json()
   
def naloga1():
    odg = poklic_ga("EUR", ["CHF", "GBP", "JPY", "USD"])
    print(f"Tečaji na dan {odg['date']}")
    for k,v in odg['rates'].items():
        print(f"{k}: {v}")
    
def v_tujo(evri:float, valuta:str, rates:dict):
    print(f"{evri} EUR = {evri*rates[valuta]} {valuta}")

def v_evre(znesek:float, valuta:str, rates:dict):
    print(f"{znesek} {valuta} = {znesek/rates[valuta]} EUR")    

def naloga2():
    evri = int(input("Znesek v EUR: "))
    valuta = input("Valuta: ").strip().upper()
    odg = poklic_ga("EUR", [valuta])
    v_tujo(evri, valuta, odg['rates'])
    v_evre(evri, valuta, odg['rates'])

def naloga3():
    odg = poklic_datum("2026-09-01", "2026-09-08", ["USD"])
    
    odg["rates"]["2026-09-03"] = odg["rates"]["2026-09-04"]
    
    stara = False
    for k, v in odg['rates'].items():
        print(f"{k}: {v['USD']}", end=(" " if stara else "\n"))
        if stara and str(v['USD']) == str(stara):
            print("")
        else:
            print("gor") if v['USD'] > stara else print("dol")
        stara = float(v['USD'])
 
if __name__ == "__main__":
    # naloga1()
    # naloga2()
    naloga3()
    