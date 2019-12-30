ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ','LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

tuplets=((a,b)  for a in ports for b in ports)
counter=0
while True:
    try:
        print(next(tuplets))
        counter+=1
    except Exception:
        print("calosc {}".format(counter))
        break

print(tuplets)

tuplets2=[(a,b) for a in ports for b in ports[ports.index(a):] if b!=a]

print(tuplets2)

print(len(tuplets2))