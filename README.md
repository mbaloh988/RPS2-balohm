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
.venv\Sripts\activate
```

3. Varno naložimo knjižnice, od katerih je projekt odvisen. Morda datoteke `requirements.txt` še nimamo.
```
cd dependencies
pip install -r requirements-noversion.txt
```

## Linux SHELL

Popolnoma enaki koraki kot zgoraj. Razen aktivacija / deaktivacija virtualnega okolja. Pomagaj si s kodo spodaj.
```
source venv/bin/activate
deactivate
```
