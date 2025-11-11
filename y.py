data_curenta = '2025-11-11'
def zile_totale(data):
    parti = data.split('-')
    an = int(parti[0])
    luna = int(parti[1])
    zi = int(parti[2])
    return an*365 + luna*30 + zi
Produse = [
    ('Lapte','09.11.2025','23.11.2025',18,n),
    ('Iaurt','23.10.2025','19.11.2025',27,n),
    ('Cascaval','04.05.2025','08.09.2025',24,n),
    ('Ou','17.08.2025','01.12.2025',7,n),
    ('Carne','12.01.2025','12.05.2025',60,n)
]
