
# PROYEK KELOMPOK 4
## Implementasi Memento Pattern Menggunakan Linked Stack untuk Fitur Undo-Redo pada Aplikasi Teks Python

### 1. Deskripsi Proyek
Proyek ini merupakan implementasi struktur data Linked Stack dan konsep Object-Oriented Programming (OOP) menggunakan Memento Pattern untuk membangun fitur Undo dan Redo pada aplikasi editor teks sederhana berbasis Python.

Fitur Undo digunakan untuk mengembalikan teks ke kondisi sebelumnya, sedangkan Redo digunakan untuk mengembalikan perubahan yang telah dibatalkan.

### 2. Tujuan Proyek
1. Mengimplementasikan struktur data Linked Stack.
2. Menerapkan Memento Pattern dalam pemrograman berorientasi objek.
3. Membuat fitur Undo dan Redo pada aplikasi teks.
4. Melakukan pengujian otomatis menggunakan UnitTest.
5. Mengukur waktu eksekusi dan penggunaan memori program.

### 3. Fitur Utama
- Menambahkan teks.
- Mengubah isi teks.
- Menghapus teks.
- Undo (membatalkan perubahan).
- Redo (mengembalikan perubahan).
- Menyimpan riwayat perubahan menggunakan Linked Stack.
- Pengujian otomatis.
- Pengukuran performa program.

### 4. Teknologi yang Digunakan
- Bahasa pemrograman: Python
- Editor kode: Visual Studio Code
- Version Control: Git
- Repository: GitHub
- Testing: unittest
- Memory Profiling: tracemalloc
- Time Profiling: time

### 5. Struktur Folder Proyek

```text
KELOMPOK_4_UNDO_REDO/
│
├── main.py
├── node.py
├── linked_stack.py
├── memento.py
├── text_editor.py
├── history_manager.py
│
├── tests/
│   ├── test_linked_stack.py
│   ├── test_memento.py
│   └── test_undo_redo.py
│
├── benchmark/
│   ├── time_profiling.py
│   └── memory_profiling.py
│
├── README.md
└── requirements.txt
```

### 6. Cara Menjalankan Program

Pastikan Python sudah terinstal.

Buka terminal pada folder proyek, kemudian jalankan:

```bash
python main.py
```

### 7. Cara Menjalankan Pengujian

Untuk menjalankan seluruh pengujian otomatis:

```bash
python -m unittest discover -s tests -v
```

### 8. Pengukuran Performa

Pengukuran waktu eksekusi:

```bash
python benchmark/time_profiling.py
```

Pengukuran penggunaan memori:

```bash
python benchmark/memory_profiling.py
```

### 9. Anggota Kelompok

Kelompok 4:

1. Anggota 1: Maria Putri Purnama Azy
2. Anggota 2: Ginzia Rina Hobang
3. Anggota 3: Arsean Riada Bera
4. Anggota 4: Sutrisno Gande

### 10. Repository GitHub

Repository proyek:

https://github.com/putrypurnamaa-svg/TUGAS-STRUKTUR-DATA-UTS-KELOMPOK-4

### 11. Kesimpulan

Melalui proyek ini, mahasiswa mempelajari penerapan struktur data Linked Stack dan Memento Pattern untuk mengelola riwayat perubahan teks. Implementasi ini diharapkan dapat menghasilkan fitur Undo-Redo yang berjalan dengan baik serta dapat diuji dan dianalisis performanya.
