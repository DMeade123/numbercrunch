def process_numbers(): #define process numbers function
    total = 0 #declare adjustable variable
    try:    #create try/except/finally block
        with open("numbers.txt", "r") as numfile: #open and close numfile for reading when block is ran
            for line in numfile: #create for loop to read each line in numfile
                total += float(line.strip()) #sum each line and assign it to total variable

        with open("sum.txt", "w") as sumfile: #write sum in blank file
            sumfile.write(f"Total sum: {total}\n") #format for output in new file
        
        print(total)

    except FileNotFoundError: #create exception to prevent code error
        print("Error: 'numbers.txt' not found. Please create the file with numbers")
    except ValueError as e:
        print("Error: Found a non-numeric value. Please ensure all lines contain valid numbers")
    finally:
        print("File processing complete.")
if __name__=="__main__":
    process_numbers()