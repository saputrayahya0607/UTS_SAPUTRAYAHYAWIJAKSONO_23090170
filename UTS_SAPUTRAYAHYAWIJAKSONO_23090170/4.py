def hitung_bmi(berat, tinggi):
    bmi = berat / (tinggi ** 2)
    return bmi

def kategori_bmi(bmi):
    if bmi < 18.5:
        return "berat badan kurang"
    elif 18.5 <= bmi < 24.9:
        return "berat badan normal"
    elif 25 <= bmi < 29.9:
        return "kelebihan berat badan"
    else:
        return "obesitas"

berat_badan = float(input("Masukkan berat badan (kg): "))
tinggi_badan = float(input("Masukkan tinggi badan (m): "))

bmi = hitung_bmi(berat_badan, tinggi_badan)
kategori = kategori_bmi(bmi)

print("Berat badan:", berat_badan, "kg")
print("Tinggi badan:", tinggi_badan, "m")
print("Nilai BMI Anda:", bmi)
print("Kategori BMI Anda:", kategori)