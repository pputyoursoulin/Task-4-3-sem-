file = open('data.txt')

try:
    massiv1 = list(map(int, file.readline().split()))
    massiv2 = list(map(int, file.readline().split()))
    if len(massiv1) < 1 or len(massiv2) < 1:
         print('Error!!! The data in the file is incorrect!')
    else:
         if(all(massiv1[i] <= massiv1[i + 1] for i in range(len(massiv1)-1))):
             if(all(massiv2[i] <= massiv2[i + 1] for i in range(len(massiv2)-1))):
                 massiv3 = massiv1 + massiv2
                 massiv3.sort()
                 print(massiv3) 
             else: print('Error!!! The data in the file is incorrect!')
         else: print('Error!!! The data in the file is incorrect!')
except ValueError:
    print('Error!!! The data in the file is incorrect!\n-----')

file.close()