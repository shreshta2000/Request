import json
import requests

# Calling Api 

saral_url  = "http://saral.navgurukul.org/api/courses"
Data = requests.get(saral_url)

# Coverting into Json

Text_Data=Data.json()

# to find out courses name  

with open("courses.json","w") as saral_courses:
    file2  = json.dump(Text_Data,saral_courses,indent=4)
i=0
while i<len(Text_Data["availableCourses"]):
    Courses_name = (Text_Data["availableCourses"][i]["name"])
    print(i+1,".",Courses_name,",Id.",Text_Data["availableCourses"][i]["id"])
    i+=1

# taking user input for print all topic of one specific courses

choose_course_no = int(input("entre the any course no : "))
selected_Courses_name = Text_Data["availableCourses"][choose_course_no-1]["name"]
parent_id = Text_Data["availableCourses"][choose_course_no-1]["id"]
print(selected_Courses_name)
up_nagitation = input("do you want to contine yes or no : ")
if up_nagitation == "no":
    i=0
    while i<len(Text_Data["availableCourses"]):
        Courses_name = (Text_Data["availableCourses"][i]["name"])
        print(i+1,".",Courses_name,",Id.",Text_Data["availableCourses"][i]["id"])
        i+=1
    choose_course_no = int(input("entre the any course no : "))
    selected_Courses_name = Text_Data["availableCourses"][choose_course_no-1]["name"]
    parent_id = Text_Data["availableCourses"][choose_course_no-1]["id"]
    print(selected_Courses_name)
# calling parents Api

parent_url = ("https://saral.navgurukul.org/api/courses/" +  str(parent_id) +"/exercises" )
Data_2 = requests.get(parent_url)

# converting parent data into Json

converting_parent_data = Data_2.json()

# pushing data into json file

with open("parent.json","w")as parent_courses:
    file3 = json.dump(converting_parent_data,parent_courses,indent=4)

# for calling parent course

j = 0
while j < len(converting_parent_data["data"]):
    parent_course = converting_parent_data["data"][j]["name"]
    print(" ",j + 1,parent_course)

# for calling childexercises or slug

    if converting_parent_data["data"][j]["childExercises"] == []:
        slug = converting_parent_data["data"][j]["slug"]
        print("     ","1.",slug)
    else:
        k = 0
        while k < len(converting_parent_data["data"][j]["childExercises"]) :
            child_exercises = converting_parent_data["data"][j]["childExercises"][k]["name"]
            print("     ",k+1,".",child_exercises)
            k = k + 1
    j = j + 1
    
# for print one specific parent course
        
choose_parent_exercises_no = int(input("entre the specific parent exercises : "))
up_nagitation1 = input("do you want to continue or do you want courses name yes/no: ")
if up_nagitation1 == "no":
    # for calling parent course

    j = 0
    while j < len(converting_parent_data["data"]):
        parent_course = converting_parent_data["data"][j]["name"]
        print(" ",j + 1,parent_course)

    # for calling childexercises or slug

        if converting_parent_data["data"][j]["childExercises"] == []:
            slug = converting_parent_data["data"][j]["slug"]
            print("     ","1.",slug)
        else:
            k = 0
            while k < len(converting_parent_data["data"][j]["childExercises"]) :
                child_exercises = converting_parent_data["data"][j]["childExercises"][k]["name"]
                print("     ",k+1,".",child_exercises)
                k = k + 1
        j = j + 1
    choose_parent_exercises_no = int(input("entre the specific parent exercises : "))
parent_exercises = converting_parent_data["data"][choose_parent_exercises_no-1]["name"]
print(choose_parent_exercises_no,parent_exercises,"id.",converting_parent_data["data"][choose_parent_exercises_no-1]["id"])

#for calling a specific parent child
if converting_parent_data["data"][choose_parent_exercises_no-1]["childExercises"]== []:
    print("     1.",converting_parent_data["data"][choose_parent_exercises_no-1]["slug"])
else:
    l = 0
    my_list = []
    while l < len(converting_parent_data["data"][choose_parent_exercises_no-1]["childExercises"]):
        print("     ", l+1 ,converting_parent_data["data"][choose_parent_exercises_no-1]["childExercises"][l]["name"])
# for calling a specific childexercises

    
        slug = (converting_parent_data["data"][choose_parent_exercises_no-1]["childExercises"][l]["slug"])
        child_exercises_url = ("http://saral.navgurukul.org/api/courses/" +  str(parent_id) +"/exercise/getBySlug?slug=" + slug )
        Data_4 = requests.get(child_exercises_url)

#converting child exercise into json

        converting_child_exercise_data = Data_4.json()

#pusing data into json file

        with open("child.json","w") as ChildExercise:
            file4 = json.dump(converting_child_exercise_data,ChildExercise,indent=4)
        content = converting_child_exercise_data["content"]
        my_list.append(content)
        l = l + 1
    choose_child_exercises_no = int(input("entre the specific child exercises : "))
    print(my_list[choose_child_exercises_no-1])
    count = choose_child_exercises_no - 1
    while choose_child_exercises_no > 0 :
        next_nagitation3 = input("do you next question or previous question n/p : ")
        if choose_child_exercises_no == len(my_list):
            print("next page")
        if next_nagitation3 == "p" :
            if choose_child_exercises_no == 1:
                print("no more questions")
                break
            elif choose_child_exercises_no > 0:
                choose_child_exercises_no = choose_child_exercises_no - 2
                print(my_list[choose_child_exercises_no])
        elif next_nagitation3 == "n":
            if choose_child_exercises_no < len(my_list):
                index = choose_child_exercises_no + 1
                print(my_list[index-1])
                count = count + 1
                choose_child_exercises_no = choose_child_exercises_no + 1 
                if count == (len(my_list)-1) :
                    print("next page")
                    break
        
            
    