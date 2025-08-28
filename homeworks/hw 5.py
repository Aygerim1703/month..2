from distance import Distance

d1 = Distance(500, 'cm')
d2 = Distance(2, 'm')
d3 = Distance(1, 'km')

print(d1)
print(d2)
print(d3)


print(d1 + d2)
print(d2 + d3)


print(d3 - d2)


print(d1 < d2)
print(d1 == Distance(5, 'm'))
print(d3 > d2)