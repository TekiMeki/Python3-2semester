from re import findall

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

listb={'you': '492', '-': '452', 'ch': '241'}
mes='Fuck 492 452 bit241'
listNum=findall(r"[0-9]{3}", mes)
res=''
for i in listNum:
    mes=mes.replace(i, get_key(listb, i))
    res=mes
print(res)