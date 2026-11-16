# PROGRAM SIMULASI PINTU AIR

# Muhammad Fadhil / 16626083
# Gilang Maulana Ditrakusuma / 16626081
# Erland Elroy Aritonang / 16626157
# Rama Pandama / 16626225
# Fakultas/Sekolah	: Fakultas Teknik Sipil dan Lingkungan (FTSL)
# Kode Mata Kuliah	: WI1102
# Nama Mata Kuliah	: Berpikir Komputasional
# Judul Tugas		: Pengaturan Pintu Air Bendungan Menggunakan Python
# Menghitung tinggi muka air akhir untuk 4 variasi bukaan
# dan mencari bukaan yang paling mendekati target.


# KAMUS

# Spesifikasi: Menghitung tinggi muka air akhir bendungan untuk 4 variasi bukaan 
# pintu air (25%, 50%, 75%, 100%) dari kondisi awal yang sama dan menentukan 
# bukaan pintu yang menghasilkan tinggi air paling mendekati target.
# h_awal         : float         (tinggi muka air awal dalam satuan meter)
# h_target       : float         (tinggi muka air target yang diinginkan dalam meter)
# q_masuk        : float         (debit air yang masuk ke bendungan dalam m3/s)
# q_maks         : float         (debit keluar maksimum saat pintu dibuka 100% dalam m3/s)
# luas           : float         (luas penampang/permukaan bendungan dalam m2)
# waktu          : float         (interval waktu atau durasi simulasi dalam detik)
# daftar_bukaan  : array [0..3] of int (menyimpan 4 variasi persentase bukaan pintu air)
# i              : int           (indeks perulangan untuk mengakses elemen array, 0 sampai 3)
# bukaan         : int           (persentase bukaan pintu air pada skenario yang sedang dihitung)
# q_keluar       : float         (debit air yang keluar dari pintu pada skenario saat ini dalam m3/s)
# delta_v        : float         (perubahan volume air selama waktu dalam m3)
# delta_h        : float         (perubahan tinggi muka air dalam meter)
# h_akhir        : float         (prediksi tinggi muka air akhir pada skenario saat ini dalam meter)
# selisih        : float         (jarak mutlak antara h_akhir dengan h_target dalam meter)
# selisih_min    : float         (menyimpan nilai selisih terkecil dari skenario terbaik dalam meter)
# bukaan_terbaik : int           (menyimpan persentase bukaan yang paling mendekati target dalam %)
# h_terbaik      : float         (menyimpan prediksi tinggi akhir dari bukaan terbaik dalam meter)

# ALGORITMA

# 1. INPUT PARAMETER AWAL
print("SIMULASI TINGGI MUKA AIR BENDUNGAN")
print("Gunakan titik untuk angka desimal, misalnya 2.5")

h_awal = float(input("Tinggi muka air awal (m): "))
h_target = float(input("Tinggi muka air target (m): "))
q_masuk = float(input("Debit air masuk (m3/s): "))
q_maks = float(input("Debit keluar maksimum (m3/s): "))
luas = float(input("Luas permukaan bendungan (m2): "))
waktu = float(input("Interval waktu simulasi (detik): "))


# 2. INISIALISASI VARIABEL
daftar_bukaan = [25, 50, 75, 100]
selisih_min = 0.0
bukaan_terbaik = 0
h_terbaik = 0.0

print("\n--- HASIL SIMULASI TIAP SKENARIO ---")#/n digunakan untuk membuat baris baru


# 3. PERULANGAN UNTUK SETIAP SKENARIO
for i in range(4):
    bukaan = daftar_bukaan[i]

    # Menghitung debit keluar
    q_keluar = (bukaan / 100) * q_maks

    # Menghitung perubahan volume dan tinggi air
    delta_v = (q_masuk - q_keluar) * waktu
    delta_h = delta_v / luas

    # Menghitung tinggi akhir dari kondisi awal yang sama
    h_akhir = h_awal + delta_h

    # Menampilkan hasil skenario
    print("\nSkenario Bukaan", bukaan, "%")
    print("Debit keluar     :", q_keluar, "m3/s")
    print("Perubahan tinggi :", delta_h, "m")
    print("Tinggi akhir     :", h_akhir, "m")

    # Peringatan jika tinggi akhir negatif
    if h_akhir < 0:
        print("PERINGATAN: Tinggi air hasil perhitungan negatif!")

    # Menghitung selisih terhadap target (Nilai Mutlak Manual)
    selisih = h_akhir - h_target
    if selisih < 0:
        selisih = -selisih

    # Memeriksa apakah skenario ini paling mendekati target
    # Jika i == 0 (skenario pertama), langsung jadikan nilai awal terbaik
    if i == 0 or selisih < selisih_min:
        selisih_min = selisih
        bukaan_terbaik = bukaan
        h_terbaik = h_akhir


# 4. OUTPUT REKOMENDASI AKHIR
print("\n--- KESIMPULAN REKOMENDASI ---")
print("Bukaan pintu terbaik       :", bukaan_terbaik, "%")
print("Prediksi tinggi air akhir  :", h_terbaik, "m")
print("Selisih dari tinggi target :", selisih_min, "m")