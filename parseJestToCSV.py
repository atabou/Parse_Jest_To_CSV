

filePath = input("Please input the file path: ")
methodName = input("Please enter the method name: ")

print("\nOpening input file..")

try:
    fp = open(filePath, "r")
except:
    print("There was an error opening the file.\n")
    exit(-1)

print("Successfully opened input file.\n")

print("Starting to read input file..")

Names = []
Inputs = []
Expecteds = []

while line := fp.readline():

    if ("test" in line) and ("async" in line):

        start_recording = False

        name = ""

        for letter in line:

            if letter == "\"" and start_recording == True:
                break

            if start_recording == True:
                name += letter

            if letter == "\"" and start_recording == False:
                start_recording = True

        Names.append(name)


    if ("let" in line) and (methodName in line):
        
        start_recording = False
        fInput = ""
        
        for letter in line:
            
            if letter == ")" and start_recording == True:
                break

            if start_recording == True:
                fInput += letter

            if letter == "(" and start_recording == False:
                start_recording = True

        Inputs.append(fInput)

    if ("expect" in line) and ("toBe" in line):

        start_recording = False
        fExpected = ""

        for i in range( len(line) ):
            
            if line[i:i+4] == "toBe":
                start_recording = True
                
            
            if start_recording == True and line[i+5] == ")":
                break

            if start_recording == True:
                fExpected += line[i+5]

        
        Expecteds.append(fExpected)

print("Finished reading input file.\n")

fp.close()

outputPath = input("Please input output path: ")

try:
    op = open(outputPath, "w")
except:
    print( "There was an error opening the ouput file.\n" )
    exit(-1)

print("Successfully opened output file.")

for i in range( len(Names) ):
    op.write(Names[i] + "," + Inputs[i] + "," + Expecteds[i] + ",\n")

print("Successfully wrote all data.")

op.close()



