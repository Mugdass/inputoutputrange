while True:
    try:
        lrange = int(input('enter your lower range, -100 the lowest: '))
        hrange = int(input('enter your higher range, 100 the highest: '))
        if lrange < -100 or lrange > 100:
            raise ValueError #this will send it to the print message and back to the input option
        elif hrange < -100 or hrange > 100:
            raise ValueError
        break
    except ValueError:
        print("The input values are out side the input ranges Please check the numbers and try again Thanks for using our calculator")

        
