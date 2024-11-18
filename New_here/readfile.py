# with open("file.txt", "w") as file_obj:
#   file_obj.write("Clean everything except this.")

# file_obj = open("C:/Users/danso/Bootstrap_Free_Training/New_here/file.txt", "r")        #This opens the file.txt and read the content

# print(file_obj.read())

file_obj = open("C:/Users/danso/Bootstrap_Free_Training/New_here/file.txt", "a")

file_obj.writelines(["Line 1\n", "Line 2\n", "Line 3\n"])