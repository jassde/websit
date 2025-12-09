import os

# Mapping: "old name": "new name"
rename_map = {
    "Anna Nooshin": "Anna_Nooshin",
    "Barbie Oh Oh Cherso": "Barbie_Oh_Oh_Cherso",
    "Bo Beljaars": "Bo_Beljaars",
    "Bridget Maasland": "Bridget_Maasland",
    "Dee van der Zeeuw": "Dee_van_der_Zeeuw",
    "Emma Wortelboer": "Emma_Wortelboer",
    "Fabiola Volkers": "Fabiola_Volkers",
    "Famke Louise": "Famke_Louise",
    "Genieve Fox": "Genieve_Fox",
    "Goedele Liekens": "Goedele_Liekens",
    "Gorgina Verbaan": "Gorgina_Verbaan",
    "Gwen van Poorten": "Gwen_van_Poorten",
    "Debby Zwiers": "Debby_Zwiers",
    "Heleen van Rooyen": "Heleen_van_Rooyen",
    "Iris Enthoven": "Iris_Enthoven",
    "Jade Anna van Vliet": "Jade_Anna_van_Vliet",
    "Juultje Tieleman": "Juultje_Tieleman",
    "Kaat": "Kaat",
    "Kim Holland": "Kim_Holland",
    "Lieke Klaver": "Lieke_Klaver",
    "Lies Zhara": "Lies_Zhara",
    "Mandy Praet_files": "Mandy_Praet",
    "Marieke Elsinga": "Marieke_Elsinga",
    "Marit Brugman": "Marit_Brugman",
    "Melanie Latooy": "Melanie_Latooy",
    "Michella Kox": "Michella_Kox",
    "Monica Geuze": "Monica_Geuze",
    "Nienke Plas": "Nienke_Plas",
    "Nina Warink": "Nina_Warink",
    "Nochtli Peralta Alvarez": "Nochtli_Peralta_Alvarez",
    "Onnedi": "Onnedi",
    "Rhode Kok": "Rhode_Kok",
    "Sophie Milzink": "Sophie_Milzink",
    "Sophie Ousri": "Sophie_Ousri",
    "Tatjana Simic": "Tatjana_Simic",
    "Yolanthe Cabau": "Yolanthe_Cabau",
    "Zimra Geurtss": "Zimra_Geurtss",
}

# Get current directory
base_path = os.getcwd()

for old, new in rename_map.items():
    old_path = os.path.join(base_path, old)
    new_path = os.path.join(base_path, new)

    if os.path.isdir(old_path):
        print(f"Renaming: {old} → {new}")
        os.rename(old_path, new_path)
    else:
        print(f"Skipping (not found): {old}")

print("\nDone!")
