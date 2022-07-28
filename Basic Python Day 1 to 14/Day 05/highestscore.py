studentscores=input('Input student scores').split()

for n in range(0,len(studentscores)):
    studentscores[n]=int(studentscores[n])

highest_score=studentscores[0]

for score in studentscores:
    if(highest_score<score):
        highest_score=score
print(f'The highest score is {highest_score}')
