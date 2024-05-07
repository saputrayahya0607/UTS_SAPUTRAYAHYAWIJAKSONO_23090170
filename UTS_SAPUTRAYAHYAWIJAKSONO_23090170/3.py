def hitung_total(harga_barang):
    total_harga = sum(harga_barang)
    return total_harga

jumlah_barang = int(input("Masukkan jumlah barang: "))

harga_barang = []
for i in range(jumlah_barang):
    harga = float(input(f"Masukkan harga barang ke-{i+1}: "))
    harga_barang.append(harga)

total_harga = hitung_total(harga_barang)

print(f"Total belanjaan: Rp {total_harga}")