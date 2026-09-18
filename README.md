# Pertemuan 03 Seleksi Python

## Identitas

Nama: Laila Fadhilah

NIM: 2225250030

Kelas: 3A

## Tujuan

Pada pertemuan ini saya mempelajari penggunaan struktur seleksi pada Python. Materi yang dipelajari meliputi percabangan `if`, `if-else`, kondisi majemuk, dan `nested if`. Struktur seleksi digunakan agar program dapat menentukan hasil berdasarkan kondisi atau nilai yang diberikan sebagai input.

## Cara Menjalankan

Program dapat dijalankan melalui terminal VS Code dengan perintah:

python tugas/analisis_persamaan_kuadrat.py

Pastikan terminal berada di dalam folder repository Pertemuan 03 sebelum menjalankan program.

## Algoritma Tugas

Program analisis persamaan kuadrat digunakan untuk menentukan jenis akar dari persamaan `ax² + bx + c = 0` berdasarkan nilai diskriminan.

Langkah-langkah keputusan program:
1. Pengguna memasukkan nilai koefisien a, b, dan c.
2. Program memeriksa apakah nilai a sama dengan 0.
3. Jika a sama dengan 0, program menampilkan bahwa input bukan persamaan kuadrat.
4. Jika a tidak sama dengan 0, program menghitung diskriminan dengan rumus D = b² - 4ac.
5. Jika D lebih besar dari 0, program menghitung dan menampilkan dua akar real yang berbeda.
6. Jika D sama dengan 0, program menghitung dan menampilkan satu akar real kembar.
7. Jika D kurang dari 0, program menampilkan bahwa tidak terdapat akar real.

## Hasil Pengujian

Pengujian dilakukan menggunakan beberapa nilai a, b, dan c untuk memastikan setiap kondisi pada program dapat berjalan sesuai dengan aturan yang telah dibuat.

Contoh pengujian:

- Input: a = 1, b = -5, c = 6
  Hasil yang diharapkan: D = 1.00 dan terdapat dua akar real yang berbeda.
  Hasil aktual: D = 1.00 dan diperoleh dua akar real, yaitu x1 = 3.00 dan x2 = 2.00.
  Status: Berhasil.

- Input: a = 1, b = 2, c = 1
  Hasil yang diharapkan: D = 0.00 dan terdapat satu akar real kembar.
  Hasil aktual: D = 0.00 dan diperoleh akar real kembar x = -1.00.
  Status: Berhasil.

- Input: a = 1, b = 0, c = 1
  Hasil yang diharapkan: D = -4.00 dan tidak terdapat akar real.
  Hasil aktual: D = -4.00 dan program menampilkan bahwa tidak ada akar real.
  Status: Berhasil.

- Input: a = 0, b = 2, c = 3
  Hasil yang diharapkan: Input dinyatakan bukan persamaan kuadrat.
  Hasil aktual: Program menampilkan "Bukan persamaan kuadrat."
  Status: Berhasil.

## Refleksi

Saat mengerjakan program, saya memahami bahwa penggunaan percabangan harus disesuaikan dengan kondisi yang ingin diperiksa. Kesalahan yang perlu diperhatikan adalah memastikan nilai a diperiksa terlebih dahulu sebelum menghitung diskriminan, karena jika a = 0 maka input tersebut bukan persamaan kuadrat. Selain itu, setiap kondisi diskriminan perlu diuji agar program dapat menghasilkan keluaran yang sesuai. Perbaikannya dilakukan dengan memeriksa setiap kondisi secara berurutan dan melakukan pengujian pada setiap cabang.