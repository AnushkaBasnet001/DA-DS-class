# File Handling flow
# Open the file => file = open("file_path", mode)
# perform operation on the file
# r => read mode
# w => write mode
# a => append mode
# close the file => file.close()

# r mode
# read the content of the file => file.read()
# IF file is opened in read mode, but the file doesnot exist, then it throws an error
file = open("abc.txt","r") 
content = file.read()
file.close()
print(content)

# w mode
# write the content in the file
# We can write only string or JSON in file
# JSON = JavaScript Object Notation -> It is similar to dictionary
# If file is opened in write mode but the file doenot exist: it creates a new file with the name provided
# in write mode, the previous content is erased and only the new content is written in the file
file = open("abc.txt","w")
file.write("")
file.close()


# a => append mode
# append the content in the file at last of file
# We can write only string or JSON in file
# If a file is opened in append mode but file doesnot exist, it creates a new file
# In append mode, previous content is preserved and new content is append at last
# file = open("abc2.txt","a")
# file.write("-Ujjwal Neupane")
# file.close()



# # Task:
# 1. Create and Write a File
# Write a program to create a new text file named notes.txt, write multiple lines of text into it, and ensure the file closes properly using a with statement.
# 2. Read Entire File Content
# Write a program to open notes.txt in read mode ('r'), load all its text into a string using read(), and print the contents to the console.
# 3. Read File Line by Line
# Write a program that iterates through notes.txt using a for loop to read and print each line individually after stripping out extra newline characters.
# 4. Append New Data
# Write a program to open notes.txt in append mode ('a') and add a new timestamp or log line to the bottom without erasing existing content.
# 5. Count Lines, Words, and Characters
# Write a program that opens a text file, counts the total number of lines, words, and characters inside it, and displays the summary.
# 6. Find and Replace Text
# Write a program that reads a file, searches for a specific target word (for example, change all instances of "old" to "new"), and saves the updated text back to the file.
# 7. Copy File Contents
# Write a program that opens a source file (source.txt), reads its content, and writes that exact content into a new destination file (backup.txt).
# 8. Read and Write CSV Data
# Write a program using Python's built-in csv module to read rows from a .csv file, filter or modify the data, and write the output into a new .csv file.
# 9. Handle Missing Files with Try-Except
# Write a program that attempts to open a non-existent file using a try...except block to catch FileNotFoundError and print a friendly warning message instead of crashing.
# 10. Check File Existence and Delete
# Write a program that checks if a file exists using os.path.exists() or Path.exists(), and safely deletes it using os.remove() if confirmed.