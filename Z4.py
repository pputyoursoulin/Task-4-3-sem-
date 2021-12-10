file = open('data.txt')

try:
    massiv = list(map(int, file.read().split()))

    if len(massiv) <= 2:
         print('Error!!! The data in the file is incorrect!\n-----')
    else:
         value1 = massiv[0]
         value2 = massiv[1]
         num = 0
         for i in range(3, len(massiv)):
            if (massiv[i] == value1) or (massiv[i] == value2):
                num = i + 1
         if num == 0:
             print('No such numbers were found...\n-----')
         else: print('№', num, '\n-----')
except ValueError:
    print('Error!!! The data in the file is incorrect!\n-----')

file.close()