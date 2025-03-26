#List Barang Toko
stok_toko = [
    ['Beras Sukatani', 'Sembako', '500gr', 10, 11000],
    ['Minyak Sawit Wangi', 'Sembako', '2L', 7, 26000],
    ['Hydrococo', 'Minuman', '1L', 22, 12000],
    ['Basreng Pedas 69', 'Cemilan', '150gr', 15, 5000],
    ['Air "Gunung Slamet"', 'Minuman', '5L', 20, 21000]
    ]

keranjang  = []

#Fungsi jika input tidak sesuai
def tempelate() :
    print('\n*****NOMOR TIDAK SESUAI, MASUKAN NOMOR YANG SESUAI*****')

#Stok Toko Dalam Bentuk Tabel
def tabel_stok(list) : 
    print('-'*28 + 'STOCK BARANG TOKO DOA IBU BAPAK' + '-'*28 )
    print('='*88)
    print(f'{'Nama Barang':<20} | {'Kategori':<10} | {'Kemasan':<10} | {'Stok Tersedia':<17} | {'Harga Barang Satuan':<25}')
    print('='*88)
    for baris in range(len(list)) :
        print(f'{list[baris][0] : <20} | {list[baris][1]:<10} | {list[baris][2]:<10} | {list[baris][3]:<17} | {list[baris][4]:<25}')

#Fungsi Read
def fungsi_read(list) : 
    while True :
        menu_read = (input('''                     
1. Tampilkan Semua Stok Barang
2. Kembali ke Menu Utama

Masukan nomor yang Sesuai : ''' ))
        if menu_read == '1' :
            print(tabel_stok(stok_toko))
        elif menu_read == '2' :
            break            
        else :
            tempelate()

#Fungsi Update
def fungsi_update(list) :
    print(tabel_stok(list))
    while True :
        menu_update = input('''
                       
1. Update List Stok Barang
2. Kembali ke Menu Sebelumnya
        
Masukan nomor yang sesuai : ''')
        if menu_update == '1' :
            tabel_stok(stok_toko)
            while True :
                update = input('Masukan nama Barang yang ingin diubah : ').capitalize()
                for update_barang in list :
                    if update in update_barang[0] :      
                        update_barang[3] = int(input(f'Masukan stok {update} yang baru. Stok lama = ({update_barang[3]}) : '))
                        update_barang[4] = int(input(f'Masukan harga {update} yang baru. Harga lama = ({update_barang[4]}) : '))
                        tabel_stok(stok_toko)
                        print('List barang berhasil diperbaharui.')
                        break                     
                else :
                    print('*****NAMA BARANG TIDAK DITEMUKAN, MASUKAN NAMA YANG BENAR*****')    
                lagi = input('\nIngin mengedit stok barang lagi? (Y/N) ')
                if lagi.lower() == 'n' :
                    break      
        elif menu_update == '2' :
            break
        else :
            tempelate()

#Fungsi Create
def fungsi_create(list) :
     while True :
        menu_create = input('''
                               
1. Tambahkan Stok Barang Baru
2. Kembali ke Menu Sebelumnya

Masukan nomor yang Sesuai : ''')
        if menu_create == '1' : 
            while True :
                nama = input('Masukkan nama barang : ').capitalize()
                cek_barang = False
                for tersedia in list :
                    if nama in tersedia[0] :
                       cek_barang = True
                if cek_barang :
                    pindah_menu = input('Barang sudah tersedia, Ingin ke menu Update untuk mengubah barang? (Y/N)')
                    if pindah_menu.upper() == 'Y' :
                        fungsi_update(list)
                    else :
                        print('BARANG GAGAL DISIMPAN')
                        break
                else :
                    kategori = input('Masukkan kategori barang : ').capitalize()
                    satuan = input('Masukkan satuan barang : ').capitalize()
                    stok = input('Masukkan stok barang : ')
                    harga = int(input('Masukkan harga barang : '))                                         
                    print(f'Anda memasukan {nama}, kategori {kategori} {satuan} sebanyak {stok} dengan harga {harga} per pcs.')
                    while True :
                        yakin = input('Apakah anda yakin? (Y/N)').upper()
                        if yakin == 'Y' :
                            stok_toko.append([nama, kategori, satuan, stok, harga])
                            tabel_stok(stok_toko)
                            print('BARANG BERHASIL DISIMPAN')
                            break
                        elif yakin == 'N' :
                            print('BARANG GAGAL DISIMPAN')
                            break
                        else :
                            print('Masukan format yang benar "(Y/N)"')
                lagi = input('\nIngin memasukkan barang lagi? (Y/N) ').upper()
                if lagi == 'N' :
                    break
        elif menu_create == '2' :
            break
        else :
            tempelate()

#Fungsi Delete
def fungsi_delete(list) :
    while True :
        menu_hapus = input('''
                       
1. Hapus Barang
2. Kembali ke Menu Sebelumnya
        
Masukan nomor yang sesuai : ''')
        if menu_hapus == '1' :
            print('-'*28 + 'STOCK BARANG TOKO DOA IBU BAPAK' + '-'*28 )
            print('='*88)
            print(f'{'Nama Barang':<20} | {'Kategori':<10} | {'Kemasan':<10} | {'Stok Tersedia':<17} | {'Harga Barang Satuan':<25}')
            print('='*88)
            for baris in range(len(list)) :
                print(f'{baris} | {list[baris][0] : <20} | {list[baris][1]:<10} | {list[baris][2]:<10} | {list[baris][3]:<17} | {list[baris][4]:<25}')
            hapus_barang = int(input('Masukan barang yang ingin dihapus : '))
            while True :
                yakin_hapus = input('Apakah anda yakin? (Y/N)')
                if yakin_hapus.upper() == 'Y' :
                    del list[hapus_barang]
                    tabel_stok(stok_toko)
                    break
                elif yakin_hapus.upper() == 'N' :
                    print('BARANG GAGAL DIHAPUS')
                    tabel_stok(stok_toko)
                    break
                else :
                    print('Masukan Format Yang Sesuai (Y/N)')
        elif menu_hapus == '2':
                break
        else :
            tempelate()

#Membuat login untuk akses admin
def password() :
    while True :
        print('KETIK E UNTUK KEMBALI KE MENU SEBELUMNYA')
        password = input('Masukan password admin : ')
        if password.upper() =='E':
            break
        elif password == '0000' :
            menu_admin()
        else :
            print('*****PASSWORD YANG ANDA MASUKAN SALAH. COBA LAGI*****')

#Membuat menu keranjang pembeli
def menu_keranjang(list) :
    print('-'*28 + 'STOCK BARANG TOKO DOA IBU BAPAK' + '-'*28 )
    print('='*88)
    print(f'{'Nama Barang':<20} | {'Kategori':<10} | {'Kemasan':<10} | {'Stok Tersedia':<17} | {'Harga Barang Satuan':<25}')
    print('='*88)
    for baris in range(len(list)) :
        print(f'{baris} | {list[baris][0] : <20} | {list[baris][1]:<10} | {list[baris][2]:<10} | {list[baris][3]:<17} | {list[baris][4]:<25}')
    while True :
        pembelian_barang = int(input('Masukan no barang yang ingin dibeli : '))
        jumlah_stok_barang = int(input('Masukan jumlah barang yang ingin dibeli : '))
        if jumlah_stok_barang > stok_toko[pembelian_barang][3] : 
            print(f'Stock {stok_toko[pembelian_barang][0]} hanya tersisa {stok_toko[pembelian_barang][3]} pcs.')
        elif jumlah_stok_barang <= 0 :
            print('Masukan jumlah yang benar : ')
        else :
            keranjang.append([stok_toko[pembelian_barang][0], jumlah_stok_barang, jumlah_stok_barang*stok_toko[pembelian_barang][4], pembelian_barang])
            print(f'{'Nama Barang':<20} | {'Banyak':<10} | {'Total':<10}')
            for barang in keranjang :
                print(f'{barang[0]:<20} | {barang[1]:<10} | {barang[2]:<10}')
        tambah_beli_buah = input('Apakah ingin menambahkan barang lain? (Y/N)')
        if tambah_beli_buah.lower() == 'n' :
            break
    total_harga = 0
    for jumlah in keranjang :
        total_harga += jumlah[2]
    print(f'Total pembelian anda sebesar {total_harga}')
    while True :
        bayar = int(input('Uang pembayaran: '))
        if bayar < total_harga :
            print(f'Uang anda kurang {total_harga-bayar}')
        elif bayar == total_harga :
            print(f'Uang anda pas')
            break
        else :
            print(f'Kembalian anda {bayar-total_harga}')
            break

#Menu admin
def menu_admin() :
    while True :
        pilihan = input(('''
Halo Admin 
                    
Menu Utama

1. Tampilkan List Barang Yang Tersedia
2. Tambah Barang Ke Dalam List
3. Edit List Barang
4. Hapus List Barang 
5. Keluar Dari Menu Utama  

Masukan nomor menu yang sesuai : '''))         
        if pilihan == '1' :
            fungsi_read(stok_toko)
        elif pilihan == '2' :
            fungsi_create(stok_toko)
        elif pilihan == '3' :
            fungsi_update(stok_toko)
        elif pilihan == '4' :
            fungsi_delete(stok_toko)
        elif pilihan == '5' :
            break
        else :
            tempelate()

#Menu Utama
def menu_login () :
     while True :
        user = input('''
TOKO DOA IBU BAPAK
        
Login sebagai :
1. Admin
2. Pembeli
3. Keluar program
                         
Masukan nomor yang sesuai : ''')
        if user == '1' :
            password()
        elif user == '2' :
            menu_keranjang(stok_toko)
        elif user == '3' :
            break
        else :
            tempelate()

print(menu_login())