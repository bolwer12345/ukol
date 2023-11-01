def kvadrrovnice(a,b,c):
    import math
    resenikvadrrovnice=[]
    if float(a)==0:
        x=-float(c)/float(b)
        resenikvadrrovnice.append(f'Um ve skutečnosti, toto není kvadratická rovnice, ale řešení této lineární rovnice je:{x}')
    else:
        d=(float(b))**2-(4*(float(a))*(float(c)))
        if d<0:
            resenikvadrrovnice.append('Rovnice nemá řešení')
        if d>0:
            x1=(-float(b)+math.sqrt(float(d)))/(2*float(a))
            x2=(-float(b)-math.sqrt(float(d)))/(2*float(a))
            resenikvadrrovnice.append(x1)
            resenikvadrrovnice.append(x2)
        if d==0:
            x1=(-float(b)+math.sqrt(float(d)))/(2*float(a))
            resenikvadrrovnice.append(x1)
    return resenikvadrrovnice
def prvocislo(n):
    prvocisla=[]
    for num in range(0, int(n) + 1):  
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prvocisla.append(num)
    return prvocisla
def obdélník(a,b):
    list=[]
    list1=[]
    list2=[]
    for i in range (int(a)):
        if i==0 or i==int(a)-1:
            list1.append('*')
            list2.append('*')
        else:
            list1.append('*')
            list2.append(' ')
    for i in range (int(b)):
        if i==0 or i==int(b)-1:
            list.append(list1)
        else:
            list.append(list2)
    return list
while True:
    t=input('Zadej 1 pro řešení kvadratické rovnice, 2 pro vypsání prvočísel do daného čísla, 3 pro obdélník z hvězdiček v zadaných rozměrech, 4 pro vypnutí programu')
    if int(t)==1:
        u=input('Zadej a ')
        v=input('Zadej b ')
        w=input('Zadej c ')
        q=kvadrrovnice(u,v,w)
        print(f'{q}')
    elif int(t)==2:
        u=input('Zadej číslo do kterého chceš prvočísla ')
        q=prvocislo(u)
        print(f'{q}')
    elif int(t)==3:
        u=input('Zadej šířku obdélníku ')
        v=input('Zadej výšku obdélníku ')
        q=obdélník(u,v)
        for i in q:
            print(i)
    elif int(t)==4:
        break
    else:
        print('wtf kmo tam třeba dej správnej input')
