studentheights = input('enter the list of student heights').split()

total_height=0.0
for height in studentheights:
    total_height+=float(height)

average=round(total_height/len(studentheights),2)
print(f'The average height is {average}')
