data_curenta = '2025-11-11'

def zile_totale(data):
    parti = data.split('-')
    an = int(parti[0])
    luna = int(parti[1])
    zi = int(parti[2])
    return an * 365 + luna * 30 + zi

Produse = [
    ('Lapte','2025-11-09','2025-11-23',18),
    ('Iaurt','2025-10-23','2025-11-19',27),
    ('Cascaval','2025-05-04','2025-09-08',24),
    ('Ou','2025-08-17','2025-12-01',7),
    ('Carne','2025-01-12','2025-05-12',60)
]

zile_azi = zile_totale(data_curenta)

expirate = []
reducere20 = []
reducere50 = []
min1an = []
max1luna = []

for produs in Produse:
    nume, fabricatie, expirare, pret_initial = produs
    z_fabricatie = zile_totale(fabricatie)
    z_expirare = zile_totale(expirare)

    termen_total = z_expirare - z_fabricatie
    trecut = zile_azi - z_fabricatie
    ramas = z_expirare - zile_azi

    if zile_azi > z_expirare:
        pret_actual = 0
        expirate.append(nume)
    elif trecut >= termen_total / 2 and ramas > termen_total * 0.25:
        pret_actual = pret_initial * 0.8
        reducere20.append(nume)
    elif ramas <= termen_total * 0.25:
        pret_actual = pret_initial * 0.5
        reducere50.append(nume)
    else:
        pret_actual = pret_initial

    if termen_total >= 365:
        min1an.append(nume)
    if termen_total <= 30:
        max1luna.append(nume)

    print(f"{nume}: {pret_actual:.2f} lei")

print("\n--- Liste cerute ---")
print("a) Expirate:", expirate)
print("b) Reducere 50%:", reducere50)
print("c) Reducere 20%:", reducere20)
print("d) Valabilitate ≥ 1 an:", min1an)
print("e) Valabilitate ≤ 1 lună:", max1luna)
