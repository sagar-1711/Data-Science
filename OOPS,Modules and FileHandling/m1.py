
#M1 Module  __main__
if __name__=='__main__':
    #Specify what to do when this modle is run directly
    print("M1 Module ",(__name__))
else:
    #Specify what to do when this modle is imported
    print("I am in M1,else block")
