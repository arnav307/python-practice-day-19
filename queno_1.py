check=False
def check_quotes():
    with open ('open_file.txt','w') as openfile:
        file_name=openfile.write("Today’s high temperature will be 75 degrees")
        print(file_name)
check_quotes()
                                 
    