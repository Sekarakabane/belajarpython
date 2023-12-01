# # for i in range (1, 6):
# #     print(i)
# #     for j in range (1, 6):
# #         print(i, "+", j, "=", int(i + j))

# # for i in range (1, 6):
# #     print(i)
# #     for j in range (1, 6):
# #         print(i, ":", j, "=", int(i / j))

# kumpulanbarang = [["meja", "kursi", "tatakan"], ["monitor", "TV", "handphone"]]
# for barang in kumpulanbarang:
#     for item in barang:
#         print(item, end=", ")
#     print()

# for i in range (1,26):
#     for j in range ():
#         print (j, end="")
#     print(j)
# print(i)

# for i in range(1,6):
#     for j in range(1,6):
#         print( i * j, end="\t")
#     print()

# for i in range(1,6):
#     for j in range(1, i + 1):
#         print( i * j, end="\t")
#     print()

# def menyapa(nama, tempat):
#     print("halooo", nama)
#     print("selamat datang di", tempat)

# menyapa("karma akabane", "hotel")

#soal 1


def hitung(angka1, angka2, operator):
   if(type(angka1) == int) and (type(angka2) == int):
      if(operator == "+"):
         return angka1 + angka2
      elif(operator == "-"):
         return angka1 - angka2
      elif(operator == "x" or operator == "*"):
         return angka1 * angka2
      elif(operator == "/" or operator == ":"):
         return angka1 / angka2
      else:
         return("operasi tidak valid")
   else:
      print("tipe data harus berupa angka (integer)")

print(hitung(30,5, "+"))

# def perulangan(nama, perulangan):
#     for i in range(perulangan):
#         print(nama)
# perulangan("i need you duan jiaxu, but i'm not sang zhi", 5)