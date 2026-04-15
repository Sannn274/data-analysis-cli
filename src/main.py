import pandas as pd
import matplotlib.pyplot as plt

# load data
def load_data():
    while True:
        nama_file = input("Masukkan Nama File (contoh: sample.csv):")

        try:
            if not nama_file.endswith(".csv"):
                print("harus .csv cuy")
                continue

            df = pd.read_csv(nama_file)
            
            print("data berhasil ditemukan")
            print(f"jumlah data: {len(df)} baris")
            print(f"kolom: {list(df.columns)}")
            print(f"\nPreview data")
            print((df.head()))
            
            return df
        
        except FileNotFoundError:
            print("Data tidak di temukan")
        except pd.errors.EmptyDataError:
            print("File kosong, coba file lain")
        except Exception as e:
            print(f"Terjadi error: {e}") 


# Fitur 1 
def tampilkan_data(df):
    print("\n=== DATA ===")
    print(df)

# Fitur 2
def filter_umur(df):
    try:
        angka = int(input("\nMasukkan Batas Umur:"))
        hasil = df[df['umur'] >= angka]
        if hasil.empty:
            print("Hasil tidak ditemukan.")
        else:
            print("\nHasil Filter")
            print(hasil)

    except ValueError:
        print("Input nya harus angka cuy")

# Fitur 3
def statistik_data(df):
    print("\n=== Statistik Data ===")

    if 'umur' not in df.columns:
        print("kolom 'umur' tidak ditemukan")
        return
    
    print(f"Rata-rata Umur: {df['umur'].mean():.2f}")
    print(f"Umur Tertinggi, {df['umur'].max()}")
    print(f"Umur Terendah, {df['umur'].min()}")

# Fitur 4
def analisis_data(df):
    print("\n=== Analisis Data ===")

    if 'kota' not in df.columns:
        print("kolom 'kota' tidak di temukan.")
        return
    
    if df.empty:
        print("Data kosong.")
        return

    kota_terbanyak = df['kota'].value_counts().idxmax()
    jumlah = df['kota'].value_counts().max()

    print(f"Kota dengan jumlah orang terbanyak: {kota_terbanyak} ({jumlah} orang)")

# Fitur 5
def pencarian_nama(df):
    # Bebas bug case sensitivity
    nama = input("\nMasukkan  Nama: ").lower()
    hasil = df[df['nama'].str.lower().str.contains(nama, case=False, na=False)]
    if hasil.empty:
        print("Hasil tidak bisa ditemukan")
    else:
        print(hasil)

# Fitur 6
def export_data(df):
    df.to_csv("hasil.csv", index=False)
    print("Data berhasil di export")

# Fitur 7
def grafik_kota(df):
    if 'kota' not in df.columns:
        print("Kolom 'kota' tidak ditemukan.")
        return
    
    data = df['kota'].value_counts()

    plt.figure()
    data.plot(kind='bar')

    plt.title("Jumlah orang per Kota")
    plt.xlabel("Kota")
    plt.ylabel("jumlah")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("Grafik Kota.png")
    print("Grafik disimpan sebagai Grafik Kota.png")

# Fitur 8
def grafik_umur(df):
    if 'umur' not in df.columns:
        print("kolom 'umur' tidak ditemukan.")
        return
    
    plt.figure()
    df['umur'].plot(kind='hist', bins=5)

    plt.title("Distribusi Umur")
    plt.xlabel("Umur")
    plt.ylabel("Frekuensi")

    plt.tight_layout()
    
    plt.savefig("Grafik Umur")
    print("Grafik disimpan sebagai Grafik Umur.png")
    
# Menu
def menu():
    print("\n=== MENU ===")
    print("1. Tampilkan semua Data")
    print("2. Filter Umur")
    print("3. Statistik Data")
    print("4. Analisis Data")
    print("5. Pencarian Nama")
    print("6. export data")
    print("7. Grafik Kota")
    print("8. Grafik Umur")
    print("9. keluar")

# Main Program
def main():
    df = load_data()

    while True:
        menu()
        pilihan = input("Pilih Menu: ")

        if pilihan == "1":
            tampilkan_data(df)

        elif pilihan == "2":
            filter_umur(df)
        
        elif pilihan == "3":
            statistik_data(df)

        elif pilihan == "4":
            analisis_data(df)

        elif pilihan == "5":
            pencarian_nama(df)

        elif pilihan == "6":
            export_data(df)

        elif pilihan == "7":
            grafik_kota(df)

        elif pilihan == "8":
            grafik_umur(df)

        elif pilihan == "9":
            print("Keluar dari Program")
            break

        else:
            print("Pilih yang bener kodok")

# Entry Point 
if __name__ == "__main__":
    main()