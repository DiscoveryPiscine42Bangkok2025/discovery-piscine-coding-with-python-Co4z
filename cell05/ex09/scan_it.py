import re
text1 = input("keyword: ")
text2 = input("sentens: ")
matches = re.findall(text1,text2)
print(len(matches))
