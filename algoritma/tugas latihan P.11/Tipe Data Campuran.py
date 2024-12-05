# DeklarasiTuple
# Dengan Mutli tipe data
Tuple1 = (10, 'Welcome', 12, 'upb')
print("\nTuple dengan Campuran Tipe Data: ")
print(Tuple1)

# Membangun Tuple bersarang
Tuple1 = (0, 2, 4, 6, 8)
Tuple2 = ('python','vscode', 'upb')
Tuple3 = (Tuple1, Tuple2)
print("\nTuple with nested tuples: ")
print(Tuple3)

# Membuat tuple perulangan
Tuple1 = ('UPB',) * 5
print("\nTuple with perulangan: ")
print(Tuple1)

# Membuat tuple dengan pengulangan/loop
Tuple1 = ('Geeks')
n = 7
print("\nTuple dengan a loop")
for i in range(int(n)):
    Tuple1 = (Tuple1,)
print(Tuple1)
