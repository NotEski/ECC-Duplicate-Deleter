import csv, os
from tkinter.filedialog import askopenfilename

ECC_CSV_File = askopenfilename(initialdir= os.getcwd(), title= "Please select the ECC CSV file:", filetypes=[("csv files", "*.csv")])       # Grabs the CSV file that contains all of the error codes

csvfile = open (ECC_CSV_File,"r")
csvDict = csv.DictReader(csvfile)   # Converts CSV file to dict

csvfile = open ((ECC_CSV_File[0:-4] + "-Duplicates_And_Toner_Removed.csv"), "w")    # Creates a new file to store data with removed duplicates

FreshDict = {}

Error = ["TonerBagFull", "TonerBagFullSupplyOrder", "WasteTonerBoxNearFull"]        # states all of the different states that the software is looking for

FileString = "Customer Number,Customer Account ID,Customer Name,Machine ID,Serial Number,Model,Event Occurrence Date & Time,Error Code,Error Description\n" # Creates the CSV from scratch this states all of the titles
for i in csvDict:       # Runs through all of the items from the list only adding unique entries based on the list of same errors from above
    if i["Serial Number"] not in FreshDict.keys() and i["Error Description"] in Error:      
        FreshDict[i["Serial Number"]] = 1
        CustomerNumber,CustomerAccountID,CustomerName,MachineID,SerialNumber,Model,EventOccurrenceDateTime,ErrorCode,ErrorDescription = i["Customer Number"],i["Customer Account ID"],i["Customer Name"],i["Machine ID"],i["Serial Number"],i["Model"],i["Event Occurrence Date & Time"],i["Error Code"],i["Error Description"]
        FileString += f"{CustomerNumber},{CustomerAccountID},{CustomerName},{MachineID},{SerialNumber},{Model},{EventOccurrenceDateTime},{ErrorCode},{ErrorDescription}\n"      # Adds the item to the end of the string
        
csvfile.write(FileString)   # Finishes creating the new file
csvfile.close()