# RPS2-balohm

To je glavni repositorij profesorja za RPS predmet v 2. letniku.

# Virtualno okolje

## Windows CMD

1. Ustvarimo virtualno okolje s spodnjim ukazom.

```
py -m venv .venv
```

2. Aktiviramo virtualno okolje
```
.venv\Scripts\activate
```

3. Varno naložimo knjižnice, od katerih je projekt odvisen. Morda datoteke `requirements.txt` še nimamo.
```
cd dependencies
pip install -r requirements.txt
```

## Linux SHELL

Popolnoma enaki koraki kot zgoraj. Razen aktivacija / deaktivacija virtualnega okolja. Pomagaj si s kodo spodaj.
```
source venv/bin/activate
deactivate
```

# Projekt je odvisen od drugih projektov

Mi usvarjamo spletni projekt. Zato je naša koda odvisna od zelo pomembne knjižnice kot je `flask`. Več o njej izveste na spletni strani [Quickstart](https://flask.palletsprojects.com/en/stable/quickstart/).

Seveda bomo vsakič potrebovali naložiti knjižnico v naše okolje, da bo koda delovala. Morda še kakšno dodatno.

Da bi si delo olajšali si poglejmo spodnje trike.

## Dependencies

Pripravili si bomo spodnjo strukturo map in datotek, da bomo imeli shranjene knjižnice in nalaganje (inštalacija) bo enostavna.

```
moj-projekt/
├── dependencies/
│   ├── requirements.txt
├── .../
└── run.py
```
Vsebina datoteke `requirements.txt` naj bo za enkrat:
```
flask
mysql-connector-python
```
Morda v prihodnje dodamo še kakšno knjižnico. Pravično je da povemo, da so tukaj zabeležene knjižnice brez zaklenjene verzije in se bo vedno naložila najnovejša. Kar nam ustreza.

## Kaj pa sedaj?
Takoj ko je virtualno okolje postavljeno, lahko naložimo knjižnice. Pojdi na korak 3. v poglavju virtualno okolje.




