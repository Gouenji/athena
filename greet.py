from datetime import datetime
import random

def get_greet(f):

    polite_tolerance = 3
    humor_tolerance = 3
    hour = datetime.now().hour
    if hour < 12:
        lt = "Morning"
    elif hour > 17:
        lt = "Night"
    else:
        lt = "Afternoon"


    greetings = open("data/personality.txt").read().split("\n")
    file = open("data/output.txt").read().split("\n")
    polite = int(file[0].split("polite=")[1])
    humor = int(file[1].split("humor=")[1])
    phrase_array = []

    for greet in greetings:
        try:
            class_list = greet.split(':')[1].split(",")
            phrase = greet.split(":")[0]
            if class_list[0] == lt or class_list[0] == "Neutral":
                values_list = class_list[1].split(";")
                polite_val = int(values_list[0].split('polite=')[1])
                if polite in range(polite_val - polite_tolerance,
                                   polite_val + polite_tolerance):
                    humor_val = int(values_list[1].split("/")[0].split("humor=")[1])
                    if humor in range(humor_val - humor_tolerance,
                                      humor_val + humor_tolerance):
                        salutation = values_list[1].split("/")[1].split("f=")[1]
                        if salutation == f:
                            phrase_array.append(phrase)
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            else:
                pass
        except IndexError:
            pass
    finalout = random.choice(phrase_array)
    return finalout
if __name__=="__main__":
	print(get_greet("hello"))
	print(get_greet("goodbye"))
