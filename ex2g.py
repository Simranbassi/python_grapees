print("enter the marks according to the subject")
maths=int(input("enter the marks of students in maths :" ))
english=int(input("enter the marks of students in english:"))
hindi=int(input("enter the marks of students in hindi:" ))
science=int(input("enter the marks of students in science :" ))
socialscience=int(input("enter the marks of students in socialscience"))
total=maths+english+hindi+science+socialscience
per=(total/500)*100
print("the percentage of marks that the student will get",per)