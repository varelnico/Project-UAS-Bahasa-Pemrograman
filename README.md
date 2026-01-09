Tugas ini untuk memenuhi Project UAS
## Nama    : Varel Nico Ramadhan
## Nim     : 312510156
## Kelas   : TI.25.A.2
## link youtube :[ https://youtu.be/m8sFWP174hY?si=h0hW6kWZ2-_BrEmw ](https://youtu.be/m8sFWP174hY?feature=shared)

## Program Manajemen Nilai Mahasiswa (OOP & Modular Programming)

---

Project ini merupakan program sederhana berbasis **Python** yang digunakan untuk mengelola data nilai mahasiswa.
Program dibuat dengan menerapkan konsep **Object Oriented Programming (OOP)** dan **Modular Programming**, di mana setiap bagian program dipisahkan ke dalam module sesuai dengan tanggung jawabnya.

Fitur utama program:

* Input data mahasiswa
* Validasi input menggunakan exception handling
* Pengolahan data nilai
* Menampilkan hasil dalam bentuk tabel

---

## Arsitektur Program

Program dibagi menjadi empat module utama:

```
project/
│
├── main.py
├── data_mahasiswa.py
├── process.py
└── view.py
```

Setiap module memiliki peran yang berbeda agar program lebih terstruktur dan mudah dipahami.

---

## Penjelasan Setiap Module

---

### `data_mahasiswa.py`

**Modul Data (Data Layer)**

Module ini berfungsi sebagai **penyimpanan dan pengelolaan data mahasiswa**.

#### Class `Mahasiswa`

Class ini digunakan untuk merepresentasikan objek mahasiswa dengan atribut:

* `nim`
* `nama`
* `nilai`

Class ini hanya menyimpan data dan tidak memiliki logika pemrosesan.

#### Class `DataMahasiswa`

Class ini berfungsi untuk:

* Menyimpan kumpulan data mahasiswa dalam bentuk list
* Menambahkan data mahasiswa baru
* Mengembalikan seluruh data mahasiswa yang tersimpan

Dengan adanya class ini, penyimpanan data dipisahkan dari proses dan tampilan.

---

### `process.py`

**Modul Proses / Logika Bisnis (Business Logic Layer)**

Module ini bertugas untuk **mengolah data mahasiswa**.

#### Class `NilaiProcess`

Class ini berisi logika untuk menentukan status kelulusan mahasiswa berdasarkan nilai:

* Nilai ≥ 75 → **LULUS**
* Nilai < 75 → **TIDAK LULUS**

Pemisahan logika ke dalam module ini membuat program lebih fleksibel jika aturan kelulusan ingin diubah di kemudian hari.

---

### `view.py`

**Modul Tampilan (View Layer)**

Module ini bertanggung jawab untuk **menampilkan output program ke layar**.

#### Class `Tampilan`

Class ini digunakan untuk:

* Menampilkan data mahasiswa dalam bentuk tabel
* Mengatur format tampilan agar rapi dan mudah dibaca

Module ini tidak melakukan pengolahan data, hanya menampilkan hasil akhir.

---

### `main.py`

**Modul Utama (Main Controller)**

Module ini merupakan **entry point** dari program dan satu-satunya file yang dijalankan.

Fungsi utama module ini:

* Mengatur alur program
* Menerima input dari pengguna
* Melakukan validasi input menggunakan exception handling
* Menghubungkan module data, process, dan view
* Menampilkan hasil akhir

Seluruh module lain dipanggil dan digunakan melalui file ini.

---

## Validasi Input

Program menerapkan **exception handling** untuk memastikan input yang dimasukkan pengguna valid, khususnya:

* Nilai harus berupa angka
* Nilai harus berada dalam rentang 0–100

Jika input tidak valid, program akan menampilkan pesan error dan meminta pengguna menginput ulang data.

---

## Cara Menjalankan Program

Pastikan seluruh file berada dalam satu folder, kemudian jalankan perintah berikut:

```
python main.py
```

Program akan meminta input data mahasiswa dan menampilkan hasil dalam bentuk tabel setelah selesai.

---------------------------------
