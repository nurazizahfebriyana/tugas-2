Nama    : Nur Azizah Febriyana
NPM     : 2206824363
Kelas   : PBP-B

**TUGAS-2**
link app : https://kwangyaaa.adaptable.app/
link repo : https://github.com/nurazizahfebriyana/tugas-2.git 

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Cara pengimplementasiaan yang telah dilakukan:
**Buat proyek django baru**
    1. Melakukan konfigurasi awal git dengan membuat direktori 'tugas_2' tempat file-file tugas 2 disimpan, kemudian inisiasi direktori dengan 'git init'.
    2. Konfigurasi username dan surel (email) dengan 'git config user.name' dan 'git config user.email'
    3. Verifikasi konfigruasi dengan 'git config --list --local'
    4. Menghubungkan repo lokal dengan github dengan 'git branch -M main', kemudian 'git remote add origin <link repo github>'
    5. Mengaktifkan virtual environment 'python -m venv env' lalu 'env\Scripts\activate.bat'
    6. Membuat file txt yaitu requirements.txt yang berisi :
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    7. Memasang dependency 'pip install -r requirements.txt' dan membuat proyek django yaitu inventory dengan 'django-admin startproject inventory .'
    8. Mengonfigurasi proyek dan menjalankan server:
        -pada seetings.py menambahkan "*" di dalam [] ALLOWED_HOST.
        -Menjalankan server 'python manage.py runserver'
        -menonaktifkan server dengan CTRL+C terlebih dahulu kemudian deactivate.
    9. Membuat direktori di github 'tugas-2' kemudian diinisiasi dengan git brance, git remote add origin <URL>.
    10. Membuat .gitignore dalam tugas_2, lalu melakukan git add, commit, dan push.

**Routing proyek dan menjalankan aplikasi**
    1. Mengaktifkan virtual environment
    2. Membuat aplikasi main dengan 'python manage.py startapp main'
    3. Pada folder main terdapat settings.py lalu tambahkan 'main' pada bagian INSTALLED_APP.
    4. Buat direktori templates, yang didalamnya ada main.html dan mengisinya dengan format isi dari aplikasinya.
    5. Buka main.html dalam template di peramban web
    
**Membuat model pada aplikasi main**
    1.Mengubah models.py di bagian class nya sesuai dengan format soal:
        -name sebagai nama item dengan tipe CharField.
        -price sebagai harga itemnya dengan tipe CharField.
        -description sebagai deskripsi item dengan tipe TextField.
        -amount sebagai jumlah item dengan tipe IntegerField.
    2. Melakukan migrasi model yaitu 'python manage.py makemigrations' kemudian 'python manage.py migrate'.

**Membuat sebuah fungsi pada views.py**
    1. pada views.py tambahkan 'from django.shortcuts import render' dan juga fungsi show_main sebagai berikut:
    def show_main(request):
    context = {
        'name': 'NCT THE 4th ALBUM \'THE GOLDEN AGE\' Photobook ver.',
        'price': 'Rp 300.000,00',
        'description': 'Get a taste of NCT\'s diverse combination, transformation, and infinite synergy from the participating 20 members from NCT 127, NCT DREAM, and WayV.',
        'amount': 100

    }
    return render(request, "main.html", context)

    2. Memodif template di main.html menjadi :
    <h1>Kwangya Store</h1>

    <h5>Product Name: </h5>
    <p>{{name}}</p> <!-- Ubahlah sesuai dengan nama kamu -->
    <h5>Price: </h5>
    <p>{{price}}</p> <!-- Ubahlah sesuai dengan kelas kamu -->
    <h5>Description: </h5>
    <p>{{description}}</p>
    <h5>Stock: </h5>
    <p>{{amount}}</p>

**Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.** 
    1. Pada urls.py di main, menambahkan kode ini:
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    2. Mengonfigurasi Routing URL proyek dengan menambahkan 'from django.urls import path, include'
    3. Menambahkan rute URL pada bagian urlpatterns 'path('main/', include('main.urls')),'
    4. Menjalankan server dan membuka link peramban web
    5. deactivate server
    6. melakukan git add, commit, push sebelum deploy

**Deployment pada Adaptable**
    Melakukan deploy sesuai dengan tahap yang sama dengan tutorial.

**Mengisi README**    
**Menambahkan test**

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![This is an image](/Bagan_Request_Client_NurAzizahFebriyana.jpg)


Hubungan antara berkas urls.py, views.py, models.py, dan berkas HTML dalam sebuah aplikasi web adalah sebagai berikut: urls.py digunakan untuk mengatur bagaimana argumen yang dikirim oleh pengguna akan diarahkan ke views.py. Berkas HTML, yang berisi tampilan dan template web, akan menerima data dari views.py dan menghasilkan output yang diperlukan. Selanjutnya, ketika terjadi permintaan untuk mengambil atau memanipulasi data dari database, views.py akan berkomunikasi dengan models.py untuk menjembatani akses ke database tersebut. Setelah data diperoleh, views.py akan menggabungkan dan memprosesnya sesuai kebutuhan sehingga dapat ditampilkan sebagai satu halaman web yang lengkap dan sesuai dengan permintaan pengguna.

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
- Virtual environment digunakan untuk mengisolasi package dan dependency dari sebuah aplikasi agar tidak saling bertabrakan dengan versi yang mungkin berbeda yang terdapat pada sistem komputer. Ini berguna untuk memastikan bahwa ketika kita melakukan pembaruan pada suatu library di salah satu proyek, versi library tersebut tidak akan berubah di proyek lainnya.

- Pembuatan aplikasi web berbasis django bisa saja tidak menggunakan virtual environment. Namun hal tersebut bisa dibilang praktik yang kurang baik karena dengan virtul environment kita dapat lebih mengisolasi, mengorganisasi, serta mengelola proyek yang kita buat sehingga dapat mencegah adanya masalah yang dapat terjadi akibat adanya dependensi dan memastikan stabilitas dan keberlanjutan proyek yang telah dibuat.

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
    - MVC atau Model View Controller adalah sebuah pola arsitektur dalam pengembangan sistem web yang terdiri dari tiga elemen utama:

        1. Model: Ini adalah komponen yang bertanggung jawab untuk mengelola data dan berinteraksi langsung dengan basis data.

        2. View: Bagian ini bertugas untuk menampilkan informasi kepada pengguna dengan cara yang sesuai.

        3. Controller: Elemen ini berperan sebagai penghubung antara Model dan View ketika ada permintaan dari pengguna.

    Pola arsitektur ini membantu dalam mengatur dan memisahkan tanggung jawab masing-masing elemen dalam pengembangan situs web.

    - MVT atau Model View Template adalah varian dari MVC yang sering digunakan dalam kerangka kerja web Django. Dalam MVT, Template digunakan untuk mengelola tampilan, yang memisahkan tampilan dari logika bisnis aplikasi. Model menangani data dan logika bisnis, sedangkan View mengatur tampilan dan menghubungkan Model dan Template.
        1. Model: Mirip dengan MVC, ini adalah komponen yang mengelola data dan logika bisnis.

        2. View: Menampilkan data kepada pengguna dan menanggapi permintaan dari pengguna.

        3. Template: Mengatur tampilan (UI) dan format data yang akan ditampilkan.

    - MVVM  atau Model View ViewModel adalah pola arsitektur yang sering digunakan dalam pengembangan aplikasi berbasis antarmuka pengguna (UI) yang kompleks, terutama dalam kerangka kerja seperti Angular atau Vue.js. ViewModel memainkan peran penting dalam memisahkan logika tampilan (View) dari logika bisnis (Model) dengan memungkinkan komunikasi dua arah antara Model dan View. 
        1. Model: Mirip dengan definisi dalam MVC dan MVT, ini mengelola data dan logika bisnis.

        2. View: Menampilkan data dan mengirim input pengguna ke ViewModel.

        3. ViewModel: Berfungsi sebagai perantara antara Model dan View. Ini mengubah data dari Model ke format yang dapat ditampilkan oleh View dan merespons input dari pengguna.

    - **Perbedaan** dari ketiganya adalah dari bagaimana mereka mengelola tampilan dan alur kontrol dalam aplikasi. MVC memiliki kontroler yang mengendalikan alur, MVT menggunakan Template untuk mengatur tampilan, dan MVVM memiliki ViewModel yang bertindak sebagai perantara antara Model dan View. Pemilihan pola tergantung pada jenis aplikasi yang dikembangkan dan kerangka kerja yang digunakan, serta preferensi dan kebutuhan spesifik proyek yang dibuat.


========================================================================================================================================================================================================================================================================
Nama    : Nur Azizah Febriyana
NPM     : 2206824363
Kelas   : PBP-B

**TUGAS-3**

1. Apa perbedaan antara form POST dan form GET dalam Django?
    **form POST**
    Digunakan untuk mengirim data ke server untuk mengolahnya.Jika berhasil, maka akan mengembalikan kode status HTTP 201. Metode ini tidak menampilkan nilai variabel (data) pada URL sehingga lebih aman. Pada metode POST ini juga tidak memiliki batasan panjang data sehingga data yang dikirim dapat lebih besar.

    **form GET**
    Digunakan untuk mengambil data dari server tanpa mengubahnya.GET mengembalikan HTTP kode status 200 (OK) jika data berhasil diambil dari server. Metode ini menampilkan nilai variabel (data) pada URL sehingga kurang aman bila digunakan untuk mengirim data yang penting seperti password. Metode ini memiliki batasan panjang data sehingga tidak disarankan untuk digunakan dalam mengirim data yang besar atau sensitif.


2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
    **XML**
    -Format fleksibel untuk struktur data hierarkis dengan penggunaan tag dan atribut.
    -Sintaksis kompleks, cocok untuk data dengan struktur rumit.
    -Digunakan untuk representasi data fleksibel dalam berbagai konteks, seperti konfigurasi berkas dan pertukaran data antar aplikasi.
    
    **JSON**
    -Format pertukaran data sederhana berdasarkan pasangan "key-value" untuk data terstruktur.
    -Sintaksis sederhana dan mudah dibaca, populer dalam pertukaran data web.
    -Digunakan untuk pertukaran data dalam lingkungan web dan aplikasi, terutama dalam API RESTful.

    **HTML**
    -Bahasa markup khusus untuk membuat halaman web dengan elemen-elemen seperti teks, gambar, dan formulir.
    -Sintaksis khusus untuk peramban web, tidak selalu mudah dibaca oleh manusia dalam bentuk sumber.
    -Digunakan untuk membuat halaman web yang dapat dilihat oleh peramban web, terutama untuk antarmuka pengguna web.
    
3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
    Ini disebabkan oleh kecenderungan JSON untuk memiliki pertukaran data yang efisien dan dapat dengan mudah diinterpretasikan oleh komputer maupun manusia. Hal ini terjadi karena JSON menggunakan kombinasi kode yang sederhana untuk membentuk array, yang dapat dengan mudah dibuat dan dimengerti. JSON juga memiliki banyak kegunaan dalam mendukung perancangan aplikasi di perguruan tinggi, terutama saat menggunakan metode RESTful API dan Layanan Web.

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    **Membuat input form untuk menambahkan objek model pada app sebelumnya**
    1. Mengaktifkan virtual environment dan melakukan set routing dari main/ ke / pada urlpattern

    2. Mengimplementasi skeleton sebagai kerangka views dengan membuat file html bernama base.html pada root folder dan pada file settings.py pada subdirektori inventory menambahkan potongan kode ini:
    'DIRS': [BASE_DIR / 'templates'],
    pada baris yang mengandung TEMPLATES. Pada file main.html di subdirektori templates di main mengubahnya menjadi :
        {% extends 'base.html' %}

        {% block content %}

            <h3>Nama: </h3>
            <p>{{nama}}</p>
            <h3>Kelas: </h3>
            <p>{{kelas}}</p>

    
            <h1>Kwangya Store</h1>

            <h5>Product Name: </h5>
            <p>{{name}}</p> 
            <h5>Price: </h5>
            <p>{{price}}</p> 
            <h5>Description: </h5>
            <p>{{description}}</p>
            <h5>Stock: </h5>
            <p>{{amount}}</p>
        {% endblock content %} 

    3. Membuat input form dengan membuat file forms.py pad direktori main :
    from django.forms import ModelForm
    from main.models import Item

    class ProductForm(ModelForm):
        class Meta:
            model = Item
            fields = ["name", "price", "description", "amount"]
    
    Selain itu juga menambahkan beberaoa import dan fungsi baru yakni create_product(request) di file views.py pada folder main dimana fungsi tersebut menerima parameter request serta mengubah sedikit pada fungsi show_main(request).

    4. Menambahkan import fungsi create_product di urls.py pada forder main, serta menambahkan path urlnya juga.

    5. Membuat berkas HTML baru dengan nama create_product.html pada direktori main/templates:
    {% extends 'base.html' %} 

    {% block content %}
    <h1>Add New Product</h1>

    <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td>
                    <input type="submit" value="Add Product"/>
                </td>
            </tr>
        </table>
    </form>

    {% endblock %}

    6. Pada main.html, menambahkan kode di dalam {% block content %} yaitu :
    <table>
        <tr>
            <th>Product Name</th>
            <th>Price</th>
            <th>Description</th>
            <th>Stock</th>
            <th>Date Added</th>
        </tr>
    
        {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}
    
        {% for product in products %}
            <tr>
                <td>{{product.name}}</td>
                <td>{{product.price}}</td>
                <td>{{product.description}}</td>
                <td>{{product.amount}}</td>
                <td>{{product.date_added}}</td>
            </tr>
        {% endfor %}
    </table>
    
    <br />
    
    <a href="{% url 'main:create_product' %}">
        <button>
            Add New Product
        </button>
    </a>
    7. Mencoba menambahkan beberapa item baru melalui link local host.
    
    **Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID**
    Pada tahap sebelumnya fungsi view dalam format sudah dibuat, tersisa format XML, JSON, XML by ID dan JSON by ID.
    1. Menambahkan import pada views.py di folder main yaitu import HttpResponse dan Serializer. lalu menambahkan fungsi yang menerima parameter request dan return HttpResponse yakni:
    def show_xml(request):
        data = Item.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml") 
    Kemudian pada urls.py di main juga menambahkan import show_xml nya dan menambahkan path url di urlpatterns. Mencoba runserver dan buka link local host xml nya.

    2. Menambahkan fungsi yang menerima parameter request dan return HttpResponse yakni:
    def show_json(request):
        data = Item.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    Kemudian pada urls.py di main juga ditambah import show_json dan path url di urlpatterns. Mencoba runserver dan buka link local host json nya.

    3. Menambahkan fungsi yang menerima parameter dan id yang return berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi JSON atau XML dan parameter content_type dengan value "application/xml" atau"application/json" yakni :

    def show_xml_by_id(request, id):
        data = Item.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json_by_id(request, id):
        data = Item.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

    Kemudian pada urls.py di main ditambahkan import fungsi show_xml_by_id dan show_json_by_id serta path url di urlpatterns. Mencoba runserver dan buka link local host xml by id dan json by id.


    **Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2**
    Menambahkan ID contoh pada akhiran URL nya. Pada proyek ini, saya telah menambahkan 2 produk item. Jika saya ingin melihat produk yang pertama saya tambahkan, maka saya hanya perlu menambahkan /1 pada akhiran URL di formatnya baik xml by id atau json by id.

    **Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md**
    Membuka postman dengan memastikan bahwa server sudah berjalan. Kemudian, klik "GET" dan copy link localhost pada setiap format dan klik "SEND" untuk melihat response dari request yang dikirim.

    Lampiran foto screenshoot:
    ![This is an image](/Screenshot_Format_HTML.jpg)
    ![This is an image](/Screenshot_Format_XML.jpg)
    ![This is an image](/Screenshot_Format_JSON.jpg)
    ![This is an image](/Screenshot_Format_XML_by_ID.jpg)
    ![This is an image](/Screenshot_Format_JSON_by_ID.jpg)

    **Melakukan add-commit-push ke GitHub**

