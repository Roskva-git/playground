last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]


subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

#Update for computer science
subjects.append("computer science")
grades.append(100)

#Update for visual arts
subjects.append("visual arts")
grades.append(93)


#Combining the subjects and grades by zipping them together into tuples (zip-function), but the first part of the code specifies that it goes in a list form
gradebook = [[subject, grade] for subject, grade in zip(subjects, grades)]

#Accessing index and changing value
gradebook[-1][1] = 97
gradebook[2].remove(85)
gradebook[2].append("Pass")


#Full gradebook
full_gradebook = last_semester_gradebook + gradebook

#Print hallelujah
print(full_gradebook)
