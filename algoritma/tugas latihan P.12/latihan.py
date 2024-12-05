# Membuat Set 
set1 = set() 
print("Set kosong awal: ") 
print(set1) 

# Membuat Set dengan menggunakan String 
set1 = set("UpbforUpb") 
print("\nAtur dengan menggunakan String: ") 
print(set1) 
String = 'UpbForUpb' 
set1 = set(String) 
print("\nAtur dengan menggunakan Object: ") 
print(set1) 

# Membuat Set dengan menggunakan Daftar 
set1 = set(["UPB", "For", "UPB"]) 
print("\nAtur dengan menggunakan Daftar: ") 
print(set1) 

# Membuat Set dengan menggunakan tuple 
t = ("Upb", "for", "Upb") 
print("\nAtur dengan menggunakan Tuple: ") 
print(set(t)) 

# Membuat Set dengan menggunakan kamus 
d = {"Upb": 1, "for": 2, "Upb": 3} 
print("\nDiatur dengan menggunakan Kamus: ") 
print(set(d)) 

# Membuat Himpunan dengan Daftar Angka 
# (Memiliki nilai duplikat) 
set1 = set([1, 2, 4, 4, 3, 3, 3, 6, 5]) 
print("\n Set dengan menggunakan Numbers: ") 
print(set1) 

# Membuat Set dengan jenis nilai campuran 
# (Memiliki angka dan string) 
set1 = set([1, 2, 'UPB', 4, 'For', 6, 'UPB']) 
print("\n Set dengan menggunakan Nilai Campuran") 
print(set1) 

# Penambahan elemen ke Set 
# menggunakan fungsi Update 
set1 = set([4, 5, (6, 7)]) 
set1.update([10, 11]) 
print("\n Set setelah Penambahan elemen menggunakan Update: ") 
print(set1)
