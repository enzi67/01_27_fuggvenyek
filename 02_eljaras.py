
'''
Az argumentum (aktuális paraméter) lehet érték, kifejezés, változó is!
Az 'x', 'y' és 'eredmeny' nevű változók LOKÁLISAK, csak az eljáráson belül érhetők el! 
'''
def osszead(x, y):
      eredmeny = x + y
      print('A két szám összege: ', eredmeny)
      return eredmeny


osszead(10, 9)
print(osszead(10, 9)) #None, returnnel kiírja
osszead(5+5, 5+4)
print(osszead(5+5, 5+4)) #None, returnnel kiírja

a = 10
b = 9
osszead(a, b) 
  