#if you can anticipate a piece of you software that is going to throw
#an error ,use :
#try - except - else - finally



try:
    p = open("Magma.py")
    #var = _bad_var
    print("Awe")
except FileNotFoundError as fnf:
    print("Oupsy ,your file doesn't exist")
    print(fnf)
except NameError as ner:
    print("Wrong name")
    print(ner)
except Exception as e : #General exeption handling
    print("Okey ,I do not know what happened")
    print(e)
else: #it only runs code that needs to be executed if TRY DOESN'T RAISE an exception
    print ("Ok try didn't throw an exeption")
finally: #it will run no matter what situation
    print("Ok this is the end of the code")



