NAME=input("ENTER YOUR NAME:")
MARK1=int(input("enter the mark1:"));
MARK2=int(input("enter the mark2:"));
MARK3=int(input("enter the mark3:"));
MARK4=int(input("enter the mark4:"));
MARK5=int(input("enter the mark5:"));
MARK6=int(input("enter the mark6:"));
TOTALMARKS=MARK1+MARK2+MARK3+MARK4+MARK5+MARK6
print("TOTAL MARK IS: ",TOTALMARKS)
if(TOTALMARKS > 100):
    if(TOTALMARKS < 600 and TOTALMARKS > 590):
        print("CONGRATS YOUR THE OUTSTANDING STUDENT AND YOU GET A 'O' GRAD")
    elif(TOTALMARKS > 400 and TOTALMARKS < 590):
        print("CONGRATS YOUR GET 'A' GRAD TRY MORE YOU GET 'O'GRAD.....")
    elif(TOTALMARKS > 300 and TOTALMARKS < 400):
        print("CONGRATS YOUR GET 'B' GRAD KEEPGOING.....")
    elif(TOTALMARKS > 200 and TOTALMARKS < 350):
        print("YOUR GET 'C' GRAD  WELTRY........ ")
    elif(TOTALMARKS > 600):
        print("YOUR OVER QUALIFIED")
else:
        print("YOUR FAIL BETTER LOCK NEXT TIME")