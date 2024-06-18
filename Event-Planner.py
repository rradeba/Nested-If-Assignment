# Task 1-3
attendees = int(input("Enter number of attendees: "))
venue = "Large hall" 
if attendees > 100:
    print(venue + " is recommended. Normal projector and speakers are sufficient.") 
    if attendees > 150:
        print("Enhanced projector is also recommended for video presentations at addiional charge.")
    if attendees > 175:
        print("Large speakers are recomended for audio system at additional charge.")
else: "Conference room recommended"


vegetarian_catering = input("Would you prefer a vegetarian caterer? (Y/N) ")

if vegetarian_catering == "Y":
    print("We recommend catering from Veggie Delight Caterers.")
elif vegetarian_catering == "N":
    print("We recommend Gourmet Meals Caterers.")
else: 
    print("Please answer Y or N")

