# Hard Code Values
Full_Name = "Tre Davis"
Student_Email = "todavis@aggies.ncat.edu"
Home_Town = "Atlanta, GA"
Grad_Semster = "Spring 2029"
Major_Degree = "Computer Engineering"

#Lists
Current_Course = ["COMP 163", "MATH 150", "ENG 101","GEEN 111"]
Completed_Course = []
Credit_Hours = [3, 3, 3, 3]
GPA_His = [3.8]


# Tuples
Emergency_Contact = ("Mom", "Hannah Smith", "704-555-0199")
Home_Addy = ("456 Oak Street", "Charlotte", "NC", 28202)
Instagram_Info = ("instagram", "@jordan_codes", 312)
Twitter_Info = ("Twitter", "@jordandev", 127)
Birth_Day = ("Birthday", 5, 22, 2006)

#Sets 
Current_Skills = {"Problem solving", "HTML", "Time management", "Photography", "Python basics"}
Skills_Learning = {"JavaScript", "Data structures", "Git", "Web design", "Public speaking"}
Career_Intrest = {"Software development", "Web development", "Game development", "Data science"}
Hobbies_Stuff = {"Gaming", "Photography", "Reading", "Soccer", "Music"}
Entertainment_Backlog = {"One Piece", "Barry", "Life", "incantation", "Memento"}

#Dictionary
Course_Credit = {"COMP 163":3, "MATH 150":3, "ENG 101":3, "HIS 105":3}
Course_Professor = {"COMP 163":"Prof. Rhodes", "MATH 150":"Dr. Lee", "ENG 101":"Dr. Martinez", "HIS 105":"Dr. Brown"}
Course_Room = {"COMP 163":"M-Eric 300", "MATH 150":"Marteena 201", "ENG 101":"Crosby 121", "HIS 105":"Crosby 210"}
Monthly_Bud = {"Food":450, "Entertainment":200, "Books":125, "Transportation":100}
Study_Hours = {"Programming":10, "Math":8, "English":4, "History":3}
Contact_direct = {"Mom":"704-555-0199", "Roommate":"336-555-7821", "Academic Advisor":"336-334-5000"}

#Calculations
Total_Credits = sum(Credit_Hours) 
Total_current_Credits = len(Current_Course)
Cum_GPA = (sum(GPA_His)/4)
Cum_GPA = round(Cum_GPA, 2)
Complete_Course_num = len(Completed_Course)
Total_Week_study = sum(Study_Hours.values())
Sum_study = sum(Course_Credit.values())
Academic_load = Total_Week_study + Sum_study
Monthly_Total_Bud = sum(Monthly_Bud.values())
Daily_Food_Bud = round((Monthly_Bud["Food"] / 30), 2)
Annual_Bud = Monthly_Total_Bud * 12
Study_Cost_Hour = round((Monthly_Bud["Books"] / Total_Week_study), 2)

#Anayltics Calculations
Total_Social_Followers = (Instagram_Info[2] + Twitter_Info[2])
Skills_Comparsion = (Current_Skills, ":", Skills_Learning)
Contact_Direct_Size = len(Contact_direct)
Entertain_Management = len(Entertainment_Backlog)
Current_Skills_1 = len(Current_Skills)
Skills_Learning_1 = len(Skills_Learning)

#Print Statements
print("================================================================")
print("              PERSONAL ACADEMIC & LIFE PORTFOLIO")
print("================================================================")

("PERSONAL ACADEMIC & LIFE PORTFOLIO")
print("Student:", Full_Name, "|", "Email:", Student_Email)
print("From:", Home_Town, "|", "Graduating:", Grad_Semster)
print("Major:", Major_Degree)

print("\n=== ACADEMIC PROFILE ===")
print("Current Semester:", Total_Credits, "credits", "across", Total_current_Credits, "courses" )
print("Cumulative GPA:", Cum_GPA)
print("Weekly Study Time:", Total_Week_study, "hours")
print(f"Academic Investment: ${Study_Cost_Hour} per study hour")

print("\nCurrent Courses:")
print(Current_Course[0], "-", Course_Credit["COMP 163"], "credits",  "-", Course_Professor["COMP 163"], "-", Course_Room["COMP 163"] )
print(Current_Course[1], "-", Course_Credit["MATH 150"], "credits", "-", Course_Professor["MATH 150"], "-", Course_Room["MATH 150"] )
print(Current_Course[2], "-", Course_Credit["ENG 101"], "credits", "-", Course_Professor["ENG 101"], "-", Course_Room["ENG 101"] )
print(Current_Course[3], "-", Course_Credit["HIS 105"], "credits", "-", Course_Professor["HIS 105"], "-", Course_Room["HIS 105"] )

print("\n=== PERSONAL DEVELOPMENT ===")
print("Current Skills:", Current_Skills)
print("Learning Goals:", Skills_Learning)
print("Career Interests:", Career_Intrest)
print("Skills Currently Have:", Current_Skills_1)
print("Skills Want to Learn:", Skills_Learning_1)

print("\n=== FINANCIAL OVERVIEW ===")
print(f"Monthly Budget: ${Monthly_Total_Bud}")
print(f"Food: ${Monthly_Bud["Food"]}", f"(${Daily_Food_Bud}/day)")
print(f"Entertainment: ${Monthly_Bud["Entertainment"]}")
print(f"Books: ${Monthly_Bud["Books"]}")
print(f"Transportation: ${Monthly_Bud["Transportation"]}")
print(f"Annual Projection: ${Annual_Bud}")

print("\n=== CONNECTIONS & CONTACTS ===")
print("Emergency Contact:", Emergency_Contact[1], f"({Emergency_Contact[0]})", "-", Emergency_Contact[2])
print(f"Home Address: {Home_Addy[0]}, {Home_Addy[1]}, {Home_Addy[2]} {Home_Addy[3]}")
print("Social Media Presence:", Total_Social_Followers, "followers across 2 platforms")
print("Key Contacts:", len(Contact_direct), "people in directory")

print("\n=== LIFE STATISTICS ===")
print("Total Courses Completed:", Complete_Course_num)
print("Current Academic Load:", Academic_load, "weekly commitments")
print("Entertainment Backlog:", len(Entertainment_Backlog), "items")
print("Current Hobbies:", len(Hobbies_Stuff), "activities")
print("================================================================")