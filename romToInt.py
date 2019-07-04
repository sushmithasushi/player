def acb(xus):
  switc={
    'I':1,
    'II':2,
    'III':3,
    'IV':4,
    'V':5,
    'VI':6,
    'VII':7,
    'VIII':8,
    'IX':9,
    'x':10,
    'XI':11,
    'XII':12,
    'XIII':13,
    'XVI':14,
    'XV':15,
    'XVI':16,
    'XII':17,
    'XIII':18,
    'XIX':19,
    'XX':20

  }
  x=switc[xus]
  return x
  
x=str(input())
print(acb(x))


