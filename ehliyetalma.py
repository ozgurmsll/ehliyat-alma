isim= input('isim : ')
yas= int(input('yaşınız: '))
egitim= input(' eğitiminiz: ')
if (yas>=18):
    if( yas >= 18) and (egitim=='lise'or egitim== 'üniversite' ):
        print(f'{isim} Ehliyet alabilirsin')
    
    else:
        print(f'Ehliyet alamazsınız eğitimin tutmuyor {isim}')
else:
    print(f'Ehliyet alamazsınız yaşınız tutmuyor {isim}')
