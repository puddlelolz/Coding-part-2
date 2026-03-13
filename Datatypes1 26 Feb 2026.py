print("Counting scores!!")
name = input("name of the student?")
indonesian = int(input("score for indonesian?"))
computer = int(input("score for Coding and computer?"))
print("")
print("")
print("Couting...")
print(f"Student: {name}")
print("average score of student:")
print((indonesian + computer)/ 2)
if((indonesian + computer)/ 2) >=80:
    print("PASS")
else:
    print("FAILED")