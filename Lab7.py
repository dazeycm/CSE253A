from tkinter import *

root = Tk()
root.title('Grade Calculator')
titles = ['Course1', 'Course2', 'Course3', 'Course4', 'Course5']

def makeEntities(root):
    grades = []
    weights = []
    for i in range(len(titles)):
        row = Frame(root)
        label = Label(row, width = 10, text = titles[i], anchor = 'w')
        grade = Entry(row)
        weight = Entry(row)
        label.grid(row = 0, column = 0)
        grade.grid(row = 0, column = 1)
        weight.grid(row = 0, column = 2)
        row.pack(side = TOP, fill = X, padx = 5, pady = 5)
        grade.insert(0, 'B')
        weight.insert(0, 3)
        grades.append(grade)
        weights.append(weight)
    return grades, weights
        

def compute():
    qualityPoints = 0
    totalCredits = 0
    for i in range(len(grades)):
        gradeValue = 0
        grade = str(grades[i].get())
        if grade == 'A+' or grade == 'A':
            gradeValue = 4
        elif grade == 'A-':
            gradeValue = 3.67
        elif grade == 'B+':
            gradeValue = 3.33
        elif grade == 'B':
            gradeValue = 3.00
        elif grade == 'B-':
            gradeValue = 2.67
        elif grade == 'C+':
            gradeValue = 2.33
        elif grade == 'C':
            gradeValue = 2.00
        elif grade == 'C-':
            gradeValue = 1.67
        elif grade == 'D+':
            gradeValue = 1.33
        elif grade == 'D':
            gradeValue = 1.00
        elif grade == 'D-':
            gradeValue = 0.67
        elif grade == 'F':
            gradeValue = 0;
        
        weight = int(weights[i].get())
        totalCredits += weight
        qualityPoints += gradeValue * weight
        
    print("GPA: %.2f" % (qualityPoints / totalCredits))
        
        

grades, weights = makeEntities(root)
b1 = Button(root, text = 'Compute', command = compute)
b1.pack(side = LEFT, padx = 5, pady = 5)
b2 = Button(root, text = 'Quit', command = sys.exit)
b2.pack(side = LEFT, padx = 5, pady = 5)

root.mainloop()