def cgpacalc(mark,n):
   grade = [0] * n
   sum = 0
   for i in range(n):
     grade[i]=(marks[i]/10)
   for i in range(n):
     sum +=grade[i]
   cgpa = sum /n
   return cgpa
n=5
marks=[90,80,70,80,90]
cgpa=cgpacalc(marks,n)
print("CGPA=",'%.if'% cgpa)
print("CGPA percentage=",'%.2f'% (cgpa * 9.5))