#numbers=[3,1,4,1,5,9,2]
import os
folderName=os.listdir('test/A/B')
print(folderName)

sorted_folderName=sorted(folderName,key=lambda x:tuple(map(int,x.split('_'))))
print(sorted_folderName)
#Sorted_numbers_desc=sorted(numbers, reverse=False)
#print(f"정렬:{sorted_numbers_desc}")
