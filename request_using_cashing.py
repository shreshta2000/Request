import json
import requests
import os

# Calling Api 
if os.path.isfile("courses.json"):
    with open("courses.json","r") as Data:
        Text_Data=json.load(Data)

else:
    saral_url  = "http://saral.navgurukul.org/api/courses"
    Data = requests.get(saral_url)
    Text_Data=Data.json()
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
# # calling parents Api
if os.path.isfile("parent/"+selected_Courses_name+str(parent_id)+".json"):
    with open ("parent/"+selected_Courses_name+str(parent_id)+".json","r") as Data1:
        converting_parent_data = json.load(Data1)
else:
    parent_url = ("https://saral.navgurukul.org/api/courses/" +  str(parent_id) +"/exercises" )
    Data_2 = requests.get(parent_url)
    converting_parent_data = Data_2.json()
    with open("parent/"+selected_Courses_name+str(parent_id)+".json","w")as parent_courses:
        file3 = json.dump(converting_parent_data,parent_courses,indent=4)

# # for calling parent course

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
    
# # for print one specific parent course
        
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
child_id = converting_parent_data["data"][choose_parent_exercises_no-1]["id"]
print(choose_parent_exercises_no,parent_exercises,"id.",child_id)

#for calling a specific parent child
if converting_parent_data["data"][choose_parent_exercises_no-1]["childExercises"]== []:
    print("     1.",converting_parent_data["data"][choose_parent_exercises_no-1]["slug"])
else:
    l = 0
    while l < len(converting_parent_data["data"][choose_parent_exercises_no-1]["childExercises"]):
        print("     ",l+1,converting_parent_data["data"][choose_parent_exercises_no-1]["childExercises"][l]["name"])
        l = l+1  
    choose_child_exercises_no = int(input("entre the specific child exercises : "))
    slug = (converting_parent_data["data"][choose_parent_exercises_no-1]["childExercises"][choose_child_exercises_no-1]["slug"])
# for calling a specific childexercises
    if os.path.isfile("child/"+ parent_exercises + str(child_id)+".json"):
        with open("child/"+ parent_exercises + str(child_id)+".json","r") as Data3:
            converting_child_exercise_data = json.load(Data3)
    else:
        child_exercises_url = ("http://saral.navgurukul.org/api/courses/" +  str(parent_id) +"/exercise/getBySlug?slug=" + slug )
        Data_4 = requests.get(child_exercises_url)
        converting_child_exercise_data = Data_4.json()
        with open("child/"+ parent_exercises + str(child_id)+".json","w") as ChildExercise:
            file4 = json.dump(converting_child_exercise_data,ChildExercise,indent=4)
print(converting_child_exercise_data["content"])    
            
    