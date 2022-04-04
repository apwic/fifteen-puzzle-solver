# Fifteen Puzzle Solver using Branch and Bound
> Tugas Kecil Mata Kuliah IF2211 Strategi Algoritma ITB.

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Pembagian Tugas](#pembagian-tugas)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information
Branch and Bound digunakan dalam persoalan optimasi yaitu untuk meminimalkan atau memaksimalkan suatu fungsi objektif, yang tidak melanggar batasan dari persoalan. Dalam implementasinya algoritma Branch and Bound mirip antara gabungan antara Breadth First Search dengan Least Cost Search, perbedaan terhadap BFS ada dalam simpul yang diekspansinya. Setiap simpul pada Branch and Bound mempunyai sebuah cost untuk menaksirkan terhadap goal  yang ingin diraih. Untuk pembangkitan simpul berikutnya dipilih dari cost yang paling kecil (pada kasus minimasi). 

Algoritma Branch and Bound salah satunya digunakan untuk menyelesaikan permainan fifteen puzzle. Fifteen Puzzle (15 Puzzle) merupakan permainan dalam suatu “papan” dengan grid 4 x 4 yang berisikan angka dari 1 sampai 15 dan 1 tempat kosong. Elemen pada “papan” tersebut dapat diacak dan objektifnya adalah agar urutan dari elemen sesuai dengan urutan yang diinginkan. Urutan yang dipakai pada tugas kecil kali ini adalah urutan dari 1 sampai 15 dengan tempat kosong pada urutan terakhir.

## Technologies Used
- Python 3

## Features
- Fifteen Puzzle Solver

## Setup
- Pastikan sudah dilakukan clone atau _download_ terhadap repository ini
- Buka folder repository ini pada terminal
- Disarankan menggunakan virtualenv, Install terlebih dahulu virtualenv dengan _command_ pada terminal:
```
pip3 install virtualenv
virtualenv src
```
- virtualenv untuk folder src akan terbuat dan untuk mengaktifkannya lakukan _command_ pada terminal:
```
src\Scripts\activate
```
- Setelah virtualenv aktif, lakukan peng-_install_-an pada modul dengan melakukan _command_ pada terminal:
```
pip3 install -r requirements.txt
```
- _Command_ tersebut akan melakukan install terhadap _library_ yang dibutuhkan untuk menjalankan program
- Jika ingin menggunakan file csv tambahan silahkan tambahkan file csv tersebut ke folder test

## Usage
- Pastikan sudah dilakukan clone atau _download_ terhadap repository ini
- Buka folder repository ini pada terminal
- Aktifkan virtualenv dan jalankan program yang sudah dibuat dengan cara lakukan _command_ pada terminal:
```
src\Scripts\activate
python main.py
```
- Program akan berjalan dan silahkan masukkan input sesuai yang diminta oleh program
- Setelah selesai menggunakan program, matikan virtualenv dengan _command_ pada terminal:
```
deactivate
```


## Project Status
Project ini sudah  _selesai_ 

## Room for Improvement
Room for improvement:
- Sebagian dari source code yang ditulis itu _redundant_, sehingga bisa dilakukan pengecekan dan penghapusan terhadap beberapa code
- Projek ini terbatas deadline, sehingga code secara keseluruhan agak berantakan dan dapat dikembangkan lebih rapih lagi

## Acknowledgements
- Projek ini dikerjakan untuk memenuhi tugas kecil mata kuliah IF2211 Strategi Algoritma
- Terima kasih kepada seluruh dosen pengajar dan asisten mata kuliah IF2211 Strategi Algoritma

## Contact
Created by:
- [@apwic](https://github.com/apwic)
<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->
