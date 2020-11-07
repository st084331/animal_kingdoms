import csv

Bacteria = []
Archaea = []
Protista = []
Chromista = []
Plants = []
Animals = []
Fungi = []
Viruses = []

type_of_diet = []
cyst_formation = []
chitin = []
core_alability = []
presence_of_pseudomurein = []
eterna_growth = []
chlorophyll_type = []

# Чтение csv файла и рассортировка данных
with open('animals - Лист1.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        type_of_diet.append(row['type_of_diet'])
        cyst_formation.append(row['cyst_formation'])
        chitin.append(row['chitin'])
        core_alability.append(row['core_alability'])
        presence_of_pseudomurein.append(row['presence_of_pseudomurein'])
        eterna_growth.append(row['eterna_growth'])
        chlorophyll_type.append(row['chlorophyll_type'])


