print("Stop! Who would cross the Bridge of Death") 
print("Must answer me these questions three, 'ere the other side he see.")
name=input("What is your name? ")
name_1 = name.capitalize()#Capatalized the first alphabet of the word stored in variable name_1
if ( "Arthur" not in name_1 ): #it checks the name is Arthur or not
    seek=input("What do you seek?")
    small = seek.lower()#it lower the string stored in variable small
    if "grail" in seek:
        colour=input("What is your favourite colour?")
        colour_1 = colour.capitalize()#it capatalize first alphabet of the word stored in variable colour_1
        if name_1[0]==colour_1[0]:#it is indexing which checks the first alphabet of name and colour 
            print("You may pass")
        else:
            print("Incorrect! You must now face the Gorge of Eternal Peril.")
    else:
        print("Only those who seek the Grail may pass.")
else:
    print("My liege! You may pass!")