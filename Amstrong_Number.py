# Amstrong Sayısı
print("***********************************************")
print("Amstrong Sayısı Bulma Programına Hoşgeldiniz...")
print("***********************************************\n")
while True:
  amstrong_sayisi = input ('Bir sayı giriniz... ')
  if not amstrong_sayisi.strip().lstrip('+-').isdigit():
    print (amstrong_sayisi, 'bir sayı değildir.\n')
    
  elif int (amstrong_sayisi)<0 :
      print("Negatif sayı giremezsiniz...\n")
      
  elif int (amstrong_sayisi)==0:
      print("Şaka mı bu, sıfır tabiki Amstrong sayısı. Tekrar deneyin...\n")
      
  else:
      new_amstrong = 0
      for i in amstrong_sayisi:
         new_amstrong += pow(int(i), len(amstrong_sayisi))
      if new_amstrong == int(amstrong_sayisi):
        print(amstrong_sayisi, "bir Amstron sayısıdır.")
      else:
         print("Malesef", amstrong_sayisi, "bir Amsatron sayısı değildir.")
      break
print("\n***********************************************")
print("Amstrong Sayısı Bulma Programı Çıkış...")
print("***********************************************")
