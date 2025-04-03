from tabulate import tabulate

class Transaction():
    menu_frozen_food = {
    "nugget_ayam": {"nama": "Nugget Ayam 1kg", "harga": 75000},
    "sosis_sapi": {"nama": "Sosis Sapi Premium 500gr", "harga": 60000},
    "dimsum_ayam": {"nama": "Dimsum Ayam 20pcs", "harga": 85000},
    "ayam_karaage": {"nama": "Ayam Karaage 500gr", "harga": 65000},
    "spaghetti_carbonara": {"nama": "Spaghetti Carbonara (Frozen)", "harga": 45000},
    "kentang_goreng": {"nama": "Kentang Goreng Shoestring 1kg", "harga": 50000},
    "fish_stick": {"nama": "Fish Stick 500gr", "harga": 70000},
    "susu_almond": {"nama": "Susu Almond Homemade 1L", "harga": 65000}
    }

    def __init__(self):
        self.cart = {}

    def show_menu(self):
        # Menyiapkan data dalam format yang bisa diterima oleh tabulate
        tabel = [(item['nama'], item['harga']) for item in self.menu_frozen_food.values()]
        print(tabulate(tabel, headers=["Nama Item", "Harga"], tablefmt="grid"))

    def add_item(self, nama_barang, jumlah):
        nama_barang = nama_barang.lower()
        # Pastikan barang ada di menu sebelum ditambahkan
        if nama_barang in self.menu_frozen_food:
            if nama_barang in self.cart:
                # Jika barang sudah ada di keranjang, tambahkan jumlahnya
                self.cart[nama_barang]["jumlah"] += jumlah
            else:
                # Jika barang belum ada di keranjang, tambahkan sebagai item baru
                self.cart[nama_barang] = {
                    "nama": self.menu_frozen_food[nama_barang]["nama"],
                    "harga": self.menu_frozen_food[nama_barang]["harga"],
                    "jumlah": jumlah
                }
            print(f"{jumlah} {self.menu_frozen_food[nama_barang]['nama']} berhasil ditambahkan ke keranjang.")
        else:
            print("Barang tidak ditemukan dalam menu.")
        
    def check_order(self):
        if not self.cart:
            print("Keranjang belanja kosong.")
            return
        
        # Mengonversi data cart menjadi format tabulate
        tabel = [[item["nama"], item["harga"], item["jumlah"], item["harga"] * item["jumlah"]]
                for item in self.cart.values()]
            
        print(tabulate(tabel, headers=["Nama Item", "Harga Satuan", "Jumlah", "Total Harga"], tablefmt="grid"))
        print("Pesanan sudah benar." if tabel else "Terdapat kesalahan input data.")

    def delete_item(self, nama_item):
        """Menghapus item tertentu dari keranjang."""
        if nama_item in self.cart:
            del self.cart[nama_item]
            print(f"Item {nama_item} telah dihapus dari keranjang.")
        else:
            print(f"Item {nama_item} tidak ditemukan di keranjang.")

    def update_item_qty(self, nama_item, jumlah_baru):
        """Memperbarui jumlah item dalam keranjang."""
        if nama_item in self.cart:
            if jumlah_baru > 0:
                self.cart[nama_item]["jumlah"] = jumlah_baru
                print(f"Jumlah {nama_item} diperbarui menjadi {jumlah_baru}.")
            else:
                del self.cart[nama_item]
                print(f"Jumlah {nama_item} diubah menjadi 0, item dihapus dari keranjang.")
        else:
            print(f"Item {nama_item} tidak ditemukan di keranjang.")

    def reset_transaction(self):
        """Menghapus seluruh isi keranjang."""
        if not self.cart:
            print("Keranjang sudah kosong.")
        else:
            self.cart.clear()
            print("Semua pesanan telah dihapus.")

    def total_price(self):
        """Menghitung total harga belanjaan dan menerapkan diskon jika memenuhi syarat."""
        if not self.cart:
            print("Keranjang belanja kosong.")
            return

        # Menghitung total sebelum diskon
        total = sum(item["harga"] * item["jumlah"] for item in self.cart.values())

        # Menentukan diskon berdasarkan total belanja
        if total > 500000:
            diskon = 0.10  # 10%
        elif total > 300000:
            diskon = 0.08  # 8%
        elif total > 200000:
            diskon = 0.05  # 5%
        else:
            diskon = 0.00  # Tidak ada diskon

        # Menghitung harga setelah diskon
        potongan = total * diskon
        total_setelah_diskon = total - potongan

        # Menampilkan hasil
        print(f"Total sebelum diskon: Rp {total:,.0f}")
        if diskon > 0:
            print(f"Diskon ({diskon*100:.0f}%): Rp {potongan:,.0f}")
            print(f"Total setelah diskon: Rp {total_setelah_diskon:,.0f}")
        else:
            print("Tidak ada diskon yang diterapkan.")




user1 = Transaction()
user1.show_menu()
user1.add_item("dimsum_ayam", 8)
user1.add_item("fish_stick", 3)
user1.check_order()
user1.total_price()
