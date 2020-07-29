# set 集合
bri = set(['brazil', 'russia', 'india'])

if 'india' in bri:
    print("True")
else:
    print("False")

if 'usa' in bri:
    print("True")
else:
    print("False")

bric = bri.copy()
bric.add('china')

if bric.issuperset(bri):
    print("True")
else:
    print("False")

bri.remove('russia')

print(bri & bric)       # OR bri.intersection(bric)
