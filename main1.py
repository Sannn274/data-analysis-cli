import pandas as pd

df = pd.read_csv('sample.csv')

while True:
    print('\n=== Menu ===')
    print('1. Tampilkan semua data')
    print('2. Filter Umur')
    print('3. Rata-rata umur')
    print('4. Keluar')

    pilihan = input('Pilih Menu: ')

    if pilihan == '1':
        print('\n === DATA ===')
        print(df)

    elif pilihan == '2':
        angka = int(input('Masukkan Batas Umur: '))
        hasil = df[df['umur'] >= angka]
        print('\n=== HASIL FILTER ===')
        print(hasil)

    elif pilihan == '3':
        print('\nRata-rata umur: ', df['umur'].mean())

    elif pilihan == '4':
        print('Keluar Program')
        break

    else:
        print('=== [PILIH YANG BENER KODOK] ===')
        break