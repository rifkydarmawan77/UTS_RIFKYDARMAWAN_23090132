jumlah_barang = int(input("Masukkan jumlah barang = "))
harga_total = 0

for i in range(1, jumlah_barang + 1):
    harga = float(input("Masukkan harga barang ke-{}: ".format(i)))
    harga_total += harga

total_belanja = harga_total
print("total belanja : RP.", total_belanja) 