file1= None
try:
 file1=open('sample.txt','r')
 for line  in file1:
  print(line.strip())
except FileNotFoundError:
 print("File was not found")
finally:
    if 'file1' in locals():
         file1.close()


d=input("ENTER DATA")
file2=open('output.txt','a')
appending_file=file2.write(d)
file2.close()
with open("output.txt") as file2:
    reading_file=file2.read()
    print(reading_file)


