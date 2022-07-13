str = "ABHSGSUAAHYSTSJAAUUSA"

count = 0

for i in str:
    if i == 'A':
        count = count +1
        
        
print(count)


str = "eeeeeE"
count = 0
for i in str:
    if i in ('e','E'):
        count+=1
        
print(count)

#https://stackoverflow.com/questions/39560387/count-a-characterboth-uppercase-and-lowercase-in-a-string-using-a-for-loop-in