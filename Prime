print (*[('-'*(40))])
print(*[('*** Asal Sayı Doğrumala Programı ***').center(40)], sep='\n')
print (*[('-'*(40))], sep='\n')
def prime ():
  num = input ('Bir sayı giriniz...: ')
  if not num.lstrip('+-').isdigit():
    print (num, 'bir sayı değildir.\n')
  elif int (num)<0 :
    print("Negatif Asal sayı yoktur.")
  elif int (num)==0:
    print("Sıfır Asal sayı değildir.")
  else:
    num = int (num)
    if num > 1:
      for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
      else:
        print(num, "is a prime number")
 
    else:
      print(num, "is not a prime number")
prime()
print (*[('-'*(40))])
print(*[('*** Çıkış ***').center(40)])
print (*[('-'*(40))])
