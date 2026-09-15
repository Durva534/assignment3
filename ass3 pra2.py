str1 = "The Maharaja Sayajirao University of Baroda, Vadodara"
str2 = "Dussera"

print("a. capitalize():", str1.capitalize())

print("b. len():", len(str1))

print("c. center():")
print(str2.center(70, '*'))
print(str2.center(20))

print("d. casefold():", str1.casefold())

print("e. count():", str1.count("a"))

print("f. endswith():", str1.endswith("Vadodara"))

print("g. encode():", str1.encode())

print("h. find():", str1.find("University"))

name = "Maharaja"
print("i. format():", "Welcome to {} University".format(name))

print("j. index():", str1.index("University"))

print("k. isalnum():", "MSU123".isalnum())

print("l. isalpha():", "Maharaja".isalpha())

print("m. isdecimal():", "12345".isdecimal())

print("n. isdigit():", "12345".isdigit())

print("o. isidentifier():")
print("myname".isidentifier())      
print("myname4".isidentifier())     
print("45myname".isidentifier())    

print("p. islower():", "hello world".islower())

print("q. isnumeric():", "12345".isnumeric())

print("r. isprintable():", "Hello World".isprintable())

print("s. isspace():", "   ".isspace())

print("t. istitle():", str1.istitle())

print("u. isupper():", "HELLO WORLD".isupper())

words = ["The", "Maharaja", "University"]
print("v. join():", " ".join(words))

print("w. ljust():", str2.ljust(20, '*'))

print("x. rjust():", str2.rjust(20, '*'))

print("y. lower():", str1.lower())

print("z. upper():", str1.upper())

print("aa. swapcase():", str1.swapcase())

str3 = "   Hello World"
print("bb. lstrip():", str3.lstrip())

str4 = "Hello World   "
print("cc. rstrip():", str4.rstrip())

str5 = "   Hello World   "
print("dd. strip():", str5.strip())

print("ee. replace():", str1.replace("Vadodara", "Gujarat"))

print("ff. rfind():", str1.rfind("a"))

print("gg. rindex():", str1.rindex("a"))

print("hh. split():", str1.split())

print("ii. rsplit():", str1.rsplit(" ", 2))

print("jj. startswith():", str1.startswith("The"))

print("kk. title():", str1.title())
