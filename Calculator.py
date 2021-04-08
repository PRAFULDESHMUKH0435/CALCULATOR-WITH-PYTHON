
print("ENTER FIRST NUMBER")
a=int(input())
print("ENTER SECOND NUMBER")
b=int(input())
print("PLEASE ENTER OPERATOR\n"
      "\033[94m+  FOR ADDITION\n"
      "-  FOR SUBTRACTION\n"
      "*  FOR MULTIPLICATION\n"
      "/  FOR DIVISION\n")
c = input()

if(c=="+"):
    print("\033[92mTHE SUM OF GIVEN TWO NUMBERS IS ", a+b)

elif(c=="-"):
    print("\033[92mTHE SUBTRACTION OF GIVEN TWO NUMBERS IS ", a-b)

elif (c == "*"):
    print("\033[92mTHE MULTIPLICATION  OF GIVEN TWO NUMBERS IS ", a*b)

elif (c == "/"):
    print("\033[92mTHE DIVISION OF GIVEN TWO NUMBERS IS ", a/b)
else:
    print("\033[91mINVALID OPERATOR")
