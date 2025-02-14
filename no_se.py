'''
3

# # #
  #
#
 #
  #
'''
print("Ingrese un numero")
number=int(input())

for m in range(number):
    print("# ",end="")   #primer paso listo

print("")

m = number -1

for j in range(1,number):

    for g in range(1,m):
        print("  ", end = "")

    m-=1
    print("#")

for n in range(1, number):
    
    for ñ in range(0, n):
        print(" ", end ="")

    print("#")

print("")