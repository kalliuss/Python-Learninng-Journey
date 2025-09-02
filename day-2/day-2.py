
# ?  4. Daha fazla kontrol akışı araçları (Döngüler - If / Else Muhabbetleri)

x = 5 
# int(input("Lütfen bir sayı giriniz: ")) # ! VERİ GİRİŞİNİ BÖYLE ALIYORSUN UNUTMA ! ! !

if x < 0:
    x = 0
    print("Negatif sayı girdin")
elif x == 0:
    print("Sıfır girdin")
elif x > 0:
    print("Pozitif sayı girdin")
else:
    print("Farklı bişey")

    # elif = else if kısaltımı
    # else if mentalitesi switch case yerine geçer

# ? for döngüsü

# pascaldaki gibi sayıların aritmetik ilerlemesi üzerine yineleme yapmak

words = ["bir", "iki", "üç", "dört", "beş"]
for w in words:   # word indexleri w ye atandı
    print(w, len(w))  # len(w) gelen değerin uzunluğunu döndürecektir.


# kolekysiyon üzerinde for döngüsü

users = {"Cem": "aktif", "kaan": "aktif", "zürafa": "pasif"}

# print(users["kaan"]) AKTİF ÇIKTISI VERİR

# bir kopya;

for user, status in users.copy().items():
    if status == "pasif": 
        del users[user]  # pasif olanları siler

# yeni  bir koleksiyon açalım
active_users = {}
for user, status in users.items():
    if status == "aktif":
        active_users[user] = status  # aktif olanları yeni koleksiyona ekler


print(active_users)  # {'Cem': 'aktif', 'kaan': 'aktif'}

# ! range() fonksiyonu

# * bir sayı dizisi üzerinde yineleme yapmanız gerekiyorsa, yerleşik range() fonks kullanışlı olur.

for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

# * verilen bitiş noktası oluşturulan dizini parçası değildir.
# yani range(10) 10 değer üretir, 10 uzunluğundaki bir dizinin ögeleri için yasal indisler
# aralığın başka bir sayıdan başlmasına izin vermek veya farklı bir artış (negatif bile olsa; bazen buna adım denir) belirtmek mümkündür:

list(range(5, 10))  # [5, 6, 7, 8, 9]

list(range(0, 10, 3))  # [0, 3, 6, 9] -> 3'er artar

list(range(-10, -100, -30))  # [-10, -40, -70]

#* bir dizinin indeksleri üzerinde yineleme yapmak için range() ve len() ögelerini aşağıdaki gibi birleştirebiliriz:

a = ["kaan", "oğuzhan", "nilay", "haşim"]

for i in range(len(a)): 
    print(i, a[i]);   

# len(a) tüm dizi uzunluğunu range üzerinden i'ye aktardı
# range 0,1,2,3,4 diye dizilim üretti
# i sırasıyla bu değerleri aldı

print(range(10))  # range(0, 10) çıktısını verir

# sum fonksiyonu
# belirtilen değer aralığındaki sayıların toplamını döndürür
print(sum(range(4)))  # 0 + 1 + 2 + 3 = 6

print(sum(range(5, 10)))  # 5 + 6 + 7 + 8 + 9 = 35

print(sum(range(0, 10, 2)))  # 0 + 2 + 4 + 6 + 8 = 20

# sum(10) hata verir aralık yok 


# ? break and continue Statements

# asal sayı kontrol örneği (break)

for n in range(2, 10):  # 2'den 9' kadar sayıları tek tek al
    for x in range(2, n): # 2'den n-1'e kadara bölen adaylarını dene  sağdaki dahil olmadığı için her zaman bir düşüğünü ve bir eksiğini alacak ondan n-1 diye değil direkt n diye yazdık.
        if n % x == 0: # n, x' e tam bölünüyorsa
            print(f"{n} equals {x} * {n // x}")
            break  # döngüyü kır /  devam etme.


        #Örnek: n = 4 olduğunda

        # İç döngü x = 2 ile başlar.

        # 4 % 2 == 0 → yani 4 sayısı 2’ye tam bölünüyor.

        # Çıktı: 4 equals 2 * 2

        # break → artık başka bölen aramaya gerek yok → iç döngüden çıkılır.


# Kodu anlamak adına kendim deniyorum

for c in range(5,15):
    for b in range(5, c): 
        if c % b == 0:
            print(f"{c} equals {b} * {c // b}")
            break  # iç döngüden çık


# ? continue 

for num in range(2, 10):
    if num % 2 == 0:
        print(f"{num} çift sayıdır.")
        continue  # atla başa dön
    print(f"{num} tek sayıdır.")  # bu satır sadece tek sayılar için çalışır


# ? else Clauses on Loops

# # Bir for veya while döngüsünde, break ifadesi bir else klozu ile eşleştirilebilir.
# Eğer döngü break çalıştırılmadan tamamlanırsa, else klozu çalıştırılır.
# Bir for döngüsünde, else klozu, döngü son iterasyonunu bitirdiğinde (ve hiç break olmadığında) çalıştırılır.

# Bir while döngüsünde, koşul False olduğunda çalıştırılır.

# Her iki tür döngüde de, eğer döngü bir break ile sonlandırılırsa, else klozu çalıştırılmaz.
# Tabii ki, döngüyü erken sonlandıran diğer yollar (örneğin return veya bir hata fırlatılması) da else klozunun çalışmasını engeller.


# ## 🔹 Döngü + `else` Mantığı (Basit Anlatım)

# Bir markete gittiğini düşün:

# * **Amaç:** Marketin içinde şeker arıyorsun.
# * **Döngü:** Her rafta tek tek bakıyorsun (`for` döngüsü).
# * **Koşul:** Eğer rafta şeker bulursan (`if` koşulu sağlanır) → hemen alıp çıkıyorsun (`break`).
# * **Sonuç:** Eğer marketten çıkarken hiç `break` olmadıysa (yani hiç şeker bulamadıysan), kapıda güvenlik sana “Şeker yokmuş” diyor (`else`).

# ---

# ## 🔹 Python’da Çalışma Şekli

 #```python
for raf in range(1, 6):   # 1'den 5. rafa kadar bak
     if raf == 3:          # 3. rafta şeker var diyelim
         print("Şeker bulundu! Raf:", raf)
         break             # hemen alışverişi bitir
else:
     print("Şeker bulunamadı")
#```

#! ### Çıktı:

# ```
# Şeker bulundu! Raf: 3
# ```

# (`break` olduğu için `else` çalışmaz.)

# ---

# Eğer şeker hiçbir rafta olmasaydı:

# ```
# Şeker bulunamadı
# ```

# → çünkü döngü normal şekilde bitti, `break` olmadı.

# ---

# ## 🔹 Özet

# * **`break` olursa** → `else` çalışmaz.
# * **`break` olmazsa** → döngü bittiğinde `else` çalışır.

# ---


#? 4.6 pass ifadeleri

# pass deyimi hiçbir şey yapmaz. Bir kod bloğunun içini boş bırakmak istediğimde de kullanırız.add()

# while True:
#     pass  # çıkmak için CTRL+C at, bekler yoksa.

#* genellikle minimal sınıflar oluştururken kullanılır

class MyEmptyClass:
    pass

#* passin kullanılabileceği bir başka yerde;
# yeni kod üzerinde çalışırken bir fonks. veya koşul gövdesi için bir yer tutucu olarak daha soyut
# bir düzeyde düşünmeye devam etmemizi sağlamaktadır. pass sessizce göz ardı edilir.


# ? match ifadeleri

#* match bir ifadeyi alır ve değerini bir veya daha fazla case bloğu olarak verilen ardışık kalıplarla karşılaştırır.
# diğer dillerdeki switch ifadesine yüzeeysel olarak benzer. 
# yalnızca eşleşen ilk kalıp yürütülür ve ayrıca bileşenleri (sıra öğeleri veya nesne nitelikleri)
# değerden değişkenlere çıkarabilir.

# en basit form, bir konu değerini bir veya daha fazla sabitle karşılaştırır:


def http_error(status): #bir fonks
    match status:
        case 400:
            
            return "Bad request"
        # veya kullanarak birkaç sabiti tek kalıpta birleştirdik.
        case 401 | 402 |403:
            return "Not authorized"
        case 418:
            return "I'm a teapot"
        case _:
            
            return "Unknown error"
            
        # wildcard görevi görür ve asla eşleşmez. Hiç bir durum eşleşmezse dallardan hiçbiri yürütülmez.

print(http_error(400))  # Bad request
print(http_error(405))  # Unknown error

# kalıplar paket açma atamalrı gibi görünebilir ve değişkenleri bağlamak için kullanılabilir

# kordinat örneği

# ! tuple = demet , pythonda veri yapısıdır, bir den fazla değeri tek değişkende saklar.
# sıralıdır
# değiştirilemez(immutable)
#elemanları farklı türde olabilir.

#koordinat = (3, 5)     # iki elemanlı tuple
# renk = ("kırmızı", "yeşil", "mavi")  # string tuple
# karisik = (1, "Kaan", True, 3.14)    # farklı türde elemanlar

# point bir (x,y) den oluşan tuple
def kordinat(point):
    match point:
        case (0, 0):
            return "Orijin" 
        case (0, y):
            return f"Y ekseni: {y}"
        case (x, 0):
            return f"X ekseni: {x}"
        case (x, y):
            return f"X={x}, Y={y}"
        case _:
            return  ValueError("Geçersiz nokta")

print(kordinat(()))


# Verilerinizi yapılandırmak için sınıfları kullanıyorsanız,
# sınıf adını ve ardından bir yapıcıya benzeyen,
# ancak nitelikleri değişkenlere yakalama yeteneğine sahip bir argüman listesi kullanabilirsiniz:


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point: 
        case Point(x = 0, y = 0):
            print("Orijin")
        case Point(x = 0, y = y):
            print(f"Y ekseni: {y}")
        case Point(x = x, y = 0):
            print(f"X ekseni: {x}")
        case Point(x = x, y = y):
            print(f"X={x}, Y={y}")
        case _:
            print("Geçersiz nokta")



#! match ve pass ifadelerine başka kaynaktan bakılacak.

#TODO Udemy kursundan kafamın açık olduğu gün devamını getireceğim. ! 


# ? 4.8 Fonksiyon Tanımlanması

# //* def fonksiyon tanımınıda kullanırız.
# fonks adı ve parantez içine alınmış resmi parametreler listesi takip eder.

# def fib(n):   gibi

def fib(n): 
    a,b = 0,1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b

         # b değerini daha sonra tanımlamak hata verecektir aynı anda tanımlamak önemlidir.
    print()


# şimdi fonksiyonu çağıralım

fib(2000)  # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597

# fibonacci serisindeki sayıları listeye aktaralım

def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b , a + b
    return result

f100 = fib2(100)

print(f100)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


# ? 4.9 İşlev Tanımlama hakkında daha fazla bilgi

# * 4.9.1 Varsayılan Değişken değerleri

# Değişken sayıda argüman içeren fonks tanımlamak da mümkündür. Birleştirilebilen üç form vardır:

# 4.9.1 Varsayılan Değişken Değerleri

# ! En kullanışlı biçim, bir veya daha fazla bağımsız değişken için varsayılan bir değer belirtmektir.
# Bu, izin vermek üzere tanımlandığından daha az sayıda bağımsız değişkenle çağrılı bir fonksiyn oluşturur.
# Örneğin;


#evet hayır cevaplarını kabul eden kod parçası:

def ask_ok(prompt, retries = 4, reminder = "Please try again !"):
    while True:
        reply = input(prompt)
        if reply in {"yes" "y", "ye"}:
            return True
        if reply in {"no", "n", "nop", "nope"}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError("invalid user response")
        print(reminder)


        #-in- anahtar sözcüğü bir diziin belirli bir değer içerip içermediğine bakar.

ask_ok("Do you really want to quit?")  # varsayılan değerleri kullanır


# varsayılan değerler tanımlayam kapsamdaki fonksiyon tanımlama noktasında değerlendirilir, böylece


i = 5

def f(arg = i):
    print(arg)

i = 6
f()

def k(arg = i):
    print(arg)

i = 7
k()  # 6 çıktısını verir

# TODO ÖNEMLİ UYARI DAN DEVAM EDİLECCEK

# varsayılan değer yalnızca bir kez değerlendirilir.
# varsayılan değer liste, sözlük veya çoğu sınıfın örnekleri gibi değiştirilebilir bir nesne
#olduğunda bu durum fark yaratır.

# örneğin, fonks sonraki çağrılarda kendisine aktarılan argümanları biriktirir:

def f(a, L =[]):
    L.append(a)
    return(L)

print(f(1))  # [1]
print(f(2))  # [1, 2]
print(f(3))  # [1, 2, 3]


#! varsayılan değerin sonraki çağrılar arasında paylaşılmasını istemiyorsanız, bunun yerine fonksiyonu şu şekilde yazabilirsiniz;

def k(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return(L)

print(k(1))  # [1]
print(k(2))  # [2]
print(k(3))  # [3]

# * 4.9.2 Anahtar Kelime Argümanları

# fonksiyonlar ayrıca kwarg-value şeklinde anahtar kelime argümanları kullanılarak da çağrılabilir.
# örnek, aşağıdaki fonksiyon:

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

# mantığını daha iyi kavramak adına kendimde üretiyorum;

def car(brand, color="siyah", fuel="dizel"):
    print("-- Araba markası", brand, end=' ')
    print("-- rengi:", color)
    print("-- yakıt türü:", fuel)
    print(brand, " markasından emin misiniz?")


car("BMW") # diğer parametreleri belirtmediğim için 2. ve 3. parametrelerde varsayılan değeri aldı
car("Audi", "beyaz") # 2. parametre belirttim ve 2. parametredeki varsayılan değer yerine beyaz ı aldı.
car("Mercedes", fuel="benzin") # 3. parametreyi anahtar kelime argümanı olarak belirttim, 2. parametre varsayılan değeri aldı.  


# *name **name mantığı

# *name sadece konumsal argümanları toplar. Yani fonksiyonda "abc", 123 gibi değerleri alır.
# **name keywords -> anahtar = değer (keyword) argümanlarını toplar. Yani key="value" şeklinde ismiyle verilmiş değerler buraya gelir.add()

def test(*cart, **curt):
    print("cart:", cart)
    print("curt:", curt)


test(10,20,30,40, "hello", name = "kaan", age = 23, date = "25 March")


# ? 4.9.6 Lambda İfadeleri

# Küçük anonim fonksiyonlar lambda anahtar sözcüğü ile oluşturulabilir.
# Bu fonksiyon iki argümanın toplamını döndürür

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
# fonksiyonu anonim kıldık

f(0)  # 42
f(1)  # 43