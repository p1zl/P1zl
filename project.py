student1 = "I am in school"
student2 = "I am in course"
mathleson1 = (" what answer of 10 * 5? ")
while True:
    try:
        answer = int(input("your answer: "))
        if answer == 50:
            print ("True")
            break
        else:
            print ("False, try again.")
    except ValueError:
        print("Invalid input, please enter a number.")
Math = mathleson1
Basketball = ("Correct vision of the ball")
PE = Basketball
History_USA = ("All Usa presidents")
Social_Science = History_USA
Birds = "Ornithology is the science of birds and has many practitioners with advanced degrees, several universities that offer related degrees, and many organizations and journals that serve to disseminate the information in the field. There are very few universities that offer degrees in ornithology, though. See Careers in Ornithology for detailed information on training and jobs. There are many ornithologists working in the public and private sector, in the field, in museums, and in the lab. If you want to find out more about what professional ornithologists do, some resources are listed below. Send your request to do my research proposal  and get a well-written proposal for your research paper or dissertation on ornithology topics."
Science = Birds
English = ("what words do you use to say whan you can help another human?")
while True:
    word = input("Enter this word: ")
    if word.lower() == "can":
        print ("Nice job!")
        break
    else: 
        print ("no sorry, think carefully. Try again.")
settings_school = [Math, PE, Social_Science, Science, English,]
European_countries = ("Ukraine", "Iceland", "Poland", "Germany")
Geography = European_countries
settings_course = [Geography]
if student1 is "I am in course":
    print (settings_course)
else: 
    print (settings_school)
if student2 is "I am in course":
    print (settings_course)
else:
    print (settings_school)