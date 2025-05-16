try :
    a= int (input( "Enter a Number"))
    b= int (input("Enter a Number "))
except ValueError as e:
    print ("Value Error:" ,e )
except Exception as e :
    print("Something Went Wrong :",e)
finally:
    print("Done !")           

