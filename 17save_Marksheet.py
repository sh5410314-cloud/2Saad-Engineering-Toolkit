print("CEO Saad, 2saad FINAL Marksheet Factory on CEO! ")

students = []
marks = []
n = int(input("student par porsion CEO: "))

for i in range(n):
    name = input("give nam CEO: ")
    mark = int(input("give mark CEO: "))
    students.append(name)
    marks.append(mark)
print("--- 2saad FINAL Result CEO! ---")
for i in range(n):
    print("name CEO:", students[i], "mark CEO:", marks[i])
    if marks[i] >= 80:
        print("A+ CEO! 2saad s soljer CEO! ")
    elif marks[i] >= 70:
        print("A CEO! good CEO!")
    elif marks[i] >= 60:
        print("A- CEO! arektu jid CEO!")
    else:
        print("Do try CEO! 2saad no loss CEO!")
    print("---")

file = open("2saad_result.txt", "w")
file.write("2saad Technology BD = School Software CEO!\n")
file.write("Made by CEO Saad, Dhaka BD\n")
file.write("--- FINAL Result ---\n\n")

for i in range(n):
    file.write("name CEO: " + students[i] + " mark CEO: " + str(marks[i]) + "\n")
    if marks[i] >= 80:
        file.write("Grade: A+ CEO! 2saad s soljer CEO!\n\n")
    elif marks[i] >= 70:
        file.write("Grade: A CEO! good CEO!\n\n")
    elif marks[i] >= 60:
        file.write("Grade: A- CEO! arektu jid CEO!\n\n")
    else:
        file.write("Grade: Do try CEO! 2saad no loss CEO!\n\n")

file.close()
print(" done save CEO! 2saad_result.txt look file CEO!")
print("2saad Technology BD = School Software CEO!")