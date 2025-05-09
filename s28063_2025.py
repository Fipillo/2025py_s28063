# Cel programu:
# Program generuje losową sekwencję DNA o zadanej długości, zapisuje ją w formacie FASTA
# i oblicza statystyki procentowe występowania nukleotydów. Imię użytkownika zostaje
# wstawione do sekwencji w losowym miejscu, ale nie jest uwzględniane w statystykach.

# Kontekst zastosowania:
# Program ten może być wykorzystywany do ćwiczeń z formatem FASTA w bioinformatyce,
# do generowania testowych danych sekwencyjnych i analizy składu nukleotydów.

import random

# Pobranie danych od użytkownika i sprawdzanie poprawności podanych danych
while True:
    length = int(input("Podaj długość sekwencji: "))
    if length <= 0:
        break

while True:
    seq_id = input("Podaj ID sekwencji: ")
    if not seq_id == "":
        break

while True:
    description = input("Podaj opis sekwencji: ")
    if not description == "":
        break

while True:
    name = input("Podaj imię: ")
    if not name == "":
        break

# Generowanie losowej sekwencji DNA
nucleotides = ['A', 'C', 'G', 'T']
sequence = ''.join(random.choices(nucleotides, k=length))

# Wstawienie imienia w losowym miejscu
insert_pos = random.randint(0, length)
sequence_with_name = sequence[:insert_pos] + name + sequence[insert_pos:]

# Zapis do pliku w formacie FASTA
filename = f"{seq_id}.fasta"
with open(filename, 'w') as file:
    file.write(f">{seq_id} {description}\n")
    file.write(sequence_with_name + "\n")

print(f"Sekwencja została zapisana do pliku {filename}")

# Obliczanie statystyk (na podstawie sekwencji bez imienia)
count_A = sequence.count('A')
count_C = sequence.count('C')
count_G = sequence.count('G')
count_T = sequence.count('T')

percent_A = (count_A / length) * 100
percent_C = (count_C / length) * 100
percent_G = (count_G / length) * 100
percent_T = (count_T / length) * 100

percent_CG = percent_C + percent_G

# Wyświetlenie statystyk
print("Statystyki sekwencji:")
print(f"A: {percent_A:.1f}%")
print(f"C: {percent_C:.1f}%")
print(f"G: {percent_G:.1f}%")
print(f"T: {percent_T:.1f}%")
print(f"%CG: {percent_CG:.1f}")
