def sprawdz_pesel(pesel):
    # Wagi do obliczenia cyfry kontrolnej
    wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    
    suma = 0
    for i in range(10):
        suma += int(pesel[i]) * wagi[i]
    
    # Obliczamy cyfrę kontrolną
    kontrolna = (10 - (suma % 10)) % 10
    
    # Porównanie z ostatnią cyfrą numeru PESEL
    if kontrolna == int(pesel[10]):
        return 1
    else:
        return 0

# Przykład użycia
pesel = input("Podaj numer PESEL: ")
wynik = sprawdz_pesel(pesel)
print("Wynik:", wynik)