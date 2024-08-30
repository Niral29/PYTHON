n=0
a=input("Enter valid email-address : ")
if(len(a)>=6):
    if(a[0].isalpha()):
        if "@" in (a) and (a.count("@")==1):
            if "." in (a) and (a.count(".")==1) and (a[-4]):
               if(a==a.lower()):
                  print("Validation Successfuly completed")
               else:
                   print("Invalid Upper-case")
            else:
                print(" . not present")
        else:
            print("@ not present") 
    else:
        print("Use alphabet first in space")

else:
    print("require 6-letter")

