import json

with open("tes.json", "r", encoding="utf-8") as file:
    data = json.load(file)

def barang_baru(nama, kategori, stock, harga):
    data.append({"Nama": nama, 
                "Kategori": kategori,
                "Stock": stock,
                "Harga": harga}
                ) 

while True:
    print("\n===== DATA INVENTARIS BARANG =====")
    print("1. Tampilkan data barang")
    print("2. Tambahkan data barang")
    print("3. Keluar") 

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
            for barang in data:
                print(f"Nama Barang: {barang['Nama']}, Kategori: {barang['Kategori']}, Stock: {barang['Stock']}, Harga: {barang['Harga']}")

    elif pilihan == "2":
        nama = input("Masukkan nama barang: ")
        kategori = input("Masukkan kategori barang: ")
        stock = int(input("Masukkan jumlah stock: "))
        harga = int(input("Masukkan harga barang: "))

        print(barang_baru(nama, kategori, stock, harga))
        
        with open("tes.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print("Data barang berhasil ditambahkan!")

    elif pilihan == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia!")