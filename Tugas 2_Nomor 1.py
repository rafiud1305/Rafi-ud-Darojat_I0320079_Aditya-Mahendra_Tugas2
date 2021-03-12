from math import pi

print ("######################################")
print ("Tugas 2 Praktik Programa Komputer")
print ("######################################")
print ("Aplikasi Menghitung Suatu Hal Dengan Cepat")
print ("######################################")


print ("Pilihlah yang ingin anda hitung?")
print ("A. Luas Permukaan Kubus")
print ("B. Luas Persegi Panjang")
print ("C. Lingkaran")
print ("D. Celcius ke Fahrenheit")
print ("E. Reamur ke Celcius")

cetak = 0
choice = input("Masukkan pilihan anda (A/B/C/D/E): ")

if choice == "A":
    rsk = float(input("Masukkan rusuk kubus : "))
    Luas = 6*rsk*2

    print ("kubus tersebut memiliki luas permukaan sebesar {}" .format(Luas))
    cetak = 1

elif choice == "B":
    p = float(input("Masukkan Panjangnya : "))
    l = float(input("Masukkan lebarnya : "))
    Luas = p*l

    print ("Persegi panjang tersebut memiliki luas sebesar {}" .format(Luas))
    cetak = 1

elif choice == "C":
    r = float(input("Masukkan jari-jari : "))
    Luas = pi*r*r

    print ("Lingkaran tersebut memiliki luas sebesar {}" .format(Luas))
    cetak = 1

elif choice == "D":
    celcius = float(input("Masukkan suhunya : "))
    ckef = (9/5 * celcius) + 32

    print ("suhu {} celcius samadengan {} fahrenheit".format(celcius,ckef))
    cetak = 1

elif choice == "E":
    reamur = float(input("Masukkan suhunya : "))
    rkec = 5/4 * reamur

    print ("suhu {} reamur samadengan {} celcius".format(reamur,rkec))
    cetak = 1

else :
    print("input salah")