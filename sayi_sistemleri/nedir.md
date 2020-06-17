# Sayı sistemleri nedir ?

    Bilgisayar ve bilgisayar programlama dillerinde dört farklı sayı sistemi kullanılmaktadır:

    - İkili (Binary) Sayı Sistemi

    - Sekizli (Octal) Sayı Sistemi

    - Onlu (Decimal) Sayı Sistemi

    - Onaltılı (Hexadecimal) Sayı Sistemi


    Sayı sistemlerini ifade eden değerler, sözkonusu sayı sisteminde kullanılan rakam sayısını göstermektedir.
    Örneğin sekizli sayı sistemi, bu sistemde 8 adet rakam kullanıldığını ifade etmektedir.


    İkili (Binary) Sayı Sistemi          :  0  1

    Sekizli (Octal) Sayı Sistemi         :  0  1  2  3  4  5  6  7

    Onlu (Decimal) Sayı Sistemi          :  0  1  2  3  4  5  6  7  8  9

    Onaltılı (Hexadecimal) Sayı Sistemi  :  0  1  2  3  4  5  6  7  8  9  A  B  C  D  E  F

    Onlu sayı sistemi nedir ?

        0'dan 9'a kadar rakamlar kullanılır
        Kullanılan rakamlardan da anlayabileceğiniz gibi günlük hayatta en çok kullandığımız sayı sistemi onluk(decimal) sistemdir.

        Her basmakta yer alan rakam 10 sayısının katları ile çarpılır(İlkokulda gösterilen basamak sistemi)

        Örneğin: 4173 sayısını basamak basamak gösterelim:

        Birler basamağı(birinci basamak): 3 * 10^0 | 3 * 1 = 3
        Onlar basamağı(ikinci basamak): 7 * 10^1 | 7 * 10 = 70
        Yüzler basamağı(üçüncü basamak): 1 * 10^2 | 1 * 100 = 100
        Binler basamağı(dördüncü basamak): 4 * 10^3 | 4 * 1000 = 4000

        (Tüm basamakların toplamı) 4000 + 100 + 70 + 3 = 4173

    Onaltılı sayı sistemi nedir ?

        0'dan 9'a kadar rakam ile 10'dan 15'e harf ile gösterimi yapılan sayı sistemidir.

        A = 10, B = 11, C = 12, D = 13, E = 14, F = 15

        Örneğin: 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 1A, 1B, 1C, 1D, 1E, 1F, 20....

                 Sekizli sistemde 173 sayısının onlu sistemde değerini bulalım:

                 3 : 3 * 8^0 | 3 * 1 = 3
                 7 : 7 * 8^1 | 7 * 8 = 56
                 1 : 1 * 8^2 | 1 * 64 = 64

                 (Tüm basamakların toplamı) 64 + 56 + 3 = 123

    İkili sayı sistemi nedir ?

        Bilgisayarlar elektronik devrelerden oluştukları için ikili sayı sistemini kullanırlar.
        Bütün işlemler 0 ve 1 rakamları ile gerçekleşir.


        *Bir ikili sistem sayısında her rakama "bit" denir.
        *8 bitten oluşan sayılara ise "byte" denir.

        Bilgisayarlar depolama birimleri olarak şöyle sıralayabiliriz:

        1 Byte = 8 Bit
        1 Kilobyte = 2^10 | 1024 Byte
        1 Megabyte = 2^10 | 1024 Kilobyte
        1 Kilobyte = 2^10 | 1024 Megabyte
        1 Terabyte = 2^10 | 1024 Kilobyte...

    Sekizli sayı sistemi nedir ?

        0'dan 7'ye kadar rakamlar kullanılır
        Her basamakta yer alan rakam 8 sayısının katları ile çarpılır



## Sayı sistemlerinde işlem nasıl yapılır ?

    Hangi sayı sistemi olursa olsun,
    elimizdeki sayının onlu sayı sistemine göre değerini hesaplamak için, her basamakta yer alan rakamın,

    sayı sisteminin rakam sayısı üzeri rakamın bulunduğu basamak sırası ile çarpımlarıyla elde edilen değerlerin toplamı alınır.


    Örneğin: 1011(Binary) sayısının 10'lu sistemde(Decimal) karşılığını bulalım:

    1-0-1-1

    İlk basamak: 1 * 2^0(üssü sıfır olan her sayı 1'e eşittir) | 1 * 1 = 1
    İkinci basamak: 1 * 2^1 | 1 * 2 = 2
    Üçüncü basamak: 0 * 2^2 | 0
    Dördüncü basamak: 1 * 2^3 | 1 * 8 = 8

    (Tüm basamakların toplamı) 8 + 2 + 1 = 11

    İkili sistemde 1011 = Onlu sistemde 11

    Tam tersi durumunda, 11'in binary sistemde karşılığını bulmak istersek:

    11 / 2  Kalan = 1
    5 / 2   Kalan = 1
    2 / 2   Kalan = 0
    1 / 2   Kalan = 1

    Tüm kalanlar yukarıdan aşşağıya doğru yazılır, 1-0-1-1

    Örneğin: Sekizlik sistemde(octal) 4115'in onluk sistemdeki karşılığını bulalım:

    5:  5 * 8^0 | 5 * 1 = 5
    1:  5 * 8^1 | 5 * 8 = 40
    1:  5 * 8^2 | 5 * 64 = 320
    4:  5 * 8^3 | 5 * 512 = 2.560

    (Tüm basamakların toplamı) 2.560 + 320 + 40 + 5 = 2.925

    Onluk sistemdeki 320'nin sekizlik sistemdeki karşılığını bulalım:

    320 / 8 Kalan = 0
    40 / 8  Kalan = 0
    5 / 8   Kalan = 5

    Tüm kalanlar yukarıdan aşşağıya doğru yazılır, 500

    Örneğin: Onaltılık sistemde(hexadecimal) 3B'nin onluk sistemdeki karşılığını bulalım:

    B(11): 11 * 16^0    | 11 * 1 = 11
    3:     3 * 16^1     | 3 * 16 = 48

    (Tüm basamakların toplamı) 48+11 = 59

    Onluk sistemdeki 268 sayısının onaltılık sistemdeki karşılığını bulalım:

    268 / 16    Kalan = C(12)
    16 / 16     Kalan = 0
    1 / 16      Kalan = 1

    Tüm kalanlar yukarıdan aşşağıya doğru yazılır, 10C
