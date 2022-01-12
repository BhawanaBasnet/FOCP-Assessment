import random

def mail_check():
    """This function will check the mail id"""
    print("Welcome to Pop Chat\nOne of our operators will be pleased to help you today.")
    used_data = input("Enter the mail id please:")
    if used_data:
        count = used_data.index("@")
        domain = "@pop.ac.uk"
        if count <= 2 or domain not in used_data: # check whether the enter the data is true or not.   
            print("worng mail id") 
        elif used_data == "":
            print("No data entered")
        else:
            chat_bod(used_data)

def words(num):
    """store the  data """
    list_1 = ("The library is closed today.")
    list_2  = ("Your deadline has been extended by two working days.")
    list_3 = ("Wifi is excellent across campus.")
    list_4 = ["Hmmmmmmmmm","what!!!!!!!!!!","oh, i see...","i don't know"]
    if num == 1:
        return (list_1)
    elif num == 3:
        return (list_2)
    elif num == 2:
        return (list_3)
    elif num == 4 : 
        return (random.choice(list_4))

def chat_bod(used_data):
    """this function is used to chat with the user """
    name = used_data.split("@") # spliting the data withe the help of  @
    user_e = name[0]  # indexing the value  
    user_name = user_e.capitalize() 
    name_list =["Bhawana","Anisha","Britney","Dikshya","Kripa"]
    print("Hi, {}! Thank you, and Welcome to PopChat!".format(user_name))
    print("My name is {}, and it will be my pleasure to help you.".format (random.choice(name_list)))
    num = (1,2,3,4,5,6,7,8,9,0)
    random_num = random.choice(num)
    if random_num == 1:
        print ("***Network Error***")
        print("Thanks, {}, for using PopChat. See you again soon!".format(user_name))
    else:    
        while True:
            input_data = input("--->")
            if input_data.capitalize() == "Exit" or input_data.capitalize() =="Goodbye" or input_data.capitalize() =="Bye" :
                print("Thanks,{} ,for using PopChat. See you again soon!".format(user_name)) 
                break
            elif "libery" in  input_data.lower():
                print(words(1)) 
            elif "wifi" in  input_data.lower():
                print(words(2))
            elif "deadline" in  input_data.lower():
                print(words(3))
            else :
                print(words(4))
mail_check()                 