height=int(input("enter your height(cm):"))
age=int(input("enter your age:"))
if height>150:
    print("Stratosfer,Family Karts,Scorpion Karts")
elif height>120 and height<150:    
    print("Fearfall,Invader,Corkscrew Roller Coaster,Bumber boatrs")
else:
    if height>90 and height<120:
        if age>=5:
            print("Los Banditos")
        if age==8:
            print("Robot Riot")
    elif height>80 and height<90:
        print("Log Flume,Gold Rush,Family Karts(passenger only),Dogems(oassenger only)")
    else:
        if age>=3 and age<=8:
            print("Fortress of Fun")


