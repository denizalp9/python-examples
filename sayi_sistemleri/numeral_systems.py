def decToBin(dec):
    try:

        bin = []
        binString = ''
        decimal = int(dec)
        if decimal < 0: # Sayı sıfırdan küçükse, negatifse
            return 'Negative input recieved, cannot convert negative on current mode.'

        while decimal > 1: # Sayı birden büyük olduğu sürece aşşağıdakileri yap:
            mod = decimal % 2 # Sayının 2'ye bölümünün kalanı
            if mod > 0: # Kalan 0'dan büyükse
                decimal = decimal // 2 # Sayıyı 2'ye böl ve kalanları umursama
                bin.append(mod) # Kalanı listeye ekle
            elif mod == 0: # eğer kalansız bölünüyor ise
                decimal = int(decimal / 2) # tek / bölme işlemi 'float' dönüdürüyor
                bin.append(mod) # Kalanı(0) listeye ekle

        bin.append(decimal) # Sayıyı listeye ekle(Burada sayı 1 veya 0'a eşit oluyor)

        for i in bin[::-1]: # Kalan listesini ters çevir, içindeki her elemanı:
            binString += str(i) # 'binString' değişkenine ekle
        return binString # değişkeni döndür

    except ValueError: # Eğer integer değer girilmediyse
        return 'Non-decimal input recieved, cannot convert non-decimal on current mode.'

def binToDec(bin):
    dec = 0
    curr = -1
    try:
        for num in str(bin):   # Eğer girilen sayının içinde:
            if int(num) != 1 and int(num) != 0:   # 1 veya 0 yoksa (pozitif)
                return 'Non-binary or negative input recieved, cannot convert non-binary or negative on current mode.'

        for i in str(bin)[::-1]: # girilen sayıyı normalde soldan sağa okuyor, o yüzden sayıyı ters çevirip okutuyorum

            curr += 1
            dec += int(i) * 2**curr

        return str(dec)

    except ValueError:
        return 'Non-binary input recieved, cannot convert non-binary on current mode.'


def decToOct(dec):
    try:

        oct = []
        octString = ''
        decimal = int(dec)
        if decimal < 0: # Sayı sıfırdan küçükse, negatifse
            return 'Negative input recieved, cannot convert negative on current mode.'
        elif decimal == 0:
            return str(decimal)

        while decimal >= 1: # Sayı birden büyük olduğu sürece aşşağıdakileri yap:
            mod = decimal % 8 # Sayının 8'ye bölümünün kalanı

            if mod > 0: # Kalan 0'dan büyükse
                decimal = decimal // 8 # Sayıyı 8'ye böl ve kalanları umursama
                oct.append(mod) # Kalanı listeye ekle

            elif mod == 0: # eğer kalansız bölünüyor ise
                decimal = int(decimal / 8) # tek / bölme işlemi 'float' dönüdürüyor
                oct.append(mod) # Kalanı listeye ekle

        for i in oct[::-1]: # Kalan listesini ters çevir, içindeki her elemanı:
            octString += str(i) # 'octString' değişkenine ekle
        return octString # değişkeni döndür

    except ValueError: # Eğer integer değer girilmediyse
        return 'Non-decimal input recieved, cannot convert non-decimal on current mode.'

def octToDec(oct):
    dec = 0
    curr = -1
    try:
        for num in str(oct):  # Eğer girilen sayının içinde:
            if int(num) == 8 or int(num) == 9 or int(num) < 0:  # 8 veya 9 varsa veya sayı negatifse
                return 'Non-octal or negative input recieved, cannot convert non-octal or negative on current mode.'

        for i in str(oct)[::-1]:  # girilen sayıyı normalde soldan sağa okuyor, o yüzden sayıyı ters çevirip okutuyorum

            curr += 1
            dec += int(i) * 8 ** curr

        return dec

    except ValueError:
        return 'Non-octal or negative input recieved, cannot convert non-octal or negative on current mode.'

def decToHex(dec):
    hexKeywords = ['A','B','C','D','E','F']
    try:

        hex = []
        hexString = ''
        decimal = int(dec)
        if decimal < 0: # Sayı sıfırdan küçükse, negatifse
            return 'Negative input recieved, cannot convert negative on current mode.'
        elif decimal == 0:
            return str(decimal)

        while decimal >= 1: # Sayı birden büyük olduğu sürece aşşağıdakileri yap:
            mod = decimal % 16 # Sayının 16'ya bölümünün kalanı
            if mod > 0 and mod <= 9: # Kalan 0'dan büyükse ve 9 dan küçükse
                decimal = decimal // 16 # Sayıyı 16'ya böl ve kalanları umursama
                hex.append(mod) # Kalanı listeye ekle
            elif mod >= 10 and mod <= 15: # Eğer kalan 10 ile 15 arasındaysa (A,B,C,D,E,F'ye dönüştürmek için)
                for num in range(10,16): # kalanın 10 ile 15 arasından hangisi olduğunu bul
                    if num == mod:

                        decimal = decimal // 16 # Girilen sayıyı 16'ya böl
                        hex.append(hexKeywords[mod - 10]) # Listeye harfi ekle

            elif mod == 0: # eğer kalansız bölünüyor ise
                decimal = int(decimal / 16) # tek / bölme işlemi 'float' dönüdürüyor
                hex.append(mod) # Kalanı listeye ekle

        for i in hex[::-1]: # Kalan listesini ters çevir, içindeki her elemanı:
            hexString += str(i) # 'hexString' değişkenine ekle
        return hexString # değişkeni döndür

    except ValueError: # Eğer integer değer girilmediyse
        return 'Non-hex input recieved, cannot convert non-hex on current mode.'

def hexToDec(hex):
    hexKeywords = ['A', 'B', 'C', 'D', 'E', 'F'] # Burada listelerin indexlerini Harflerin karşılık geldiği sayıyı bulmak için kullanacağım, dict gibi.
    hexNumbers = [10,11,12,13,14,15]
    dec = 0
    hexL = list()
    curr = -1
    try:
        for num in str(hex).upper():  # Girilen hex'in içindeki tüm harfleri büyük harf yapıp öyle kontrol ediyorum.
            if num in hexKeywords: # Eğer harf girildiyse
                 num = hexNumbers[hexKeywords.index(num)] # Harfe karşılık gelen sayıyı bul
                 hexL.append(num) # Sayıyı listeye ekle

            elif int(num) <= 9 and int(num) >= 0: # Eğer girilen sayıysa ve negatif değilse
                hexL.append(num) # Sayıyı listeye ekle
            else:
                 return 'Non-hex or negative input recieved, cannot convert non-hex or negative on current mode.'


        for i in hexL[::-1]:  # listeyi normalde soldan sağa okuyor, o yüzden listeyi ters çevirip okutuyorum

            curr += 1
            dec += int(i) * 16 ** curr

        return dec

    except ValueError:
        return 'Non-hex or negative input recieved, cannot convert non-hex or negative on current mode.'

def binToOct(bin):
    dec = binToDec(bin)
    return decToOct(bin)

def binToHex(bin):
    dec = binToDec(bin)
    return decToHex(dec)

def octToBin(oct):
    dec = octToDec(oct)
    return decToBin(dec)

def octToHex(oct):
    dec = octToDec(oct)
    return decToHex(dec)

def hexToBin(hex):
    dec = hexToDec(hex)
    return decToBin(dec)

def hexToOct(hex):
    dec = hexToDec(hex)
    return decToOct(dec)

# Todo: 2 ile 9 arasında custom sayı sistemi

if __name__ == '__main__': # Eğer bu .py dosyası import edilmemiş, direk dosyanın kendisi çalıştırılmışsa:
    while True:
        #print(decToBin(input('Dec to Bin: ')))
        #print(binToDec(input('Bin to Dec: ')))
        #print(decToOct(input('Dec to Oct: ')))
        #print(octToDec(input('Oct to Dec: ')))
        #print(decToHex(input('Dec to Hex: ')))
        #print(hexToDec(input('Hex to Dec: ')))
        #print(binToOct(input('Bin to Oct: ')))
        #print(binToHex(input('Bin to Hex: ')))
        #print(octToBin(input('Oct to Bin: ')))
        #print(octToHex(input('Oct to Hex: ')))
        #print(hexToBin(input('Hex to Bin: ')))
        #print(hexToOct(input('Hex to Oct: ')))
        pass
