from  area import Area

b = float(input('Enter base: '))
h = float(input('Enter high: '))

aobj = Area()
aobj.base = b
aobj.high = h
print(f'area = {aobj.compute_area()}')