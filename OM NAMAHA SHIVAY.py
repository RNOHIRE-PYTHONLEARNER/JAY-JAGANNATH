a=input("STUDENT'S NAME")
s={"ALICE" :56,"SHIVA" :89,"AMAN" :78,"ASHISH":90,"SAMEER":89}
if a in s:
    print(f"{a}'s number is {s[a]}")
else:
    print("student's NAME WAS NOT fOUND")


original_list=list(range(1,11))
extracted_list=original_list[:5]
reversed_list=extracted_list[::-1]
print("original_list:",original_list)
print("extracted_list:",extracted_list)
print("reversed_list:",reversed_list)