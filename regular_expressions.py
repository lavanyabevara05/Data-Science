########## REGULAR EXPRESSIONS ##################

# import re
# text="python  is  easy "
# result=re.search("easy",text)
# res=re.match("easy",text) # apply for check the start values only
# print(result)
# print(res)
# print(result.group())
# print(result.start())
# print(result.end())
# print(result.span())

# import re
# text="I Scored 85 and 90  marks in the end sem examination"
# result=re.findall(r"\d+",text)
# print(result)

# import re
# text="apple bat cat rat"
# result=re.findall(r"[abcr]at",text)
# print(result)

# import re
# mobile="9908541869"
# if re.fullmatch("[6-9]\\d{9}",mobile):
#     print("Valid number")
# else:
#     print("Invalid number")


# import re
# email=input("enter the email: ")
# if re.fullmatch(r"\w+@\w+.\w+",email):
#     print("Valid Email")
# else:
#     print("Invalid Email")

import re
# text="python is a easy language"
# print(re.match("python",text))

# text="Learning Python is fun"
# print(re.search("Python",text))

# str="lav1853"
# print(re.findall(r"\d+",str))

# marks= "78 85 90"
# print(re.findall(r"\d+",marks))

# print(re.match(r"\d{5}","12234"))

# print(re.match(r"^a\w*","abjfgugug567tug"))

# print(re.match(r"[a-z]+","hfyufguygfyuvg"))

# print(re.findall("\\w+ing", "loving is anything"))

# print(re.match(r"^[a-zA-Z0-9]+$", "hfgfdgf64546gduyfgjhjdf"))

# print(re.fullmatch(r"^\d{6}$","522212"))

# txt=input("Enter the string: ")
# if(re.fullmatch(r"^CSE_N22\d{4}$", txt)):
#   print("Valid")
# else:
#   print("Invalid")

# txt=input("enter the number: ")
# print(re.fullmatch(r"^(19\d{2}|20\d{2})$",txt))

# txt="Lav Lav"
# print(re.sub(r"\s"," ❤️  ",txt))

# mobile=input("enter the 10 digit mobile number:")
# if len(mobile)==10 and mobile.isdigit():
#   masked=mobile[:2] +  "*" * 6 + mobile[-2:]
#   print("Masked Number:", masked)

# else:
#   print("Invalid Number")

# password=input("Enter the password: ")
# pattern=r"^(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&]).{8,}$"
# if re.match(pattern,password):
#   print("Strong password")
# else:
#   print("Weak password")

# date=input("Enter the Date: ")
# pattern=r"^\d{2}/\d{2}/\d{4}$"
# if re.match(pattern,date):
#   print("Valid Date Format")
# else:
#   print("Invalid Date Format")



