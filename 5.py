a = int(input("Enter a number: ")) 
binary_representation = bin(a)
if a in range(228, 255):
    print("True: ", binary_representation)
else:
    print("False: ", binary_representation)