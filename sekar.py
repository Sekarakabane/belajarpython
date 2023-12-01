print("selamat datang di dafun")
nama = input("masukan namamu : ")
umur = input("masukan umurmu : ")
print("halo", nama, "selamat menikmati wahana di dafun\n")

print("daftar wahana")
daftar_wahana = ["1. biang lala RP. 13.000", "2. istana boneka RP. 10.000", "3. rumah kaca RP. 15.000", "4. roller coaster RP. 20.000"]
harga = 0
for wahana in daftar_wahana:
    print(wahana)

choose = int(input("pilih nomor wahana : "))
if choose == 1:
    print("Tiket RP. 13.000")
    harga += 13000
elif choose == 2:
    print("Tiket RP. 10.000")
    harga += 10000
elif choose == 3:
    print("Tiket RP. 15.000")
    harga += 15000
elif choose == 4:
    if int (umur < 18):
        print("anda tidak bisa menaiki wahana ini")
    else:
        print("Tiket RP. 20.000")
        harga += 20000
else:
    print("pilih yang benar")

print("+ pajak RP. 2.000")

pajak = int(2000)
total = (harga + pajak)
print("total keseluruhan yang harus kamu bayar adalah", total)



