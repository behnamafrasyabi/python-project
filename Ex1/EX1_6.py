def EX1_6(number):
    '''
This function can convert numbers from 1 to 10 into Roman numerals
'''
    if number>10 or number<1:
        return("the number is not correct")
    else:   
        x=["I","II","III",'IV','V','VI','VII','VIII','IX','X']
        nunber=number-1
        return(x[nunber])








print(EX1_6(9))
