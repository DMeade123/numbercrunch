def reprocess_numbers(): #define process numbers function
    total_sum = 0 #declare adjustable variable
    line_count = 0 #declare variable to store line count
    min_number = float(0)
    max_number = float(0)

    with open("error_log.txt", "w") as error_log:
        try:
            with open("numbers.txt", "r") as numfile:
                for line in numfile:
                    try:
                        number = float(line.strip())
                        
                        total_sum += number
                        line_count += 1

                        if number < min_number:
                            min_number = number
                        if number > max_number:
                            max_number = number
                        
                        average = total_sum / line_count
                    
                    except FileNotFoundError: #create exception to prevent code error
                        print("Error: 'numbers.txt' not found. Please create the file with numbers")
                    except ValueError as e:
                        print("Error: Found a non-numeric value. Please ensure all lines contain valid numbers")
                    except FileNotFoundError:
                        print(f"Error: The file {numfile} does not exist.")
                        return None
        except ValueError:
            error_log.write(f"Warning: {line.strip()} is not a valid number and was skipped.\n")
        finally:
            print("File processing complete.")

            with open("report.txt", "w") as reportfile: #write sum in blank file
                reportfile.write("Report:\n")
                reportfile.write("-------\n")
                reportfile.write(f"Count: {line_count}\n")
                reportfile.write(f"Sum: {total_sum}\n")
                reportfile.write(f"Average: {average}\n")
                reportfile.write(f"Minimum: {min_number}\n")
                reportfile.write(f"Maximum: {max_number}\n")
if __name__=="__main__":
    reprocess_numbers()