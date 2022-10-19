num = int(input('pls input height of pyramid : '))

for i in range(num):
    print((' '*int(num-(i+1))) + '*'*(i*2 + 1))
