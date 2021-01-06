import csv

def writting(list1):
    with open('stud_info.csv','a', newline='') as csv_file:
        writer = csv.writer(csv_file)


        if csv_file.tell() == 0:
            writer.writerow(["Name","Age","Contact Number","E-Mail ID"])

        writer.writerow(list1)

condition = True

while(condition):
    stud_info = input("Enter the Student's information by the format (Name Age Contact_Number E-Mail-ID :")
    
    stud_info_list2 = stud_info.split(' ')
    writting(stud_info_list2)
    
    print("Entered Information is saved successfully")

    condition_check = input("Enter yes/no to add another student's Information: ")
    if condition_check == "yes":
        condition = True
    elif condition_check == "no":
        condition = False
    else:
        print("type yes/no correctly")
        continue


    
