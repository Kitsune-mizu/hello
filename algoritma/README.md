# pratikum2 Python3 (vs code)
# Menentukan bilangan terbesar dari 3 input bilangan 

//masukan input
num1 = int(input("masukan bilangan pertama:"))
num2 = int(input("masukan bilangan kedua:"))
num3 = int(input("masukan bilangan ketiga:"))
// mencari bilangan terbesar
if num1 > num2 and num1 > num3:
maks = num1
elif num2 > num3:
maks = num2
else:
maks = num3
print("Bilangan terbesar adalah", maks)

// Penjelasan
1. Baris 3,4,5 tempat untuk menyimpan bilangan yang akan di masukan dalam bentuk variabel num1, num2, num3 yang merupakan 3 bilangan yang akan di inputkan untuk mencari bilangan terbesar.
2. Baris 7-12 menggunakan perintah if untuk membuat sebuah pernyataan, elif atau singkatan “else dan if” untuk memeriksa secara berurutan, dan else untuk menyeleksi yang tidak memenuhi kondisi if. 
3. Baris 13 untuk menampilkan/mencetak hasil bilangan terbesar ke terminal. 
4. Saat program di jalankan akan ada perintah memasukan bilangan pertama yang akan disimpan di variabel num1, terus kedua num2 sampai ke tiga num3 dan akan di proses untuk mencari bilangan terbesar dari 3 bilangan yang dimasukan dan di simpan di variabel largest untuk di tampilkan hasil di terminal.

# Menentukan bilangan terbesar dari N, untuk menentukan jumlah N, berikan input angka 0

// Mencari bilangan N 
maks = 0 
while True:
  N = int(input("Masukkan number (0 untuk berhenti): "))
  if N == 0:
    break
  if maks is None or N > maks:
     maks = N
if maks is not None:
   print("Bilangan terbesar adalah:", maks)

// Penjelasan
1. Pada baris 32,  variabel maks sama dengan nol, kosong untuk menandai awal program. 
2. Pada baris 33-36, perintah perulangan While True yang membuat perulangan tak terbatas hingga perintah di berhentikan dengan Break, dengan memasukan bilangan 0 pada perintah input di terminal sebagai tanda berhenti. 
3. Dalam menjalankan program diperintahkan untuk memasukan bilangan dan enter untuk ketahap selanjutnya dengan program terus berulang sampai di masukan bilangan 0 untuk menyudahi proses dan menentukan hasil. 
4. Jika variabel maks masih (Nol) kosong atau angka yang baru yang di inputkan maka variabel maks akan diperbarui dengan bilangan tertinggi yang di inputkan. 
5. Setelah perulangan selesai dengan menginputkan bilangan 0 , nilai pada variabel maks di cetak atau di tampilkan dari hasil menentukan bilangan tertinggi yang di inputkan. 
