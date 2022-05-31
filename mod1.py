def eua(a, b):
    r=[a, b]
    q=[r[0]//r[1]]
    i=1
    s=[1, 0]
    t=[0, 1]
    while 1:
        r.append(r[i-1]-q[i-1]*r[i])
        s.append(s[i-1]-q[i-1]*s[i])
        t.append(t[i-1]-q[i-1]*t[i])
        if r[i+1]==0:
            break
        q.append(r[i]//r[i+1])
        i=i+1
    if t[-2]>=0:
        return t[-2]
    else:
        return a+t[-2]


#Генерация ключевой информации
p=89
q=144
N=p*q
e=5
fiN=(p-1)*(q-1)
d=eua(fiN, e)
print('Open key: (',e,',',N,')')
print('Private key: (',d,',',N,')')