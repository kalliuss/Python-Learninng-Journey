print("Hello World");

# yorum satırı

8 / 5 # 1.6 bölmeler float verecektir

8 // 5 # // kullanırsak floor yapacaktır. Yani aşağı yuvarlar

5**2 # 5'in karesi 25

#bir değişkeni tanımlmadan kullanamıyoruz

# eğer bir tam sayıdan ondalıklı çıkartırsan sonuç oto ondalıklı döner;

quest = 4 * 3.75 - 1

print(quest) # 14.0

name = "kaan" 
name = 'kaan' # aynılar

# escape
print("Kaan\'ın kitabı") # Kaan'ın kitabı

# \ ile başlayan karakterler özzel olarak yorumlansın istemiyorsak; 
print('C:\some\name') # bu şekilde escape oluyor ancak;

print(r'C:\some\name') # bu şekilde escape olmuyor

#birden fazla satırı kullanmak :?

print("""\


      
Kullanıcı adı: kaan
Şifre: 12345
""")

# dizeler + ile birleşir (klasik) fakat * operatörü ile tekrarlar

print(3 * 'an' + 'am')

# yan yana 2 veya daha fazla dize sabiti yanni tırnak işaretleri arasına alınanlar otomatik birleşir

bumps = 'bum' 'p' 's'
print(bumps)

# bu özellik uzun dizeleri kırmak istediğinizde kullanışlıdır

text = ('Kullanıcı adı: kaan '
        'Şifre: 12345')
print(text)

# dizeler ilk karakter 0, sağdan saymaya başlamak için ideksler negatif sayılarda olabilir:

word = 'Python'
print(word[0])  # P
print(word[-1]) # n

# neden -1 den başlar: çünkü 0 ile -0 aynıdır. 

# dilimleme
print(word[0:2])  # Py | 2. indeks dahil olmaz
print(word[2:5])  #tho | 5. indeks dahil olmaz

# dilim indekslerin kullanışlı varsayılanları vardır;

# atlanmış bir ilk dizin varsayılanı 0'dır
word[:2]  # Py

# atlanmış bir ikinci dizin varsayılanı dilimlenmekte olan dizenin boyutudur
word[4:] #on
# =
word[-2:] #on

# s[:i] + s[i:] = s

print(word[:2] + word[2:])  # Python
print(word[:4] + word[4:])  # Python

# çok büyük dizin kullanmak yani sınırı aşmak hata sebebi olur
#print(word[100])  # IndexError: string index out of range

# ancak, aralık dışı dilim endeskleri, dilimleme için kullanıldığında zarif bir şekilde işlenir:
print(word[4:100])  # on
print(word[100:])  # boş dize


# PYTHON dizeleri değitiremez
# word[0] = '3' - hata

# farklı bir dize ihtiyacı varsa yenisini oluşturmalısınız

newWord = 'J' + word[1:]  # Jython
newWord2 = word[:1] + 'y' + word[2:]  # Python

print(newWord)  # Jython
print(newWord2)  # Python

# len(değişken) bir dizenin uzunluğunu döndürür

s = "merhabalar"

print(len(s))  # 10


# listeler
# farklı türde veriler içerebilir ancak genelde geneli aynıdır. 

squares = [1, 4, 9, 16, 25]
print(squares)  # [1, 4, 9, 16, 25]

# dizine alınabilir, dilimlenebilir

squares[0]  # 1
squares[-1]  # 25
squares[-3:]  # [9, 16, 25]

# dizeler değişemez ancak listeler değiştirilebilir

cubes = [1, 8, 27,65, 125] # bir hata mevcut 65?
4**3 # 64 ! 

cubes[3] = 64  # 4'ün küpü 64
print(cubes)  # [1, 8, 27, 64, 125]

# yöntemler hakkında daha sonra detaya giricez ancak list.append() ile en sona eleman ekleyebiliriz.add()

cubes.append(216)  # 6'nın küpü
cubes.append(7**3)  # 7'nin küpü
print(cubes)  # [1, 8, 27, 64, 125, 216, 343]

# basit atama asla verileri kopyalamz ancak,
# bir değişkene liste atandığında, deişken mevcut listeyi işaret 
# atanan değişken üzerinden işlem yaptığınızda listede etkienecektir.

rgb = ['red', 'green', 'blue']
rgba = rgb  # rgb'yi işaret ediyor
id(rgb) == id(rgba) # true aynı nesneyi işaret ediyorlar

rgba.append("Alph")
print(rgb) # ['red', 'green', 'blue', 'Alph'] dikkat! rgb'yi yazdırdık. 

# shallow copy

# listenin aynı özelliklerine ait farklıbir varyasyon oluşturuyor gibi düşünebiliriz 
# birbirinden bağımsız

# ['red', 'green', 'blue', 'Alph']
correct_rgba = rgba[:]
correct_rgba[-1] = "Alpha"

print(correct_rgba)  # ['red', 'green', 'blue', 'Alpha']
print(rgba)  # ['red', 'green', 'blue', 'Alph'] dikkat! farklı


# dilimlemelerde atamalarda mümkündür. 
# listenin boyutuu değiştirebilir veya tamamen temizleyebilir !

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)  # ['a', 'b', 'c', 'd', 'e']

# replace bazı değerler
letters [2:5] = ['C', 'D', 'E']
print(letters)  # ['a', 'b', 'C', 'D', 'E', 'f', 'g']

# şimdi bazı değerleri temizleyelim
letters[2:5] = []  # boş liste atandı  ! 2 DAHİL ANCAK 5 DEĞİL
print(letters)  # ['a', 'b', 'f', 'g']

# tamamını temizleyelim
letters[:] = []   # [:] ile tümünü seçtik kısaca
print(letters)  # []

# len() listeler içinde geçerlidir
print(len(letters))  # 0

# listeleri iç içe yerleştirme (diğer listeleri içeren listeler oluşturmak) mümkündür ;

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]

print(x)  # [['a', 'b', 'c'], [1, 2, 3]]
x[0]  # ['a', 'b', 'c']
x[0][1]  # 'b'  - ilk elemanın içerisindeki 1. index

# 3.2 Programlamaya doğru ilk adımlar

# fibonacci dizisi
# iki elemanın toplamı diğer sayıyı verecek

a, b = 0, 1 # çoklu atama
while a < 10: 
    print(a)
    a, b = b, a + b  # a'yı b'ye atar ve b'yi a + b yapar 
    # a = b
    # b = a + b

# pythonda 0 olmayan herhangi bir tam sayı doğrudur.
# sıfır yanlıştır
# uzunluğu sıfır olmayan her şey doğrudur, boş dize yanlıştır.

# end elemandan sonra gelecek yeni satırı önlemek veya çıktıyı farklı bir dizeyle bitirmek için kullanılabilr;

c, d = 0, 1
while c < 1000:
    print(c, end=', ')  # virgülle ayırarak yazdırır
    c, d = d, c+d;
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987,

# DİPNOTLAR

# ** , - den daha yüksek öncelikli old için;
# -3**2, -(3**2) olarak yorumlanacaktır. -9
# 9 elde etmek için (-3)**2 yazmalısınız.

