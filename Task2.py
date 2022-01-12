print("Swallow Speed Analysis: Version 1.0")
eu_reading=[]
uk_reading=[]
while True:#infinite loop
    reading=input("Enter the Next Reading:")
    print("Reading saved")
    if reading =="":
        break
    elif reading[0]=="U" or reading[0]=="u":
        uk_reading.append(float(reading[1:]))
        eu_reading.append(float(reading[1:])*1.60934)#Covert into km
    elif reading[0]=="E" or reading[0]=="e" :
        eu_reading.append(float(reading[1:]))
        uk_reading.append(float(reading[1:])*0.621371)#convert into miles
    elif reading[0:] != "U" or reading[0:]!="u" and reading[0:] != "E" or reading[0:]!="e":
        print("wrong input")
if uk_reading!=[]:
    print("Result Summery:")
    print("Max speed: {:.1f} MPH {:.1f} KPH".format(max(eu_reading),max(uk_reading)))
    print("Min speed: {:.1f} MPH {:.1f} KPH".format(min(eu_reading),min(uk_reading)))
    print("Avg speed: {:.1f} MPH {:.1f} KPH".format(sum(eu_reading)/len(eu_reading),sum(uk_reading)/len(uk_reading))) 
else:
    print("No readings entered. Nothing to do.")