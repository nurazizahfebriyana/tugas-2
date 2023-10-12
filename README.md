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



========================================================================================================================================================================================================================================================================
Nama    : Nur Azizah Febriyana
NPM     : 2206824363
Kelas   : PBP-B

**TUGAS-4**

1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
    Django UserCreationForm adalah impor formulir bawaan yang memudahkan pembuatan formulir pendaftaran pengguna dalam aplikasi web. Dengan diimpornya formulir ini, pengguna baru dapat melakukan register atau pendaftaran dengan mudah melalui di situs web tanpa melakukan penulisan kode dari awal.

    **Kelebihan**
    - Mudah dalam pembuatan akun user baru
    - Terdapat validasi bawaan untuk verifikasi email atau kata sandi yang sudah sesuai dengan standar keamanan
    -Mudah menambahkan Captcha yang melindungi aplikasi dari serangan bot
    -Proses penyimpanan data lebih mudah karena sudah memiliki integrasi yang baik dengan model user django

    **Kekurangan**
    - Keterbatasan dalam kustomisasi
    - Tidak mendukung tambahan profil pengguna
    - UserCreationForm kurang fleksibel sehingga perlu melakukan kustomisasi
    - Fitur yang diberikan tidak begitu banyak, jika ingin menambahkan fitur seperti otentikasi dua faktor maka perlu menambahkan sendiri atau memasang dari pihak ketiga


2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
    - Auntentikasi adalah proses yang melakukan verifikasi siapakah kita saat melakukan login di sebuah aplikasi serta membantu menentukan apakah pengguna adalah orang yang dia klaim.
    - Otorisasi adalah yang memverifikasi bahwa apakah seseorang tersebut memiliki akses untuk melakukan aktifitas di suatu sistem aplikasi.

    Kedua hal tersebut penting karena dapat melindungi privasi kita seperti data-data penting dalam sebuah aplikasi. Selain itu, keduanya merupakan bentuk pencegahan adanya penyusupan pada data pribadi dengan mengatur kelola akses dan verifikasi identitas serta mencegah dari kerusakan atau pelanggaran yang terjadi jika pengguna yang tidak berhak memiliki akses yang tidak pantas.


3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
    Cookies dalam konteks aplikasi web merupakan informasi yang dikirimkan oleh web server ke browser yang kemudian dikirim kembali oleh peramban pada halaman request yang akan datang.
    Django menggunakan cookies untuk mengelola data sesi pengguna dengan cara berikut:

        1. Konfigurasi: Anda mengatur konfigurasi sesi di `settings.py`, termasuk nama cookie sesi dan pengaturan lainnya.

        2. Menggunakan `request.session`: Anda menggunakan objek `request.session` untuk menyimpan dan mengambil data sesi pengguna.

        3. Middleware: Middleware Django mengelola cookie sesi secara otomatis.

        4. Penanganan Cookie: Django mengirim dan menyimpan cookie sesi di sisi klien.

        5. Penyimpanan Data Sesi: Data sesi sebenarnya disimpan di server, bukan di cookie, dan dapat disesuaikan dengan basis data atau penyimpanan lainnya.


4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
    Penggunaan cookies dalam pengembangan web memiliki risiko potensial termasuk pencurian data, penyadapan, XSS, CSRF, dan privasi pengguna. Untuk menjaga keamanan, enkripsi HTTPS penting untuk enkripsi, serta perlindungan terhadap serangan XSS, CSRF, dan pengaturan cookie yang aman. Informasikan pengguna dan berikan kontrol atas cookie. Cookies bisa aman jika dikelola dengan benar.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    **1. Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar**
        **REGISTRASI**
    1. Pada views.py di subdirektori main, membuat fungsi register yang menerima request. 
    2. Menambahkan import redirect, UserCreationForm, dan message pada file yang sama. UserCreationForm ini adalah impor untuk melakukan register bagi pengguna baru.
    3. Membuat berkas register.html pada folder template di dalam subdirektori main dengan isi sebagai berikut:
        {% extends 'base.html' %}

        {% block meta %}
            <title>Register</title>
        {% endblock meta %}

        {% block content %}  

        <div class = "login">
    
            <h1>Register</h1>  

                <form method="POST" >  
                    {% csrf_token %}  
                    <table>  
                        {{ form.as_table }}  
                        <tr>  
                        <td></td>
                        <td><input type="submit" name="submit" value="Daftar"/></td>  
                        </tr>  
                    </table>  
                </form>

            {% if messages %}  
                <ul>   
                    {% for message in messages %}  
                        <li>{{ message }}</li>  
                    {% endfor %}  
                </ul>   
            {% endif %}

        </div>  

        {% endblock content %}

    4. Menambahkan import fungsi register dalam urls.py pada main dan menambahkan path url ke dalam urlpatterns.

        **LOGIN DAN LOGOUT**
    1. Menambahkan import authenticate, login, logout
    2. Membuat fungsi login_user dan logout_user yang menerima parameter request. Untuk fungsi login terdapat variabel sebagai input nama, username, password pengguna baru, untuk fungsi logout, ia akan merequest logout dan redirect ke halaman login.
    3. Membuat berkas login.html pada folder yang sama dengan main.html sesuai template.
    4. Pada main.html, menambahkan beberapa potongan kode untuk button logout setelah button add new product.
    5. Membuka urls.py pada main dan melakukan import fungsi login_user, logout_user yang kemudian mengisi path pada urlpatternsnya.
        
    **2. Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal**
    1. Menambahkan requirement login terlebih dahulu agar user selalu diminta login terlebih dahulu, penambahan pada views.py di atas fungsi show_main.
    2. Mencoba menjalankan server dan membuka link localhost
    3. Membuat 2 buah akun yang berbeda dan menambahkan masing-masing 3 item product pada aplikasi.
    
    **3. Menghubungkan model Item dengan User**
    1. Pada models.py di main, menambahkan import user
    2. pada kelas item, menambahkan  user = models.ForeignKey(User, on_delete=models.CASCADE)
    3. Membuat fungsi baru bernama create_product di berkas views.py di main:
        def create_product(request):
            form = ProductForm(request.POST or None)

            if form.is_valid() and request.method == "POST":
                item = form.save(commit=False)
                item.user = request.user
                item.save()
                return HttpResponseRedirect(reverse('main:show_main'))

    4. Mengubah value pada key 'name' di context fungsi show_main menjadi request.user.username agar namanya bisa menyesuaikan dengan nama user ketika dilakukan login.
    5. Melakukan makemigration

    **4. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi**
    1. Menambahkan import datetime pada views.py di main
    2. Melangkapi fungsi login_user di bagian is user is not None dengan kode berikut:
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    3. Pada context di show_main, menambahkan 'last_login': request.COOKIES['last_login'],
    4. Pada main.html menambahkan kode ini setelah penampilan produk yang ada dan sebelum button add new product dan button logout :
    <h5>Your last login: {{ last_login }}</h5>
    5. Melakukan run server dan membukan link local host, kemudian login dengan salah satu akun. Untuk melihat cookies, melakukan cara yang sama seperti tutorial 3 dengan fitur inspect element di bagian Application/Storage. Akan terlihat last_login, sessionid, dan csrftoken. Jika melakukan logout, sessionid dan last_login akan hilang.

    **Bonus**
    1. Menambahkan beberapa kode untuk fitur tambah, kurang, dan delete product seperti berikut :

            <tr>
                <td>{{product.name}}</td>
                <td>{{product.price}}</td>
                <td>{{product.description}}</td>
                <td>
                <a href="{% url 'main:decrease' product.id %}">
                    <button>-</button>
                </a>
                {{product.amount}}
                <a href="{% url 'main:increase' product.id %}">
                    <button>+</button>
                </a>
                </td>
                <td>{{product.date_added}}</td>
                <td>
                    <a href="{% url 'main:delete' product.id %}">
                        <button>delete</button>
                    </a>
                </td>
            </tr>

    2. Menambahkan fungsi increase, decrease, dan delete pada views.py
    3. Menambahkan import fungsi increase, decrease, dan delete pada urls.py di main dan menambahkan path pada urlspatternnya.


========================================================================================================================================================================================================================================================================
Nama    : Nur Azizah Febriyana
NPM     : 2206824363
Kelas   : PBP-B

**TUGAS-5**

1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
**Selector Elemen (Element Selector)**:
-Manfaat: Memilih elemen berdasarkan nama elemennya. Misalnya, p akan memilih semua elemen paragraf.
-Kapan Menggunakan: Cocok untuk memilih semua instansi dari suatu elemen tertentu pada halaman.

**Selector Kelas (Class Selector)**:
-Manfaat: Memilih elemen berdasarkan nama kelas yang diberikan. Misalnya, .container akan memilih semua elemen dengan kelas "container".
-Kapan Menggunakan: Ideal untuk mengaplikasikan gaya yang sama pada beberapa elemen dengan kelas yang sama.

**Selector ID (ID Selector)**:
-Manfaat: Memilih elemen berdasarkan ID yang diberikan. Misalnya, #header akan memilih elemen dengan ID "header".
-Kapan Menggunakan: Terbaik untuk mengaplikasikan gaya khusus pada satu elemen tertentu, karena ID harus unik dalam satu halaman.

**Selector Atribut (Attribute Selector)**:
-Manfaat: Memilih elemen berdasarkan nilai atribut tertentu. Misalnya, [type="text"] akan memilih semua elemen dengan atribut type yang memiliki nilai "text".
-Kapan Menggunakan: Berguna ketika ingin memilih elemen berdasarkan atribut tertentu.

**Selector Anak Langsung (Child Selector)**:
-Manfaat: Memilih elemen anak langsung dari elemen tertentu. Misalnya, ul > li akan memilih elemen li yang langsung berada di dalam elemen ul.
-Kapan Menggunakan: Berguna ketika hanya ingin memilih elemen yang langsung berada di bawah elemen lain.

**Selector Pseudo-class dan Pseudo-element**:
-Manfaat: Pseudo-class (seperti :hover, :active) digunakan untuk memilih elemen dalam keadaan tertentu, sedangkan pseudo-element (seperti ::before, ::after) memungkinkan penambahan konten tertentu sebelum atau setelah elemen.
-Kapan Menggunakan: Pseudo-class digunakan untuk menanggapi interaksi pengguna, sementara pseudo-element digunakan untuk menambahkan gaya tambahan ke elemen.


2. Jelaskan HTML5 Tag yang kamu ketahui.
HTML5 atau Hypertext Markup Language versi 5 merupakan spesifikasi terbaru dari HTML, yang merupakan bahasa markup inti untuk membuat atau merancang sebuah kontek-konten pada web dengan tujuan berikut:
    - Mendorong markah semantik (bermakna)
    - Memisahkan desain dari konten
    - Mempromosikan aksesibilitas dan daya tanggap desain
    - Mengurangi tumpang tindih antara HTML, CSS, dan JavaScript
    - Mendukung pengalaman media yang kaya sekaligus menghilangkan kebutuhan akan plugin seperti Flash atau Java
    - Elemen semantik baru seperti <nav>, <header>, <footer>,<artikel>, <bagian>
    - Atribut baru dari elemen formulir seperti datalist, keygen, output
    - Jenis masukan baru: tanggal waktu, nomor, email, bulan, url, warna, dll.
    - Atribut input baru: wajib diisi, placeholder, fokus otomatis
    - Elemen grafis baru: <svg> dan <canvas>
    - Elemen multimedia baru: <audio> dan <video>

3. Jelaskan perbedaan antara margin dan padding.
Margin dan padding merupakan dua konsep pada desain CSS yang mengatur tata letak elemen HTML.
    **Margin**
    Merupakan ruang di sekitar elemen yang berarti margin ini memiliki fungsi untuk mengatur atau memberi jarak antara elemen satu dengan elemen-elemen di sekitarnya. Margin mempengaruhi elemen dari luar batas elemen tersebut. Jadi, perubahan dalam margin akan mempengaruhi seberapa jauh elemen tersebut dari elemen-elemen tetangganya.
    **Padding**
    Mengacu pada ruang antar elemen yang berarti padding memiliki fungsi mengatur atau memberikan jarak antara konten elemen dengan batasnya. Padding mempengaruhi elemen dari dalam batas elemen tersebut. Jadi, perubahan dalam padding akan mempengaruhi seberapa jauh konten dari batas elemen.

4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
**Desain**
-CSS Tailwind : Membangun interface yang menggabungkan class utilitas yang lebih kecil sehingga kebebasan kreatif lebih besar dan memungkinkan penggunaan class yang spesifik.
-Bootstrap : Menyediakan komponen-komponen gaya bawaan yang sudah didesain dengan baik sehingga mampu mempercepat proses desain komponen dengan baik.

**Fleksibilitas**
-CSS Tailwind : Lebih fleksibel karena memungkinkan pengguna membangun desain secara kustom sesuai dengan keinginan dan kebutuhan sehingga pengguna memiliki kendali yang penuh atas gaya desainnya.
-Bootstrap : Terdapat keterbatasan karena desain yang diberikan sudah bawaaan dari bootsrap itu sendiri yang lebih mementingkan kemudahan dalam desain.

**Ukuran file**
-CSS Tailwind : Ukuran file yang lebih ringan, tetapi bisa bergantung pada desain pengguna.
-Bootstrap : Ukuran file memungkinkan lebih besar karena adanya desain bawaan.

**Ekosistem pengembangan**
-CSS Tailwind : didukung oleh dokumentasi yang baik dan komunitas yang aktif. Berbagai sumber daya, plugin, dan integrasi dengan kerangka kerja JavaScript seperti React atau Vue dapat ditemukan, memberikan fleksibilitas tambahan kepada pengembang.
-Bootstrap : memiliki ekosistem yang sangat kuat, didukung oleh dokumentasi yang komprehensif, beragam tema dan template yang tersedia, serta dukungan komunitas yang luas. Ini memudahkan pengembang untuk memulai proyek dengan cepat dan mengakses sumber daya yang diperlukan.

**Kapan menggunakan CSS Tailwind dan Bootstrap?**
- CSS Tailwind : Karena tailwind didesain untuk lebih fleksibel, maka penggunaan framework ini sangat cocok untuk pengembang yang ingin lebih spesifik dan tampilan yang lebih unik mengenai desain yang diinginkan dan dibutuhkan sehingga menghindari penggunaan gaya default. Framework ini didesain khusus untuk pengembang yang ingin menciptakan tampilan yang khusus untuk suatu proyek yang ingin dibangun.
-Bootstrap : Karena bootstrap didesain dengan komponen dengan gaya bawaan, sehingga ini lebih baik digunakan saat pengembang ingin menggunakan komponen yang siap pakai dengan konsistensi visual yang tinggi serta desain yang terbukti dan waktu desain yang lebih cepat.
 
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    1. Kustomisasi desain pada templat HTML yang telah dibuat pada Tugas 4 dengan menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut
    -Menambahkan beberapa kode pada base.html tepatnya di dalaam block meta :
    <meta name="viewport" content="width=device-width, initial-scale=1">
    -Menambahkan bootstrap CSS dan jS

    2. Kustomisasi halaman login, register, dan tambah inventori semenarik mungkin.
    -Untuk tahap ini saya mendapatkan inspirasi template dari https://bbbootstrap.com/snippets/bootstrap-glowing-login-form-61831104
    -Mengedit beberapa elemen agar sesuai dengan format-format elemen yang sudah ada
    -untuk fungsi tambah inventori, saya sedikit menambahkan pada file forms.py,views.py, dan models.py yang berguna saat melakukan pengeditan/kustomisasi halaman daftar inventori.
    -contoh pada models.py:
    class Item(models.Model):
        name = models.CharField(max_length=255, default = '')
        price = models.CharField(max_length=255, default = '')
        description = models.TextField()
        amount = models.IntegerField(default=0)
        date_added = models.DateField(auto_now = True, null= True)
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        photo = models.CharField(max_length=255, default = '') -->tambahannya
    -pada views.py menambahkan request.POST.get('photo') pada fungsi edit_product dan create_product.
    
    3. Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan apporach lain seperti menggunakan Card.
    -Pada tahap ini saya menambahkan template dari bootstrap sebagai header dari halaman daftar inventori:
    <nav class="navbar bg-body-tertiary">
    <div class="container-fluid">
        <a class="navbar-brand" href="#">
            <img src="https://yt3.googleusercontent.com/rD5w3FIsk4BSctADzRYlOBPsdipd9eurjyditDWnXZ8Nj9o7gOxB4649LkYik7HNTomJ9Vtl=s900-c-k-c0x00ffffff-no-rj" alt="Logo" width="30" height="24" class="d-inline-block align-text-top">
            Kwangya Store
        </a>
        <h5>Your last login: {{ last_login }}</h5>
        <a href="{% url 'main:create_product' %}">
            <button class="action-button-create">
                Add New Product
            </button>
        </a>
        <a href="{% url 'main:logout' %}">
            <button class="action-button-logout">
                Logout
            </button>
        </a>
    </div>
    </nav>
    -Mengatur warna background sesuai dengan keinginan
    -Membentuk template untuk tata letak foto, nama, harga, amount, date added pada produk tersebut dalam bentuk bubble-bubble:
    <style>
    .product-bubble {
        display: flex;
        align-items: center;
        border: 1px solid #9124cf;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
        background-color: #eac1ef;
    }

    .product-image {
        width: 100px;
        height: 100px;
        object-fit: cover;
        border-radius: 50%;
        margin-right: 10px;
    }

    .product-details {
        flex-grow: 1;
    }

    .product-name {
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 5px;
    }

    .product-description {
        margin-bottom: 5px;
    }

    .product-price,
    .product-amount,
    .product-date {
        margin-bottom: 5px;
    }

    .product-actions {
        display: flex;
        align-items: center;
    }

    .action-button {
        background-color: #ba63dc;
        color: #fff;
        padding: 5px 15px;
        border: none;
        border-radius: 5px;
        margin-right: 5px;
    }

    .action-button-delete {
        background-color: #ba0d72;
        color: #fff;
        padding: 5px 15px;
        border: none;
        border-radius: 5px;
        margin-right: 5px;
    }

    .action-button-logout {
        background-color: #ac36db;
        color: #fff;
        padding: 5px 15px;
        border: none;
        border-radius: 5px;
        margin-right: 5px;
    }

    </style>
**Bonus**
    -menambahkan kode kelas berikut pada main.html:
    .product-bubble.last-product {
    background-color: #ed48ff; /* untuk last product */
    }

    -menambahkan if untuk last-product:
    <div class="product-bubble {% if forloop.last %}last-product{% endif %}">
            <img src="{{ product.photo }}" class="product-image">
            <div class="product-details">
                <h4 class="product-name">{{ product.name }}</h4>
                <p class="product-description">{{ product.description }}</p>
                <p class="product-price">Price: {{ product.price }}</p>
                <p class="product-amount">Amount: {{ product.amount }}</p>
                <p class="product-date">Date added: {{ product.date_added }}</p>
            </div>
            <div class="product-actions">
                <a href="{% url 'main:decrease' product.id %}">
                    <button class="action-button">-</button>
                </a>
                <a href="{% url 'main:increase' product.id %}">
                    <button class="action-button">+</button>
                </a>
                <a href="{% url 'main:edit_product' product.pk %}">
                    <button class="action-button">Edit</button>
                </a>
                <a href="{% url 'main:delete' product.id %}">
                    <button class="action-button-delete">Delete</button>
                </a>
            </div>
        </div>

    4. Menjawab beberapa pertanyaan berikut pada README.md pada root folder 
    5. Melakukan git add, commit, dan push


========================================================================================================================================================================================================================================================================
Nama    : Nur Azizah Febriyana
NPM     : 2206824363
Kelas   : PBP-B

**TUGAS-6**

**Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.**
    *asynchronous programming*
    1. Tugas-tugas dieksekusi tanpa menunggu tugas sebelumnya selesai.
    2. Tugas yang membutuhkan waktu lama tidak memblokir eksekusi program.
    3. Menggunakan callback atau await/async untuk menangani hasil tugas yang mungkin belum selesai.
    4. Kesalahan dapat ditangani lebih efektif dengan menggunakan mekanisme seperti try-catch pada blok await/async atau menggunakan callback untuk menangani kesalahan.

    *synchronous programming*
    1. Tugas-tugas dilakukan satu per satu dengan menunggu tugas sebelumnya selesai terlebih dahulu.
    2. Tugas dapat menjadi "blocking," yang berarti eksekusi program terhenti atau diblokir sampai tugas tersebut selesai. 
    3. Biasanya menggunakan pemanggilan fungsi atau metode secara langsung.
    4. Kesalahan dapat menyebabkan program berhenti atau crash.

**Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.**
    *Paradigma event-driven programming* adalah pendekatan pemrograman di mana eksekusi program dipicu oleh kejadian (events) atau tindakan yang terjadi pada suatu waktu tertentu. Sebagai alternatif dari eksekusi program yang berurutan (synchronous), pada paradigma ini, program merespon peristiwa yang terjadi secara asynchronous. Maksud dari paradigma event-driven programming:

    1. Program tidak berjalan dari atas ke bawah secara berurutan, tetapi merespon kejadian atau tindakan tertentu.
    2. Peristiwa dapat mencakup interaksi pengguna (seperti klik tombol), koneksi jaringan, atau pemrosesan data yang telah selesai (seperti AJAX requests).
    3. Dalam lingkungan web, event-driven programming seringkali digunakan untuk meningkatkan responsivitas halaman web dengan mengizinkan tugas tertentu untuk berjalan di latar belakang.

**Jelaskan penerapan asynchronous programming pada AJAX.**
    Asynchronous JavaScript and XML (AJAX) adalah teknik yang memungkinkan halaman web untuk mengirim dan menerima data dari server secara asinkron tanpa harus me-refresh seluruh halaman. Penerapan AJAX umumnya melibatkan asynchronous programming untuk memastikan bahwa permintaan ke server dan tanggapan dari server dapat ditangani tanpa menghentikan eksekusi program utama. 
    Berikut adalah cara kerja AJAX:
    1. Browser akan memanggil AJAX javascript untuk mengaktifkan XMLHttpRequest dan mengirimkan HTTP Request ke server. 
    2. XMLHttpRequest dibuat untuk proses pertukaran data di server secara asinkron.
    3. Server menerima, memproses, dan mengirimkan data kembali ke browser.  
    4. Browser menerima data tersebut dan langsung ditampilkan di halaman website, tanpa perlu reload atau membuat halaman baru.

**Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.**
    
    *Kemudahan Penggunaan*
    Jika Anda sudah terbiasa dengan jQuery, maka menggunakan jQuery akan lebih mudah karena ia menyediakan metode yang mudah dipahami dan digunakan untuk mengambil data dari server. Namun, Fetch API juga cukup mudah digunakan dengan sintaks yang sederhana.

    *Performa*
    Fetch API cenderung memiliki performa yang lebih baik daripada jQuery. Fetch API menggunakan metode modern seperti Promise dan async/await, yang memungkinkan untuk mengambil data dengan cara yang lebih efisien dan tanpa harus mengunduh semua file jQuery yang besar.

    *Ukuran*
    Fetch API memiliki ukuran yang lebih kecil daripada jQuery. jQuery adalah sebuah library yang cukup besar, sementara Fetch API hanya berfokus pada fitur pengambilan data dari server. Jadi, jika Anda ingin mengurangi ukuran halaman web Anda, menggunakan Fetch API mungkin lebih baik.

    *Kemampuan dan Kompatibilitas*
    jQuery memiliki banyak fitur dan plugin yang dapat digunakan untuk membuat tampilan yang menarik dan interaktif. Namun, Fetch API adalah standar web modern dan didukung oleh semua browser terkini. Jadi, jika Anda ingin membuat aplikasi yang lebih canggih dan menggunakan fitur terbaru, Fetch API akan menjadi pilihan yang lebih baik.

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
    1. Mengubah tugas 5 yang telah dibuat sebelumnya menjadi menggunakan AJAX.
        a. Atur alur program untuk AJAX GET:
            1. Buat fungsi di `views.py` untuk menampilkan data produk pada HTML menggunakan fetch, serta tambahkan kemampuan untuk menambahkan produk baru ke basis data melalui AJAX.
            2. Tambahkan path yang mengarahkan ke fungsi views yang sudah dibuat sebelumnya.
            3. Tambahkan ID dan script yang diperlukan di dalam file `main.html`.
            4. Buat modal sebagai form di dalam file `main.html`.


        b. Atur alur program untuk AJAX POST:
            1. Buat fungsi baru di dalam script di file `main.html`.
            2. Tambahkan fungsi `onclick` untuk menambahkan item collections.

        
    2. Melakukan perintah collectstatic
        Perintah collecstatic dilakukan menyesuaikan tutorial 2 pada bagian Menambahkan Konfigurasi Deployment ke PaaS PBP Fasilkom UI

    3. Menjawab pertanyaan di dalam file README.md

    4. Melakukan git workflow (add, commit, push)

    5. Melakukan deployment ke PaaS PBP Fasilkom UI
        - Mengunduh environ 
        - Membuat beberapa file dan folder terkait deployment (Procfile, .dockerignore, Dockerfile, folder .github dan workflows, pbp-deploy.yml)
        - Mengedit settings.py dengan menambahkan beberapa kode baru terkait deployment
        - Set repository secret pada Secrets and variables di settings repository github dengan memasukkan DOKKU_SERVER_IP, DOKKU_APP_NAME, dan DOKKU_SSH_PRIVATE_KEY
        akses deployment : https://nur-azizah25-tutorial.pbp.cs.ui.ac.id