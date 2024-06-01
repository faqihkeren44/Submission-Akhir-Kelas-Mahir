# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan internasional yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Permasalahan Bisnis
Dengan berbagai macam cara mendaftar, seperti general contingent, special contingent, ordinance, dan lainnya, Jaya Jaya Institute menerima siswa dari berbagai negara, latar belakang keluarga, tingkat ekonomi, pendidikan, umur, dan lainnya. Inilah tantangan siswa dalam proses belajarnya, sehingga berakibat pada dropout.

Banyak siswa yang berstatus displaced sehingga kesulitan untuk melakukan pembayaran. Banyak juga siswa yang berhutang namun hutang ini tidak dipergunakan untuk melakukan pembayaran, sehingga memiliki tanggungan pembiayaan yang banyak. Oleh karena itu banyak siswa yang dropout dikarenakan pembiayaan yang kurang.

Curriculum unit yang dikreditkan banyak yang tidak diterima. Tidak diterimanya curriculum unit berjumlah 2 saja membuat sebagian siswa dropout, terlebih lagi jika yang tidak diterima berjumlah di atas 3.

Beasiswa merupakan salah satu daya tarik bagi siswa agar tetap bertahna hingga lulus. Namun penerima beasiswa belum tepat sasaran. Banyak siswa dengan ekonomi kurang atau nilai tingga tidak mendapat beasiswa. Beasiswa diberikan berdasarkan application mode.

### Cakupan Proyek
Analisis dilakukan dengan bantuan library pandas agar lebih memudahkan mengolahnya. Memang terdapat banyak data/feature, namun agar lebih fokus dan menghasilkan insight yang lebih baik, hanya 10 data/feature yang memiliki korelasi/hubungan tertinggi dengan status siswa. Tentunya data yang diolah adalah data yang bersih dari missing value atau duplikasi.

Adapula data yang tidak diketahui penjelasannya seperti Unemployment_rate, Inflation_rate, GDP, data-data ini tidak akan digunakan.

Harapannya, dengan selesainya proyek ini, akan terbuat dashboard yang dapat memberitahu penyebab dropout, dan model yang dapat memprediksi siswa mana yang berpotensi melakukan dropout. Sehingga Jaya Jaya Institute dapat lebih optimal mengurangi siswa dropout.

### Persiapan

Sumber data:
```
https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance
```

Setup environment - Anaconda:
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install numpy pandas scipy matplotlib seaborn jupyter streamlit
pip install scikit-learn==1.2.2
jupyter-notebook
```

## Business Dashboard
Dashboard dibuat hanya dengan data siswa yang dropout (Kecuali pie chart status), yaitu 18% data yang ada atau sebanyak 794 siswa dari total 4424 siswa.
Agar kolom pada chart Age_at_enrollment tidak banyak, umur siswa dikelompokkan dengan jarak 4,35 tahun.
Selain itu, nilai Curricular_unit pada semester 1 dan 2 tidak jauh, maka pada dashboard ini hanya menampilkan jumlah Curricular_unit semester 1 saja.

Pada dashboard ini, terdapat 2 bar chart yang memiliki warna berbeda, yaitu Tuition Feeds Up To Date dan Scholarship. Hal ini dibuat untuk memberitahu bahwa Tuition Feeds Up To Date berhubungan dengan status debtor. Begitu pula pada bar chart Scholarship, dibuat 2 warna berdasarkan jenis kelamin.

Dashboard ini dapat dilihat melalui link di bawah ini:
```
https://public.tableau.com/app/profile/alif.khusain.bilfaqih/viz/dashboard_17169966514310/Dashboard1?publish=yes
```

## Menjalankan Sistem Machine Learning
Untuk menampilkan mesin model klik tombol panah (>) di pojok kiri atas halaman. Pada tampilannya, ada beberapa inputan yang harus diisi, yaitu:

Gender: Jenis kelamin siswa (Man = Pria, Woman = Wanita)

Marital Status: Status pernikahan (Single = Belum menikah, Married = Menikah, Widower = Janda/Duda, Divorced = Cerai, Facto Union = Pernikahan tidak resmi, Legally Separated = Perceraian resmi)

Age At Enrollment: Usia siswa saat melakukan enrollment

Debtor: Apakah siswa memiliki tanggungan hutang?

Tuition Fees: Apakah siswa sudah melunasi pembayaran terkini?

Scholarship Holder: Apakah siswa mendapatkan beasiswa?

Displaced: Apakah siswa berasal dari keluarga kurang mampu?

Curriculum Unit: Jumlah Curriculum yang dikreditkan, dienrollment, disetujui, dan nilainya. Baik pada semester
```
https://submission-akhir-kelas-mahir-alu5zaagidoimnezg45veg.streamlit.app/
```

## Conclusion
Jaya Jaya Institute mencakup berbagai kalangan masyarakat. Yang paling menonjol yaitu dari siswi berusia 18-21 tahun. Adapun siswa laki-laki memiliki nilai curriculum unit yang rendah sehingga menjadi penyebab dropout.

Pengelolaan keuangan menjadi tantangan bagi siswa. Banyak siswa memiliki tanggungan hutang walaupun bukan termasuk Displaced dan mendapat beasiswa. 

### Rekomendasi Action Items
Beberapa rekomendasi action dapat dilakukan untuk menyelesaikan permasalahan dropout diantaranya:
- Beasiswa diberikan kepada siswa displaced atau memiliki tingkat pendapatan rendah, sehingga biaya tidak menjadi kenadala dalam belajar. Beasiswa juga dapat diberikan kepada siswa dengan nilai terbaik, sehingga semua siswa dapat berkompetensi untuk mendapatkannya dengan cara yang adil. Setelah mendapat beasiswa, siswa diberikan pelajaran khusus untuk mengatur keuangan agar beasiswa ini digunakan dengan baik dan tidak memiliki tanggungan hutang.
- Jumlah Curriculum_unit_enrolled harus dibatasi agar dapat diselesaikan semua dengan nilai terbaik. Jika siswa pada semester 1 dapat menyelesaikan curricular unit dengan baik, siswa tersebut berkesempatan mendapat jumlah Curriculum_unit_enrolled lebih banyak.
