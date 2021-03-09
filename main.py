def puissance(a, b):
  return a ** b


print(puissance(2,3))
#On peut aussi etre plus explicite
print(puissance(a=2, b=3))
#On peut utiliser les deux en meme temps:
print(puissance(2, b=3))

print(puissance(b=3, a=2))



def fonct(a,b,c):
  print(a, b,c)
  return a,b,c

fonct(1,2, c=4)

## Question 1

def somme(a, b):
  return a+b

print(somme(5,8))

## Question 2

fonct(1,2,4)



### Abstration des parametres

valeurs = 1,2
c,d = valeurs
res = somme(c,d)

print(res)

res2 = somme(*valeurs)
print(res2)

kw_valeurs = {'a': 0, 'b': 1}
res3 = somme(**kw_valeurs)
print(res3)


valeurs2 = 1,
kw_valeurs2 = {'b':1}
print(somme(*valeurs2, **kw_valeurs2))


## Question 3

k = [1,2] 
dic = {'c':2} 
fonct(*k,**dic)

## Question 3.1 :

valeurs = [[2,3], [3,3], [3,4]]
for i in valeurs :
  a,b = i
  print(a**b) 


### Parametres obligatoires et parametres 






