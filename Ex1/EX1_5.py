def EX1_5(x):
    '''
This function can announce the person's life status by taking the person's age
'''
    if x<1:
        return("infant")
    elif x<13:
        return("child")
    elif x<20:
        return("teenager")
    else :
        return("adult")
