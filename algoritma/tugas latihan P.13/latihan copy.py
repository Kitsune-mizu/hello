Dict = {1: 'UPB', 2: 'For', 3: 'Word'}
print("\nkamus dengan menggunakan kunci integer: ")
print(Dict)

Dict = {'Name': 'UPB', 1: [1, 2, 3, 4]}
print("\nkamus dengan kombinasi kunci: ")
print(Dict)
print("\n")

Dict = {}
print("Contoh Kamus Kosong: ")
print(Dict)

Dict = dict({1: 'UPB', 2: 'For', 3: 'Word'})
print("\nKamus menggunakan Kamus(): ")
print(Dict)

Dict = dict([(1, 'UPB'), (2, 'Megah')])
print("\nKamus dengan beberapa item : ")
print(Dict)
print("\n")

Dict = {1: 'UPB', 2: 'Megah', 3: {'A': 'Welcome', 'B': 'To', 'C': 'UPB'}}
print(Dict)
print("\n")

Dict = {}
print("Empty Dictionary: ")
print(Dict)

Dict[1] = 'UPB'
Dict[2] = 'For'
Dict[3] = 1
print("\nKamus setelah menambahkan 3 elements: ")
print(Dict)

Dict['Value_set'] = 2, 3, 4
print("\nKamaus Setelah Menambahkan 3 elements: ")
print(Dict)

Dict[2] = 'Selamat Datang'
print("\nUpdated Kata Kuni Nilai : ")
print(Dict)

Dict[5] = {'Nested': {'1': 'Life', '2': 'Economic'}}
print("\nMenambahkan kunci bersarang: ")
print(Dict)
print("\n")

Dict = {1: 'NasiGoreng', 'name': 'For', 3: 'Nasi Bakar'}
print("Mengakses elemen dengan nama:")
print(Dict['name'])
print("Mengakses Elemen dengan Kunci:")
print(Dict[1])
print("\n")

Dict = {1: 'UPB', 'name': 'For', 3: 'Megah'}
print("Mengakses element dengan get:")
print(Dict.get(3))
print("\n")

Dict = {'Dict1': {1: 'UPB'},'Dict2': {'Name': 'Megah '}}
print(Dict['Dict1'])
print(Dict['Dict1'][1])
print(Dict['Dict2']['Name'])
print("\n")

Dict = {1: 'UPB', 'name': 'Megah ', 3: 'Jaya'}
print("Kamus =")
print(Dict)
del(Dict[1])
print("Data setelah di hapus=")
print(Dict)
print("\n")

dict1 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"}
dict2 = dict1.copy()
print(dict2)
dict1.clear()
print(dict1)
print(dict2.get(1))
print(dict2.items())
print(dict2.keys())
dict2.pop(4)
print(dict2)
dict2.popitem()
print(dict2)
dict2.update({3: "Scala"})
print(dict2)
print(dict2.values())
print("\n")
