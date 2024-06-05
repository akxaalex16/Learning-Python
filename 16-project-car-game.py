# help should show:
# start - to start the car
# stop - to stop the car
# quit - to exit
# if you type anything else then it is going to say: "I dont understand that"

command= ""
started= False
while True:    
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started...Ready to go!")
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car stopped")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
              """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that...")