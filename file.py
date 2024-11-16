import sys

def file(file_name: str):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                parts = line.split()
                if len(parts) != 2: #Each line must have 2 values
                    print("Error: Line does not contain exactly two values: " + line)
                else:
                    try:
                        num1 = float(parts[0]) #Turns to float
                        num2 = float(parts[1]) #Turns to float
                        print("Sum: " + str(num1 + num2)) #Displays sum of floats
                    except ValueError: #Missing Value or Cannot be Converted
                        print("Error: Could not convert values to floats: " + line)
    except FileNotFoundError: #File could not be opened
        print("Error: File '" + file_name + "' not found.")
        sys.exit(1) #Exit with error
    except IOError: #File could not be provided
        print("Error: Could not open file '" + file_name + "'.")
        sys.exit(1) #Exit with error


def main():
    file_name = input("Please enter the file name: ")
    if not file_name:
        print("Error: No file name provided. Please provide a valid file name.")
        sys.exit(1)
    file(file_name)
if __name__ == "__main__":
    main()