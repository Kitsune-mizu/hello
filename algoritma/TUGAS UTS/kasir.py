class Barang:
    def __init__(self, kode, nama, harga, jumlah=1):
        self.kode = kode       # Kode barang (misalnya: B001, B002)
        self.nama = nama       # Nama barang (misalnya: Sabun, Shampoo)
        self.harga = harga     # Harga satuan barang (misalnya: 5000)
        self.jumlah = jumlah   # Jumlah barang yang dibeli (default 1)
    
    def total_harga(self):
        return self.harga * self.jumlah

class KeranjangBelanja:
    def __init__(self):
        self.barang_list = []  # List untuk menyimpan barang dalam keranjang
    
    # Menambah barang ke dalam keranjang
    def tambah_barang(self, barang):
        self.barang_list.append(barang)
    
    # Menampilkan daftar barang dalam keranjang
    def tampilkan_barang(self):
        if not self.barang_list:
            print("Keranjang belanja kosong.")
        else:
            print("Daftar Barang:")
            print(f"{'Kode':<10}{'Nama Barang':<30}{'Harga':<10}{'Jumlah':<10}{'Total Harga'}")
            for barang in self.barang_list:
                print(f"{barang.kode:<10}{self.format_nama_barang(barang.nama):<30}{barang.harga:<10}{barang.jumlah:<10}{barang.total_harga():<10}")
    
    # Menghitung total harga semua barang dalam keranjang
    def hitung_total(self):
        total = sum(barang.total_harga() for barang in self.barang_list)
        return total
    
    # Mencetak struk pembayaran
    def cetak_struk(self):
        if not self.barang_list:
            print("Keranjang belanja kosong.")
            return
        print("\n----- STRUK PEMBELIAN -----")
        print(f"{'Kode':<10}{'Nama Barang':<30}{'Harga':<10}{'Jumlah':<10}{'Total Harga'}")
        for barang in self.barang_list:
            print(f"{barang.kode:<10}{self.format_nama_barang(barang.nama):<30}{barang.harga:<10}{barang.jumlah:<10}{barang.total_harga():<10}")
        print("-" * 50)
        print(f"Total Harga: Rp. {self.hitung_total()}")
        print("Terima kasih atas kunjungan Anda!")

 # Fungsi untuk membatasi panjang nama barang
    def format_nama_barang(self, nama):
        # Batasi nama barang menjadi maksimal 30 karakter
        MAX_LENGTH = 30
        if len(nama) > MAX_LENGTH:
            return nama[:MAX_LENGTH] + "..."  # Potong nama jika terlalu panjang
        return nama  # Jika tidak panjang, tampilkan seperti biasa

# Daftar barang yang sudah ditentukan (contoh barang di toko)
barang_default = [
    Barang(kode="B001l", nama="Sabun.Lifebuoy,110gr :", harga=6300),
    Barang(kode="B001n", nama="Sabun.Nouvo,4x.100gr :", harga=14200),
    Barang(kode="B002k", nama="Shampoo.Kodomo,200ml :", harga=11900),
    Barang(kode="B002z", nama="Shampoo.Zinc,170ml :", harga=14900),
    Barang(kode="B003p", nama="Pasta Gigi.Pepsodent,190gr :", harga=25900),
    Barang(kode="B003c", nama="Pasta Gigi.Ciptadent,190gr :", harga=9900),
    Barang(kode="B004b", nama="Minyak Goreng.Bimoli,2l :", harga=37900),
    Barang(kode="B004s", nama="Minyak Goreng.Sania,1l :", harga=18700),
    Barang(kode="B005a", nama="Air Mineral.Aqua,1500ml :", harga=6600),
    Barang(kode="B005l", nama="Air Mineral.LeMinerale,1500ml :", harga=6500)
]

def main():
    keranjang = KeranjangBelanja()
    
    while True:
        print("\nMenu Kasir:")
        print("1. Tambah Barang dari Daftar")
        print("2. Tampilkan Daftar Barang dalam Keranjang")
        print("3. Hitung Total Harga")
        print("4. Cetak Struk")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == "1":
            
            # Menampilkan daftar barang yang tersedia
            print("\nDaftar Barang yang Tersedia:")
            print(f"{'Kode':<10}{'Nama Barang':<30}{'Harga'}")
            for barang in barang_default:
                print(f"{barang.kode:<10}{keranjang.format_nama_barang(barang.nama):<30}{barang.harga}")
            
            kode_barang = input("\nMasukkan kode barang yang ingin dibeli: ")
            
            # Mencari barang berdasarkan kode
            barang_dipilih = next((b for b in barang_default if b.kode == kode_barang), None)
            
            if barang_dipilih:
                jumlah = int(input(f"Masukkan jumlah {barang_dipilih.nama} yang ingin dibeli: "))

                # Menambah barang ke keranjang dengan jumlah yang dipilih
                barang_dipilih.jumlah = jumlah
                keranjang.tambah_barang(barang_dipilih)
                print(f"{barang_dipilih.nama} berhasil ditambahkan ke keranjang.")
            else:
                print("Barang dengan kode tersebut tidak ditemukan.")
        
        elif pilihan == "2":
            keranjang.tampilkan_barang()
        
        elif pilihan == "3":
            total = keranjang.hitung_total()
            print(f"Total harga semua barang: Rp. {total}")
        
        elif pilihan == "4":
            keranjang.cetak_struk()
        
        elif pilihan == "5":
            print("Terima kasih, sampai jumpa!")
            break
        
        else:
            print("Pilihan tidak valid, silakan pilih lagi.")

if __name__ == "__main__":
    main()
